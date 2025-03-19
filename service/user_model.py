class UserModel:

    def __init__(self, email: str, name: str, age: int, address):
        self.email = email
        self.name = name 
        self.age = age
        self.address = address
        self.wallet = 0.0
    
    def __repr__(self):
        print(f"<User email: {self.email}, name: {self.name}, wallet {self.wallet}")
        return f"{self.email}, name: {self.name}, wallet {self.wallet}>"
