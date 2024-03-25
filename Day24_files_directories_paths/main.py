"""Project: Working with files
Start: March 20th, 2024
Last touched: March 20th, 2024
Author: Madeleine L.
"""

import os
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("my_file.txt", mode="a") as file:  # "a" stands for append, "w" would overwrite everything in file. Default
#     # mode is to "r" read.
#     file.write("This is my random addition.")

# TODO: For each name in names.txt replace the [name] in the started letter and save letter to output directory
# Extract names into list to loop over later
names_list = []
with open(os.path.expanduser(
        "~/GitHub/complete_python_bootcamp/Day24_files_directories_paths/Input/Addressee/names.txt")) as names:
    for name in names.readlines():
        # print(name.strip())  # strip removes new line \n from end of each name
        names_list.append(name.strip())

# print(names_list)

# Store letter as string and then replace [name] with names. Saving strings to unique objects
with open(os.path.expanduser(
        "~/GitHub/complete_python_bootcamp/Day24_files_directories_paths/Input/Letters/starting_letter.txt"), mode="r"
) as input_letter:
    input_content = input_letter.read()
    for name in names_list:
        separated_name = name.split()
        file_name = ""
        for i in separated_name:
            file_name += f"{i}_"
        file_name += f"final_letter.txt"

        output_content = input_content.replace("[name]", f"{name}")
        with open(os.path.expanduser(f"~/GitHub/complete_python_bootcamp/Day24_files_directories_paths/Output/"
                                     f"{file_name}"), mode="w") as output_letter:
            output_letter.write(output_content)
        # print(file_name)


