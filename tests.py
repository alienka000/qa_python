from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Проверка добавления жанра книги - положительный тест
    @pytest.mark.parametrize('book_name, genre',
        [
            ['Песнь льда и пламени', 'Фантастика'],
            ['Десять негритят', 'Детективы'],
            ['Двенадцать стульев', 'Комедии']
        ]
    )
    def test_set_book_genre_three_books_positive(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre


    # Проверка добавления жанра книги - 3 книги с неверным жанром
    @pytest.mark.parametrize('book_name, genre',
                             [
                                 ['Песнь льда и пламени', 'Фантастик'],
                                 ['Десять негритят', 'Детектив'],
                                 ['Двенадцать стульев', 'Комедия']
                             ]
                             )
    def test_set_book_genre_three_books_with_wrong_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] != genre


    # Проверка получения жанра книги по ее имени
    def test_get_book_genre_get_fantasy(self, books):
        bookname = 'Песнь льда и пламени'
        assert books.get_book_genre(bookname) == books.books_genre[bookname]


    # Проверка получения списка книг с определенным жанром
    def test_get_books_with_specific_genre_only_fantasy(self,books):
        genre = 'Фантастика'
        book_list = []
        for book_name in books.books_genre.keys():
            if books.books_genre[book_name] == genre:
                book_list.append(book_name)
        assert book_list == books.get_books_with_specific_genre(genre)


    # Проверка получения словаря books_genre
    def test_get_books_genre_dictionaries_equals(self, books):
        assert books.get_books_genre() == books.books_genre


    # Проверка получения подходящих книг для детей
    def test_get_books_for_children_positive(self, books):
        for book_name in books.get_books_for_children():
            if books.books_genre[book_name] == 'Ужасы' or books.books_genre[book_name] == 'Детективы':
                assert False
                break
            assert True


    # Проверка успешного добавления двух книг в Избранное
    def test_add_book_in_favorites_two_books_positive(self, books):
        book1 = 'Песнь льда и пламени'
        book2 = 'Двенадцать стульев'
        books.add_book_in_favorites(book1)
        books.add_book_in_favorites(book2)
        assert book1 in books.favorites and book2 in books.favorites


    # Проверка добавления в Избранное книги, которой нет в списке
    def test_add_book_in_favorites_book_not_in_list_negative(self, books):
        book = 'Золотой теленок'
        books.add_book_in_favorites(book)
        assert book not in books.favorites


    # Проверка успешного удаления книги из Избранного
    def test_delete_book_from_favorites_positive(self, books, books_in_favorites):
        deleted_book='Элла в первом классе'
        books.delete_book_from_favorites(deleted_book)
        assert deleted_book not in books_in_favorites


    # Проверка получения списка Избранных книг
    def test_get_list_of_favorites_books_positive(self, books, books_in_favorites):
        assert books.favorites == books.get_list_of_favorites_books()




