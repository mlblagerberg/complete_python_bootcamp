"""Project: Errors and Exception Handling
Start: May 5th, 2024
Last touched: May 6th, 2024
Author: Madeleine L.
"""


# --------------------------------------- Error Types --------------------------------------- #
# # FileNotFound
# with open("test_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = { "key": "value"}
# value = a_dictionary["non_existent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Oranges", "Bananas"]
# fruit_list[3]
#
# # TypeError
# text = "abc"
# print(text + 5)

# --------------------------------------- Handling --------------------------------------- #
# Try: Something that might cause an exception
# Except: Do this if there was an exception
# Else: Do this if there were no exceptions
# Finally: Do this no matter what happens

# # FileNotFound & KeyError
# try:
#     file = open("test_file.txt")
#     b_dictionary = {"key": "value"}
#     print(b_dictionary["key"])
# except FileNotFoundError:
#     file = open("test_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("Testing whether file exists")
#     raise KeyError("This is an error that I made up")

height = float(input("Height (inches): "))
weight = int(input("Weight (lbs): "))

if height > 108:
    raise ValueError("Human height should not be over 9 feet")

bmi = 703*weight / height ** 2
print(bmi)

