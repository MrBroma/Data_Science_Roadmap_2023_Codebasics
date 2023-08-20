total_push = 50
count = 0


while total_push >= 0:
    total_push -= 1
    count += 1
    if count == 10 or count == 20 or count == 30 or count == 40:
        answer = input('Are you tired? Yes or No : ')
        if answer == 'Yes' or 'Y':
            print(f'You did a total of {count} push-ups')
            break
        else:
            continue
    elif count == 50:
        print(f'Congratulations! You made it.')
