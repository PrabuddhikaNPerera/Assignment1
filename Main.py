def main():
    numAssessments = int(input("Enter number of Assessments: "))
    print(numAssessments)
    AssessmentNames = []
    AssessmentValues = []

    for i in range(numAssessments):
        AssessmentNames.append(input(f'Enter Assessment Name {i+1} : '))
        AssessmentValues.append(int(input(f'Enter Assessment Value {i+1} :')))

    print (AssessmentNames)
    print (AssessmentValues)

    numStudents = int(input("How many Students?: "))


main()
