# #FileNotFound 

# try:

#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("something")

# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")

# else:

#     content = file.read()
#     print(content)

# finally:

#     raise TypeError("This is an error that i made up")


height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Humans Height should not be over 3 meter")

bmi = weight/ height**2
print(bmi)





