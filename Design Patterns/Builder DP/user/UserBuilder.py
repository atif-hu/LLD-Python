from .User import User

class UserBuilder:
    def __init__(self) -> None:
        self.firstname=""
        self.lastname=""
        self.age=0
        self.street=""

    @staticmethod
    def item():
        return UserBuilder()
    
    def withFirstName(self,name):
        self.firstname=name
        return self
    
    def withLastName(self,name):
        self.lastname=name
        return self
    
    def withAge(self,age):
        self.age=age
        return self
    
    def liveInStreet(self,street):
        self.street=street
        return self
    
    def build(self):
        return User(self.firstname,self.lastname,self.age,self.street)
    

