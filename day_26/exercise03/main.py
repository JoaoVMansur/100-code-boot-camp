with open("day 26/exercise03/file1.txt") as file1:

    file_1_data = file1.readlines()


with open("day 26/exercise03/file2.txt") as file2:

    file_2_data = file2.readlines()


result = [int(num) for num in file_1_data if num in file_2_data]

print(result)