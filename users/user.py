

class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def return_first_name(self):
        return self.first_name

    def return_last_name(self):
        return self.last_name

    def return_username(self):
        return self.first_name

    def return_password(self):
        return self.password