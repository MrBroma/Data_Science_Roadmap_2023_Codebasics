data = {
    'Id_name': ['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History'],
    'Jennifer': ['58', '96', '78', '46', '96', '77', '83'],
    'Jessica': ['78', '55', '86', '63', '54', '89', '75'],
    'John': ['55', '45', '56', '87', '21', '52', '89'],
    'Ramesh': ['25', '54', '89', '76', '95', '87', '56'],
    'Suresh': ['75', '55', '', '64', '90', '61', '58']
}

# Get the names of the students and remove 'Id_name'
student_names = list(data.keys())
student_names.remove('Id_name')

# Calculate the total for each student
totals = {}
for student in student_names:
    scores = data[student]
    total = sum([int(score) for score in scores if score.isdigit()])
    totals[student] = total

print(totals)
