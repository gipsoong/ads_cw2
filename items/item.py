class Item:
    def __init__(self, title, category, language, authors, year_published):
        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published

    def return_title(self):
        return self.title

    def return_category(self):
        return self.category

    def return_language(self):
        return self.language

    def return_authors(self):
        return self.authors

    def return_year_published(self):
        return self.year_published

    def __str__(self):
        return f"{self.title}, published in {self.year_published} by {self.authors}"
