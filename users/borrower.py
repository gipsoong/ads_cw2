from user import User


class Borrower(User):

    def __init__(self, first_name, last_name, username, password, account_number, borrowed_items):
        super().__init__(first_name, last_name, username, password)
        self.account_number = account_number
        self.borrowed_items = borrowed_items

    def return_account_number(self):
        return self.account_number

    def borrowed_items(self):
        return self.borrowed_items()
