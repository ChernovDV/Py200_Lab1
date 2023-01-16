class Book:

    """Класс описывает книгу"""
    def __init__(self, name:str, pages:int, year_publication:int):
        """Инициализация экземпляра класса, при этом на атрибут отвечающий
        за год публикации книги накладывается ограничение"""
        self.name = name
        self.pages = pages
        if year_publication > 2022:
            raise ValueError("Год издания не может быть позже 2021")
        self.year_publication = year_publication

    def price(self)->int:
        """Метод рассчитывает цену книги
        в зависимости от колличества страниц
        >>> book_ = Book("Азбука", 1000, 1890)
        >>> book_.price()
        3000
        """
        price = self.pages * 3
        return price

    def discont(self, discont:int)->int:
        """Метод используется для установления скидки на книгу"""
        if self.pages < 300:
            discont = 500
        return discont