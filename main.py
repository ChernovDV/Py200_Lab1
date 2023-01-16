import country
import book
import car
import doctest

# Написать 3 класса с документацией и аннотацией типов


if __name__ == "__main__":
# работоспособность экземпляров класса проверить с помощью doctest

    irland = country.Country(1000000, "английский", "Дублин")
    print(irland.population_growth(15))

    book_ = book.Book("Азбука", 1000, 1890)
    print(book_.price())

    moskvich = car.Car("белый", "легковой")
    print(moskvich.price())

doctest.testmod()