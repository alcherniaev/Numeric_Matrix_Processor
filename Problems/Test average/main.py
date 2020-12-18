def average_mark(*lst_):
    sum_ = 0
    for i in lst_:
        sum_ += i
    return round(sum_ / len(lst_), 1)
