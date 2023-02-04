def mini_max_sum(iterable):
    iterable = sorted(iterable)
    return sum(iterable[:4]), sum(iterable[-4:])


min_sum, max_sum = mini_max_sum([1,3,5,7,9])

print(f"Minimum sum is {min_sum}\nMaximum sum is {max_sum}")
