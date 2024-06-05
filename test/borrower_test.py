from users.borrower import Borrower
from items.book import Book


def main():
    book1 = Book('Metamorphosis', 'Self Help', 'English',
                 'Franz Kafka', 1915, 10)

    book2 = Book('Hello', 'Autobiography', 'German',
                 'Adele', 1915, 12)

    jane_doe = Borrower('Jane', 'Doe', 'janedoe2', 'password123',
                        800, [book1, book2])

    print(jane_doe.return_borrowed_items())


main()
