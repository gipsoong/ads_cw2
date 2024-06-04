from user import User


class Borrower(User):

    def __init__(self, first_name, last_name, username, password, account_number, rented_items):
        super().__init__(first_name, last_name, username, password)

        self.account_number = account_number
        self.rented_items = rented_items

    def return_account_number(self):
        return self.account_number

    def return_rented_items(self):
        return self.rented_items