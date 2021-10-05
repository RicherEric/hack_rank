'''
n = 5
print string: 12345
'''


if __name__ == '__main__':
    n = int(input())
    print(''.join([str(num) for num in list(range(1,n+1))]))