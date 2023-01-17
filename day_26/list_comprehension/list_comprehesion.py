#list comprehension with other list

numbers =  [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)


#list comprehension with strings

name = "Angela"
name_list = [n for n in name]
print(name_list)

#list comprehension with ranges

double_range = [n*2 for n in range(1, 5)]
print(double_range)

#list comprehension with conditional 

names = ["Alex", "John", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(uppercase_names)