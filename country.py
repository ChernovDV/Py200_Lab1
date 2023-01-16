class Country:
    """Класс описывает страну"""
    def __init__(self, population:int, language:str, capital:str):
        """Инициализация экземпляра класса"""
        self.population = population
        self.language = language
        self.capital = capital

    def population_growth(self, percent:int)->int:
        """Метод определяет прирост населения страны
        >>> irland = Country(1000000, "английский", "Дублин")
        >>> irland.population_growth(15)
        150000"""
        growth = int(self.population*percent/100)
        return growth

    def population_decline(self, percent:int)->float:
        """Метод определяет уменьшение населения страны"""
        decline = self.population*percent/100
        return decline