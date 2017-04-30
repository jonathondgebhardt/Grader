import re

def getGrade(filename):
    # Matches 5.5 / 5.5 & 5 / 5
    grade = "\d+\.?\d*\s/\s\d+\.?\d*"

    f1 = open(filename)
    gradesList = []

    # Read grades from file using "grade" regex
    for line in f1:
        if re.match(grade, line):
            gradesList.append(line[:len(line) - 1].split(" / "))

    # Split grades up into separate lists
    receivedPoints = []
    totalPoints = []
    gradeCount = 0

    for line in gradesList:
        receivedPoints.append(float(line[0]))
        totalPoints.append(float(line[1]))
        gradeCount = gradeCount + 1

    received = 0
    actual = 0

    # Total up grades
    for i in range(0, gradeCount):
        received = received + receivedPoints[i]
        actual = actual + totalPoints[i]

    # Print final grade
    # Print file name after last "\"

    slash = len(filename)

    # Get index of first char of file name
    for i in reversed(filename):
        if i == '\\':
            break
        slash = slash - 1

    # Print results associated with file name
    print(filename[slash:], "grade is:", received/actual * 100, "\n")

def main():
    consoleInput = " "
    while consoleInput != "":
        print("Enter file path and name (press Enter to quit): ")
        consoleInput = input()
        if consoleInput != "":
            getGrade(consoleInput)

    print("Goodbye")

main()
