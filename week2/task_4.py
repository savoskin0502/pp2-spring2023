import collections

words = input().split()
results = collections.defaultdict(int)  # dict

for word in words:
    results[word] += 1

print(results)
