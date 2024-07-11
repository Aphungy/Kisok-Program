from abc import ABC, abstractmethod

class Toppings(ABC):

  @abstractmethod
  def get_name(self) -> str:
      pass
  
  @abstractmethod
  def get_price(self) -> str:
      pass

class SandwichToppings(Toppings):
  def __init__(self, name: str, price: str):
      self.__Name = name
      self.__Price = price

  def get_name(self) -> str:
      return self.__Name

  def get_price(self) -> str:
      return self.__Price