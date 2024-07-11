from abc import ABC, abstractmethod

class FoodItem(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> str:
        pass

    @abstractmethod
    def get_image(self) -> str:
        pass

class Sandwich(FoodItem):
    def __init__(self, name: str, price: str, image: str):
        self.__Name = name
        self.__Price = price
        self.__Image = image

    def get_name(self) -> str:
        return self.__Name

    def get_price(self) -> str:
        return self.__Price

    def get_image(self) -> str:
        return self.__Image

class Drinks(FoodItem):
    def __init__(self, name: str, price: str, image: str):
        self.__Name = name
        self.__Price = price
        self.__Image = image

    def get_name(self) -> str:
        return self.__Name

    def get_price(self) -> str:
        return self.__Price

    def get_image(self) -> str:
        return self.__Image

class Sides(FoodItem):
    def __init__(self, name: str, price: str, image: str):
        self.__Name = name
        self.__Price = price
        self.__Image = image

    def get_name(self) -> str:
        return self.__Name

    def get_price(self) -> str:
        return self.__Price

    def get_image(self) -> str:
        return self.__Image


