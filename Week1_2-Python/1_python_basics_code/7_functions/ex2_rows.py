# Write a python function that will take n as input and print the pattern
# of n rows. If the n is even, then print it flipped.
def three(n):
    # test if n is an odd or an even number

    # even number
    if n % 2 == 0:
        for i in range(n, 0, -1):
            for j in range(i):
                print('*', end=' ')
            print('')

    # odd number
    else:
        for i in range(n + 1):
            for j in range(i):
                print('*', end=' ')
            print('')


# call of the function
if __name__ == "__main__":
    n = 4
    three(n)
