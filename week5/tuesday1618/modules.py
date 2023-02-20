# modules

# import chain_example
import chain_example as ch
# from chain_example import chain


def chain():
    return 1


array1 = [1, 2]
array2 = [3, 4]
for i in ch.chain(array1, array2):
    print(i)
