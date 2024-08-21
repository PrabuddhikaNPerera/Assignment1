def calculateGrade(grade):
    if grade < 50:
        return "Fail"
    elif 50 <= grade < 60:
        return "Pass"
    elif 60 <= grade < 70:
        return "Credit"
    elif 70 <= grade < 80:
        return "Distinction"
    else:
        return "High Distinction"

def main():
    numAssessments = int(input("Enter number of Assessments: "))
#    print(numAssessments)
    AssessmentNames = []
    AssessmentValues = []

    for i in range(numAssessments):
        AssessmentNames.append(input(f'Enter Assessment Name {i+1} : '))
        AssessmentValues.append(int(input(f'Enter Assessment Value {i+1} :')))

    if sum(AssessmentValues) > 100:
        print('Error: Assessment values do not add up to 100')

 #   print (AssessmentNames)
 #   print (AssessmentValues)

    numStudents = int(input("\nHow many Students?: "))

    TopStudentName= ""
    topStudentResult= 0
    ClassTotalResult = 0

    for i in range(numStudents):
        StudentName=(input(f'\nWhat is the name of student {i+1} : '))
        StudentTotal=0
        for j in range(numAssessments):
            result = int(input(f'What did {StudentName} get out of {AssessmentValues[j]} in the {AssessmentNames[j]} : '))
            if result < 0:
                result = 0
            elif result > int(AssessmentValues[j]):
                result = int(AssessmentValues[j])

            assessmentPresentage= result/AssessmentValues[j]*100
            grade=calculateGrade(assessmentPresentage)
            print(f'{result} out of {AssessmentValues[j]} is a {grade}')

            StudentTotal=StudentTotal+result
        grade = calculateGrade(StudentTotal)
        print(f'{StudentName} has a total number of: {StudentTotal} ({grade})')


        if StudentTotal > topStudentResult:
            TopStudentName=StudentName
            TopStudentResult=StudentTotal

            ClassTotalResult=ClassTotalResult+StudentTotal

        j=j+1

    print ('All marks are entered!')
    classAverage = ClassTotalResult/numStudents
    print(f'The class average is {classAverage}')
    print(f'The top student is {TopStudentName} with a total mark of {TopStudentResult}')

main()
