def sum(a, b):
    return a + b

if __name__ == '__main__':
    print('Input two numbers for adding.\nFirst number: ', end='')
    a = int(input())
    print('Second number: ', end='')
    b = int(input())
    print('Result =', sum(a, b))