def average_mark(*lst_):
    sum = 0
    for i in lst_:
        sum += i
    output = round(sum / len(lst_), 1)
    return output
