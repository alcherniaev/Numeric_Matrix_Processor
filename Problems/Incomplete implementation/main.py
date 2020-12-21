def startswith_capital_counter(names):
    counter_ = 0
    for name in names:
        if name[0].isupper():
            counter_ += 1
    return counter_
