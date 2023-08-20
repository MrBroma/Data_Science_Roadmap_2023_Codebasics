# Write a python function to check if any given number is a prime number and odd number?

# If given number is greater than 1

def prime_odd(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                if num % 2 == 0:
                    print(num, "is even and not a prime number")
                    break
                print(num, "is odd and not a prime number")
                break
        else:
            if num % 2 == 0:
                print(num, "is even and a prime number")
            print(num, "is odd and a prime number")
    else:
        print(num, "is not a prime number")

num = 97

prime_odd(num)

