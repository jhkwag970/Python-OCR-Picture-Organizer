class Annotation:
    def __init__(self,file,description,score):
        self.__file = file
        self.__description = description
        self.__score = score

    def getFile(self):
        return self.__file
    
    def getDesc(self):
        return self.__description

    def getScore(self):
        return self.__score
    
    def toString(self):
        print("File: ",self.getFile())
        print("desc: ",self.getDesc())
        print("score: ",self.getScore)
        print("-------------------------")
