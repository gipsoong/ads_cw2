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
