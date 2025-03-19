from typing import List
from user_model import UserModel

class UserRepository:

    users: List['UserModel'] = []


    def save(self, user: 'UserModel') -> 'UserModel':
        if user.email in UserRepository.users:
            print({'status': 404, 'message': f'User with {user.email} already exists'})
        else:
            return UserRepository.users.append(user)
    
    def find_user_by_email(self, email: str) -> 'UserModel':
        if email in UserRepository.users:
            return [user for user in UserRepository.users if user.email == email]
        return {'status': 404, 'message': 'User not found'}
    
    def delete_user_email(email: str) -> str:
        if email in UserRepository.users:
            UserRepository.users = [user for user in UserRepository.users if user.email != email]
            return {'status': 200, 'message': 'User successfully deleted'}
        return {'status': 404, 'message': 'User not found'}
    
    def find_all_users(self) -> List['UserModel']:
        saved_users = [u for u in UserRepository.users]
        return saved_users
