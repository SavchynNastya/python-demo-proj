class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class President(Person, metaclass=Singleton):
    def __init__(self, name, surname, election_year):
        super().__init__(name, surname)
        self.election_year = election_year


def func():
    print("\nSINGLETON AND INHERITANCE")
    president1 = President("Volodymyr", "Zelenskiy", 2019)
    president2 = President("Joe", "Biden", 2020)
    print("president1 == president2 - ", president1 == president2)
    print(type(president1), " ", type(president2))
