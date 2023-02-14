# module_examples -> __main__
import sys

import list_generation
# import module1
from module1 import x
import module2 as m2


if __name__ == '__main__':
    print(x)
    # sys.path.append(
    #     '/Users/'
    # )
    # print(sys.path)

    s = list_generation.simple_generator(n=5)
    # for i in s:
    #     print(i)
