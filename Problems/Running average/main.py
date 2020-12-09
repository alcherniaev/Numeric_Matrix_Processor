'''lst_ = [int(el) for el in input()]
lst_to_print = list()
for i in range(1, len(lst_)):
    lst_to_print.append((lst_[i] + lst_[i - 1]) / 2)

print(lst_to_print)'''


print([(int(i) + int(i) + 1) / 2 for i in input()[:-1]])
