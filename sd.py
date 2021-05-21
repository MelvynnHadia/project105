import csv
with open('data.csv', newline= '') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

total_marks = 0
total_entries = len(data)
for marks in data:
    total_marks+=float(marks[1])

mean = total_marks//total_entries

print("Mean is "+str(mean))

number = mean
sqrt = number ** 0.5
print("Standard Deviation is ", sqrt)

