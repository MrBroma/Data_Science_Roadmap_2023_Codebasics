import pprint
import csv


d = {}
with open('student_marks.csv', 'r') as f:
    for line in f:
        each_line = line.rstrip("\n").split(',')
        name = each_line[0]
        values = each_line[3:]
        d[name] = values

backup_line = d['']
del d['']
student_dict = dict()
student_dict['Id_name'] = backup_line
student_dict.update(d)
student_dict['Id_name'].append('Total')
student_dict['Id_name'].append('Average')

pprint.pprint(student_dict)

# Calculate the total for each student and add it as the last value in the list
for student in student_dict.keys():
    if student != 'Id_name':
        scores = student_dict[student]
        numeric_scores = [int(score) if score.isdigit() else 0 for score in scores]
        total = sum(numeric_scores)
        average = total / len(numeric_scores)
        scores.append(str(total))  # Convert the total to a string and add it to the list
        scores.append(str(average))  # Convert the average to a string and add it to the list

pprint.pprint(student_dict)


# Specify the output CSV file name
csv_filename = 'student_marks_updated.csv'

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row with 'Id_name' as the first element
    header_row = ['Id_name'] + student_dict['Id_name']
    csv_writer.writerow(header_row)

    # Write the data for each student
    for student in student_dict.keys():
        if student != 'Id_name':
            csv_writer.writerow([student] + student_dict[student])

print(f"CSV file '{csv_filename}' has been created.")