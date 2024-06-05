from item import Item


class AudioBook(Item):

    def __init__(self, title, category, language, authors, year_published, isbn, audio_format):
        super().__init__(title, category, language, authors, year_published)

        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published
        self.isbn = isbn
        self.audio_format = audio_format

    def return_isbn(self):
        return self.isbn

    def return_audio_format(self):
        return self.audio_format

    def __str__(self):
        return f"{self.title}, published in {self.year_published} by {self.authors}"