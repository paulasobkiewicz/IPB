class Student:
    def __init__(self, name, indexNo, studyAvg = 0):
        self.name = name
        self.indexNo = indexNo
        self.studyAvg = studyAvg
    
    def setAvg(self, avg):
        self.studyAvg = avg

    def getAvg(self):
        return self.studyAvg

    def __str__(self):
        return self.name +", Index No. "+str(self.indexNo)+", Study avg: "+ str(self.studyAvg)

ali = Student("Kowalski", 12345)

print(ali)
