programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}
# Retriving a items from dictionary
print(programming_dictionary["Bug"])

# Adding  new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creat a empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}

# Edit a item in a dictionary
programming_dictionary["Bug"] = "A moth  in your computer"

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
# Nesting a list into a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttugart"],
}
# Nesting a dictionary into a dictionary
travel_log2 = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 12},
    "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttugart"], "Total_visits": 5},
}
# Nesting a dictionary into a List
travel_log3 = [
    {"Country": "France", 
    "Cities_visited": ["Paris", "Lille", "Dijon"],
     "Total_visits": 12
     },
    {"Country": "Germany",
     "Cities_visited": ["Berlin", "Hamburg", "Stuttugart"], 
    "Total_visits": 5
    },
]