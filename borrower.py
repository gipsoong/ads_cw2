from user import User


class Borrower(User):

    def __init__(self, first_name, last_name, username, password, account_number, borrowed_items):
        super().__init__(first_name, last_name, username, password)
        self.account_number = account_number
        self.borrowed_items = borrowed_items

    def return_account_number(self):
        return self.account_number

    def return_borrowed_items(self):
        if self.check_borrowed_items():
            return self.borrowed_items()
        else:
            return False

    def check_borrowed_items(self):
        if 0 < len(self.borrowed_items) > 8:
            return False
        else:
            return True
