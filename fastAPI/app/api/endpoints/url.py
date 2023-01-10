
LOGIN = ""


class UserService:
    pass


class Url:
    def router(self, menu):
        if menu == LOGIN:
            UserService().login()