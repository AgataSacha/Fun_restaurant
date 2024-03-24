class CustomError(Exception):
    def __init__(self, message):
        print(message)
class InvalidNumberError(CustomError):
    def __init__(self):
        super().__init__("Podałeś/aś nieprawidłową wartość")

class checkNumber(InvalidNumberError):
    def __init__(self,k):
        if k != 1 and k != 2 and k != 3:
            raise InvalidNumberError