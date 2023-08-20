total_push = 50
count = 0


while total_push >= 0:
    total_push -= 1
    count += 1
    if count == 10 or count == 20 or count == 30 or count == 40:
        answer = input(f'You did a total of {count} push-ups. Are you tired? '
                       f'Yes or No : ')
        if answer == 'Yes' or answer == 'Y':
            print(f'You did a total of {count} push-ups')
            break
        else:
            continue
    elif count == 50:
        print(f'Congratulations you did {count}! You made it.')
