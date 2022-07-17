class Human:
    # __init__ is a method for initialize values of class
    # first argument is "self" which means class itself 
    def __init__(self,object_name,object_occupation):
        self.name=object_name
        self.occupation=object_occupation
    def do_work(self):
        if self.occupation=='Actor':
            print(self.name,"Shoots a Film ")
        elif self.occupation=='Tennis Player':
            print(self.name,"Plays Tennis ")
    def speak(self):
        print(self.name,'says How are you ')
tom = Human("Tom Cruise","Actor")
tom.do_work()
tom.speak()
print("\n")
maria = Human("Maria Sarapoba","Tennis Player")
maria.do_work()
maria.speak()
