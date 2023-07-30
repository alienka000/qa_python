import pytest
from main import BooksCollector


@pytest.fixture
def books():
    collector = BooksCollector()
    collector.books_genre = {
        'Песнь льда и пламени' : 'Фантастика',
        'Десять негритят': 'Детективы',
        'Двенадцать стульев' : 'Комедии',
        'Элла в первом классе' : 'Комедии'
    }
    return collector

