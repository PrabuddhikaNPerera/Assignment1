def main():
    numAssessments = int(input("Enter number of Assessments: "))
    print(numAssessments)
    AssessmentNames = []
    AssessmentValues = []

    for i in range(numAssessments):
        AssessmentNames.append(input(f'Enter Assessment Name {i+1} : '))
        AssessmentValues.append(int(input(f'Enter Assessment Value {i+1} :')))

    if sum(AssessmentValues) > 100:
        print('Error: Assessment values do not add up to 100')

    print (AssessmentNames)
    print (AssessmentValues)

    numStudents = int(input("How many Students?: "))

    TopStudentName= "test"
    topStudentResult= 0
    TotalResult = 0

    for i in range(numStudents):
        StudentName=(input(f' What is the name of student {i+1} : '))
        for j in range(numAssessments):
            result = input(f'What did {StudentName} get out of {AssessmentValues[i]} in the {AssessmentNames[i]} : ')




main()
