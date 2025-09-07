class Mates:
    def __init__(self, name, gender, height):
        self.name = name
        self.gender = gender
        self.height = height 
    
    def Desc(self):
        print(f"Hi \n My name is {self.name} \n I am a {self.gender} \n i think am {self.height}")


mate1 = Mates("Prince", "Male", "tall")
mate2 = Mates("Collins", "Male", "Short")
mate3 = Mates("DUmebi", "Female", "Short")

mate1.Desc()
mate2.Desc()
mate3.Desc()

