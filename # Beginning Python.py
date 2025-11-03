# Beginning Python 
# Created by Ryan Saelens

# # Comments --> Use Hashtags

# Variables (Underscore Method)

my_name = "Ryan"

fav_food = "Pizza"

fav_color = "Green"

fav_heroes = ["Spider-Man", "Dr. Manhattan", "Mr. Fantastic"]

fav_num = 9

# # -----------------------------------------------------------------------------------------------------------

# # Variables (CamelCase Method)

myName = "Ryan"

favFood = "Pizza"

FavColor = "Green"

FAVHEROES = ["Spider-Man", "Dr. Manhattan", "Mr. Fantastic"]

favNumber = 9

favNumber1 = "Nine"

# -------------------------------------------------------------------------------------------------------------

# Lists

food = ["Pizza", "Cheetos", "Milk", "Dark Choclate"]

print(food)

food.append("Soda") # Append adds an item to the end of the list


print(food) # prints whatever is inside ()

# Math
num1 = 3
num2 = 4
result = num1 + num2
result = num1 / num2

# For-Loop

for item in food: # This is going to loop through and print each item in the food list above
    print(item)


# Conditional Statement --> If-Else
if num1 < 6:
    print("This number is less than 6")
else:
    print("Not less than 6")