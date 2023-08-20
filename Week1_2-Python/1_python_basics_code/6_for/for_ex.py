# # 1. Write a Python program to print the following pattern.
# #
# # 1 2 3 4 5
# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1


for i in range(5, 0, -1):
    for i in range(i):
        print(i + 1, end=' ')
    print('')

# # 2. Write a Python program to find the sum of all the numbers except odd
# # numbers between 1 and 20 using a loop. Can you also do this using a while
# # loop?

n = 0
for i in range(1, 21):
     if i % 2 == 0:
         n += i
print(n)

a = 20
add = 0
while a >= 0:
    if a % 2 == 0:
        add += a
    a -= 1
print(add)


# 3. After throwing the dice several times, you got this result.
dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
# Using a for loop find out the followings:
# How many times have you got 6s
# How many times have you got 1s
# How many times have you got 6s two times in a row
n = 0
for i in dice_result:
    if i == 6:
        n += 1
print(n)

n = 0
for i in dice_result:
    if i == 1:
        n += 1
print(n)

###########################################
wo_6s = 0
l = len(dice_result)

for i in range(l - 1):
    if dice_result[i] == 6 and dice_result[i + 1] == 6:
        two_6s += 1

print(two_6s)

