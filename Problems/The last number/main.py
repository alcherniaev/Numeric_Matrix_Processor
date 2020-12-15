# use this tuple
numbers = tuple(int(n) for n in input().split())


def lst_item(any_tuple):
    print(any_tuple[-1])


lst_item(numbers)
