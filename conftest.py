import pytest
from main import BooksCollector


# Добавление 3 книг с жанрами
@pytest.fixture
def books():
    collector = BooksCollector()
    collector.books_genre = {
        'Песнь льда и пламени': 'Фантастика',
        'Десять негритят': 'Детективы',
        'Двенадцать стульев': 'Комедии',
        'Элла в первом классе':'Комедии',
        'Пикник на обочине':'Фантастика'
    }
    return collector

# Создание списка Избранных книг
@pytest.fixture
def books_in_favorites(books):
    books.add_book_in_favorites('Песнь льда и пламени')
    books.add_book_in_favorites('Двенадцать стульев')
    books.add_book_in_favorites('Элла в первом классе')
    return books.favorites
