from users.user import User


class Borrower(User):

    def __init__(self, first_name, last_name, username, password, account_number, borrowed_items):
        super().__init__(first_name, last_name, username, password)
        self.account_number = account_number
        self.borrowed_items = borrowed_items

    def return_account_number(self):
        return self.account_number

    def return_borrowed_items(self):
        borrowed_string = 'BORROWED ITEMS: '
        if self.check_borrowed_items():
            for i in self.borrowed_items:
                borrowed_string += f"{i.title}, "
        else:
            return False

        return borrowed_string

    def check_borrowed_items(self):
        if 0 < len(self.borrowed_items) > 8:
            return False
        else:
            return True
