class User:
    def __init__(self,firstname,lastname,age,street) -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.street=street
    
    def getFirstname(self):
        return self.firstname
    
    def setFirstname(self,firstname):
        self.firstname=firstname

    def getLastname(self):
        return self.lastname
    
    def setLastname(self,lastname):
        self.lastname=lastname

    def getAge(self):
        return self.age
    
    def setAge(self,age):
        self.age=age

    def getStreet(self):
        return self.street
    
    def setStreet(self,street):
        self.street=street

    def print(self):
        print("===== User =====")
        print(f"User name :{self.firstname} {self.lastname}")
        print(f"Age: {self.age}")
        print(f"Street: {self.street}")