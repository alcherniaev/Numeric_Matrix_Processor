# please work with the variable 'list_of_strings'

#input_nums = input()

for i in range(0, len(list_of_strings)):
    list_of_strings[i] = int(list_of_strings[i])

add_one = [x + 1 for x in list_of_strings]
print(add_one)

