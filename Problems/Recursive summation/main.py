def rec_sum(n):
    # write the insides here!
    if n == 0:
        return 0
    return n + rec_sum(n - 1)

# print(rec_sum(1))