def range_sum(numbers, start, end):
    s = 0
    for x in numbers:
        if start <= x <= end:
            s += x
    return s


input_numbers = list(map(int, input().split()))
a, b = list(map(int, input().split()))
# input_numbers = [4, 5, 1, 3, 8]
# a = 4
# b = 6
print(range_sum(input_numbers, a, b))