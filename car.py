class Car:

    """Класс описывает машину"""
    def __init__(self, color:str, type:str):
        """Инициализация экземпляра класса"""
        self.color = color
        self.type = type

    def price(self)->int:
        """Метод определяет цену машины
        >>> moskvich = Car("белый", "легковой")
        >>> moskvich.price()
        1000
        """
        price_car = 1000
        return price_car

