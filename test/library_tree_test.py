from node import Node
from items.book import Book
from functions import *


def main():
    metamorphosis = Book("Meta", "Novel", 'English', 'Franz Kafka',
                         1915, 104592)

    bible = Book("Bible", "Biography", 'English', 'Adam',
                 1915, 104592)

    quran = Book("Quran", "Religious Text", 'English', 'Muhammad',
                 1915, 104592)

    test = Book("Test", "Test", 'English', 'Franz Kafka',
                2022, 104592)

    genshin = Book("Genshin", "Game", 'English', 'Franz Kafka',
                   1915, 104592)

    honkai = Book("Honkai", "Story", 'English', 'Franz Kafka',
                  1915, 104592)

    cow = Book("Cow", "Animal", 'English', 'Farmer',
                  2020, 104592)

    items = [metamorphosis, bible, quran, test, genshin, honkai, cow]

    sorted_list = sort_items_by_title(items)
    middle_index = return_middle_of_list(sorted_list)

    # start with creating the root of the tree, in this case it is 'Honkai'
    library_tree = Node(middle_index, return_value_of_middle_index(items, middle_index))

    # will create a function to loop through rest of the list and insert, but this will do for now
    library_tree.insert("Metamorphosis", metamorphosis)
    library_tree.insert("Bible", bible)
    library_tree.insert("Quran", quran)
    library_tree.insert("Genshin", genshin)
    library_tree.insert("Cow", cow)
    library_tree.insert("Test", test)

    print(library_tree.find("Cow"))
    # library_tree.preorder()


main()
