from app.models.user import User


class UserService:
    def login(self, user_email, password):
        user = User(user_email, password)
        print(f" 리액트에서 보낸 이메일: {user.get_email()}")
        print(f" 리액트에서 보낸 비번: {user.get_password()}")