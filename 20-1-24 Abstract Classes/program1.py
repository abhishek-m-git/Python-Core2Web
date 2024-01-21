from abc import ABC,abstractmethod

class Core2Web(ABC):
    
    def slogan(self):
        print("Know the code till the core")

    @abstractmethod
    def courseType(self):
        pass

class python(Core2Web):

    def courseType(self):
        print("This is Python Course")

class flutter(Core2Web):

    def courseType(self):
        print("This is flutter course")

obj1 = python()
obj1.slogan()
obj1.courseType()

obj2 = flutter()
obj2.courseType()
