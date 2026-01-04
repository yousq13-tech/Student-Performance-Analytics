marks = [50, 55, 58]  
threshold = 60
total = 0
count = 0

if len(marks) == 0:
    print("No marks available to calculate average.")
else:
    for mark in marks:
        total += mark
        count += 1

    average = total / count

    if average < threshold:
        print("Student is At Risk")
    else:
        print("Student Performance is Good")
