f = open('funny.txt', 'r')

for line in f:
    print(line, end=' ')

f.close()

with open('funny.txt', 'r') as f:
    for line in f:
        print(line, end=' ')

with open('funny.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

print(type(lines))

with open('love.txt', 'w') as f:
    f.write('I love Java\n')
    f.write('I love Javascript\n')
    f.write('I love C#\n')
    f.write('I love Python\n')

with open('love.txt', 'a') as f:
    f.write('I love Bash\n')

with open('love.txt', 'w') as f:
    f.writelines([
        "I love Fortran\n",
        "I love C++\n"
    ])

