marks = [50, 55, 58]
threshold = 60
total = 0
count = 0

for mark in marks:
    total += mark

count = len(marks)

average = total / count

if average < threshold:
    print("Student is At Risk")
else:
    print("Student Performance is Good")
