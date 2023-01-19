
class Data:
    def __init__(self):
        f = open('Admin','r')
        self.name = f.readline()[0].strip()
        self.pushdata = f.readline()[1].strip()
        self.warmup= f.readline()[2].strip()
        self.eyedistance= f.readline()[3].strip()
        self.eyetired= f.readline()[4].strip()
        self.audiopush= f.readline()[5].strip()
        self.squint= f.readline()[6].strip()
        self.spine= f.readline()[7].strip()
    def save(self):
        f = open('Admin','w')
        f.write(self.name + '\n')
        f.write(self.pushdata + '\n')
        f.write(self.warmup + '\n')
        f.write(self.eyedistance + '\n')
        f.write(self.eyetired + '\n')
        f.write(self.audiopush + '\n')
        f.write(self.squint + '\n')
        f.write(self.spine + '\n')
    def set(self):
        f = open('Admin','r')
        self.name = f.readline()[0].strip()
        self.pushdata = f.readline()[1].strip()
        self.warmup= f.readline()[2].strip()
        self.eyedistance= f.readline()[3].strip()
        self.eyetired= f.readline()[4].strip()
        self.audiopush= f.readline()[5].strip()
        self.squint= f.readline()[6].strip()
        self.spine= f.readline()[7].strip()

