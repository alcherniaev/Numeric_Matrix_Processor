a = input()

running_total = []

total = 0
for n in a:
    total += int(n)
    running_total.append(total)
print(running_total)
