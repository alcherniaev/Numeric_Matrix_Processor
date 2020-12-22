def rec_sum(n):
    if n == 0:
        return 0
    # write the insides here!
    return n + rec_sum(n - 1)
