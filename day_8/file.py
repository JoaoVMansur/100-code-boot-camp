# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print("pedrao e feio")
#     print("pedrao e gay")
#     print("pedrao e guloso")

# greet()
#this is positional argument:
# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"how is like in {location}?")


#key word argument:
a = input("say your name: ")
b = input("where you are: ")

def greet_with_key(location=b, name=a):
    print(f"hello {name}")
    print(f"how is like in {location}")


greet_with_key()