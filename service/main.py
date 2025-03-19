

from user_model import UserModel
from user_repository import UserRepository


fred = UserModel('fred@ait.edu.com', 'fred', 32, "Nima street")

users = [
    UserModel('fred1@ait.edu.com', 'fred', 32, "Nima street"),
    UserModel('fred2@ait.edu.com', 'fred', 32, "Nima street"),
    UserModel('fred3@ait.edu.com', 'fred', 32, "Nima street"),
    UserModel('fred4@ait.edu.com', 'fred', 32, "Nima street")
]

user_repository = UserRepository()
for user in users:
    user_repository.save(user)
    # print(t)
# print("Print all users")
 
user_repository.save(fred)
print(user_repository.find_all_users())
print(user_repository.find_user_by_email(fred.email))

