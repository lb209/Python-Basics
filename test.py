class Passw:
    def __init__(self, password):
        self.__password = password   # 🔒 private

    def set_password(self):
        if self.__password:
            print("Password set successfully")
        else:
            print("Password not set")

    def check_password(self, user_input):
        if self.__password == user_input:
            print("Access granted")
        else:
            print("Access denied")


s1 = Passw("1234")
s1.set_password()
s1.check_password("1234")