import math
import dlib
import cv2
from Application import posemodule1
import numpy as np
class FatigueDetect:
    def landmarks_to_np(landmarks, dtype="int"):
        num = landmarks.num_parts
        coords = np.zeros((num, 2), dtype=dtype)
        for i in range(0, num):
            coords[i] = (landmarks.part(i).x, landmarks.part(i).y)
        return coords
    def logic(self):
        predictor_path = "./shape_predictor_68_face_landmarks.dat"
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path) #РАЗОБРАТЬСЯ
        video = cv2.VideoCapture(0)
        detect = posemodule1.PoseDetector1()
        queue = np.zeros(30,dtype=int)
        queue = queue.tolist()
        ans = 0
        while 1>0:  #Можно изменить на нажатие какой-то кнопки
            ret,frame = video.read() #ret не нужно, оно проверяет было ли чтение успешным, frame - само изображение

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            rects = detector(gray, 1)
            for i, rect in enumerate(rects):
                x = rect.left()
                y = rect.top()
                w = rect.right() - x
                h = rect.bottom() - y

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2,
                    cv2.LINE_AA)

                landmarks = predictor(gray, rect)
                landmarks = self.landmarks_to_np(landmarks)
                for (x, y) in landmarks:
                    cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

                d1 = np.linalg.norm(landmarks[37] - landmarks[41])
                d2 = np.linalg.norm(landmarks[38] - landmarks[40])
                d3 = np.linalg.norm(landmarks[43] - landmarks[47])
                d4 = np.linalg.norm(landmarks[44] - landmarks[46])
                d_mean = (d1 + d2 + d3 + d4) / 4
                d5 = np.linalg.norm(landmarks[36] - landmarks[39])
                d6 = np.linalg.norm(landmarks[42] - landmarks[45])
                d_reference = (d5 + d6) / 2
                d_judge = d_mean / d_reference

                flag = int(d_judge < 0.25)

        # flag入队
                queue = queue[1:len(queue)] + [flag]

        # 判断是否疲劳：根据时间序列中低于阈值的元素个数是否超过一半
                if sum(queue) > len(queue) / 2:
                    cv2.putText(frame, "WARNING !", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "SAFE", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

            image_reading = detect.findPose(frame) #getting the position on the image/frame
            body,box_reading = detect.findPosition(frame,bboxWithHands=False)
    #Now, lets check the center of each coordinate in the human body
            if box_reading:
                center = box_reading['center']
        #lets draw and give a crircle mark at each joint movement of the body
                cv2.circle(frame,center,5,(255,255,0),cv2.FILLED)

            color_yellow = (0, 255, 255)
            try:
                distance_between_eyes_pixels = math.sqrt((body[2][2]-body[5][2])**2+(body[2][1]-body[5][1])**2)
                distance_between_eyes_real=60
                frame_real_distance=0.02635872298*frame.shape[0]*1.5 # заменить на обычный размер, который можно будет менять в приложении
                screen_distance = distance_between_eyes_pixels**(-1.1321)*7301.5525
                angle_shoulders = detect.findAngle(frame,11,12,body[11][2])
                pixel_distance = frame.shape[0]/2-(body[2][2]+body[5][2])/2
                real_distance=distance_between_eyes_real*pixel_distance/distance_between_eyes_pixels
                angle_sitter=math.asin((real_distance+frame_real_distance)/screen_distance)*180/math.pi

                cv2.putText(frame, "head angle " + str(angle_sitter), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,color_yellow, 2)
                cv2.putText(frame, "Shoulders angle " + str(angle_shoulders), (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 1,color_yellow, 2)
                cv2.putText(frame, "Screen distance "+str(screen_distance), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
        #cv2.putText(frame, "Screen distance with mp "+str((body[2][3]+body[5][3])/2), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)

                cv2.imshow('frame_name',frame) #показ изображения
            except Exception:
                print("Ну ты и кринж, сядь нормально", ans)
                ans += 1
    #если на фото не нашлись нужные нам точки
            if cv2.waitKey(20) and 0xFF == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
a = FatigueDetect()
a.logic()