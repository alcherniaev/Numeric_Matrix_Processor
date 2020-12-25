import math

first_n = math.fabs(int(input()))
second_n = int(input())
if second_n in [0, 1] or second_n < 0:
    print(round(math.log(first_n), 2))
else:
    print(round(math.log(first_n, second_n), 2))
