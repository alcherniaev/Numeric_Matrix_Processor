num = int(input())
lst_ = []
add = 0
for i in range(num + 1):
    a =+ (i - 1)
    lst_.append(('#' * (i + a)))

for i in lst_:
    print((i).center(len(lst_[-1])))
