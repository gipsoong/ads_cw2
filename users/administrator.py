from user import User


class Administrator(User):

    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
