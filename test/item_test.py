from items.book import Book
from items.audio_book import AudioBook
from items.periodical import Periodical


def main():
    metamorphosis = Book("Metamorphosis", "Novel", 'English', 'Franz Kafka',
                         1915, 104592)

    mein_kampf = Book("Mein Kampf", "Autobiography", 'English', 'Adolf Hilter',
                      1943, 340949)

    podcast1 = AudioBook("Podcast 1", "Podcast", 'English', 'Podcast Bro',
                         2023, 495091, 'mp3')

    podcast2 = AudioBook("Podcast 2", "Podcast", 'English', 'Podcast Sis',
                         2024, 959135, 'wav')

    straits_times = Periodical("The Straits Times", "Newspaper", 'English', 'Editor',
                               2025)

    her_mag = Periodical("Her", "Magazine", 'English', 'Girl',
                         2020)

    print(metamorphosis.id)
    print(mein_kampf.id)
    print(podcast1.id)
    print(podcast2.id)
    print(straits_times.id)
    print(her_mag.id)


main()
