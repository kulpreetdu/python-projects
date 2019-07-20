class ThreeD:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def __str__(self):
        return "x: "+str(self.x)+" "+"y: "+str(self.y)+" "+"z: "+str(self.z)
if(__name__=="__main__"):
    ob1=ThreeD()
    print(ob1)