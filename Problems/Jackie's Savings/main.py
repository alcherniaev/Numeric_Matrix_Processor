def final_deposit_amount(*interest, amount=1000):
    current_amount = amount
    for month_ in interest:
        current_amount = current_amount * ((month_ / 100) + 1)
    return round(current_amount, 2)


