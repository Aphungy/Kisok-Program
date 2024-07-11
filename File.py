from fooditem import Sandwich, Drinks, Sides
from toppings import SandwichToppings
import os

# Sandwhich read file

def read_sandwiches_from_file(file_name):
    sandwiches_list = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist.")
        return sandwiches_list

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            if len(data) >= 3:
              name = data[0]
              price = data[1]
              image = data[2]
              sandwiches_list.append(Sandwich(name, price, image))
    return sandwiches_list

sandwiches = read_sandwiches_from_file("Fooditems.txt")

if sandwiches:
    for sandwich in sandwiches:
        print("Name:", sandwich.get_name())
        print("Price:", sandwich.get_price())
        print("Image:", sandwich.get_image())
        print()
else:
    print("No sandwiches found.")


# Drinks Read File 

def read_drinks_from_file(file_name):
    drinks_list = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist.")
        return drinks_list

    with open(file_path, 'r') as file:
        for line in file:
          data = line.strip().split(', ')
          if len(data) >= 3:
            name = data[0]
            price = data[1]
            image = data[2]
            drinks_list.append(Drinks(name, price, image))
    return drinks_list

drinks = read_drinks_from_file("Fooditems.txt")

# Sides Read File

def read_sides_from_file(file_name):
    sides_list = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist.")
        return sides_list

    with open(file_path, 'r') as file:
        for line in file:
          data = line.strip().split(', ')
          if len(data) >= 3:
            name = data[0]
            price = data[1]
            image = data[2]
            sides_list.append(Sides(name, price, image))
    return sides_list

sides = read_sides_from_file("Fooditems.txt")


# Extra toppings read file

def read_toppings_from_file(file_name):
    toppings_list = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist.")
        return toppings_list

    with open(file_path, 'r') as file:
        for line in file:
          data = line.strip().split(', ')
          if len(data) >= 2:
            name = data[0]
            price = data[1]
            toppings_list.append(SandwichToppings(name, price))
    return toppings_list
  
extra_toppings = read_toppings_from_file("Toppings.txt")