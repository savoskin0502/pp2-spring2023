# 1 2 3 4 5
numbers = set(input().split())


while True:
    command, *args = input().split()

    if command == 'stop':
        break
    elif command == 'pop':
        if len(numbers):
            deleted_number = numbers.pop()
            print(f'{deleted_number} deleted.')
        else:
            print("there's no elements in `numbers`")
    elif command == 'remove':
        if len(args):
            variable_to_delete = args[0]
            if variable_to_delete in numbers:
                numbers.remove(variable_to_delete)
            else:
                print("there's no such variable in `numbers`")
        else:
            print("there's no arguments")
    elif command == 'discard':
        variable_to_delete = args[0]
        numbers.discard(variable_to_delete)
    elif command == 'print':
        print(numbers)
    else:
        print("i don't know that command")
