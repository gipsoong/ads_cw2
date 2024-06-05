from items.item import Item


class Periodical(Item):
    def __init__(self, title, category, language, authors, year_published):
        super().__init__(title, category, language, authors, year_published)

        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published

    def __str__(self):
        return f"{self.title}, published in {self.year_published} by {self.authors}"