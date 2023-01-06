from pydantic import BaseModel

class User(BaseModel):
    user_email: str
    password: str

    def get_email(self):
        return self.user_email

    def get_password(self):
        return self.password
