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
    ClassTotalResult = 0

    for i in range(numStudents):
        StudentName=(input(f' What is the name of student {i+1} : '))
        StudentTotal=0
        for j in range(numAssessments):
            result = int(input(f'What did {StudentName} get out of {AssessmentValues[j]} in the {AssessmentNames[j]} : '))
            if result < 0:
                result = 0
            elif result > int(AssessmentValues[j]):
                result = int(AssessmentValues[j])

            StudentTotal=StudentTotal+result
            print(StudentTotal)

            if StudentTotal > topStudentResult:
                TopStudentName=StudentName
                TopStudentResult=StudentTotal

            ClassTotalResult=ClassTotalResult+StudentTotal

            j=j+1

    print(TopStudentName)
    print(TopStudentResult)
    print(ClassTotalResult)



main()
