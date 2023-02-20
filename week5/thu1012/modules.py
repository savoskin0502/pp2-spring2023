# modules
# import chain_example
# import chain_example as ch
from chain_example import chain
import m1
import m2

import sys
# sys.path.append(
#     '/Users'
# )


def chain(*args):
    print('modules chain')
    return []


def main():
    pass


if __name__ == '__main__':
    main()
    print(sys.path)
    # print(list(chain_example.chain([7, 8], [9, 10])))
    # print(list(ch.chain([7, 8], [9, 10])))
    # print(list(chain([7, 8], [9, 10])))
    print(m1.x)
    print(m2.x)
