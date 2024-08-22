#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

def calculateGrade(grade):
    #Calculate the grade based on the percentage
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

def get_positive_integer(prompt):
    #Function to get a positive integer input from the user
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Error: The number must be integer. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():

    #Main function to process assessments and students
    numAssessments = get_positive_integer("Enter number of Assessments: ")


    AssessmentNames = []
    AssessmentValues = []


    #Collect details for each assessment
    for i in range(numAssessments):
        AssessmentNames.append(input(f'Enter Assessment Name {i + 1} : '))
        AssessmentValues.append(get_positive_integer(f'Enter Assessment Value {i + 1} :'))

    #Check if the total of assessment values adds up to 100
    if sum(AssessmentValues) > 100:
        print('Error: Assessment values do not add up to 100')

    numStudents = get_positive_integer("\nHow many Students?: ")

    # Initialize variables to track top student and class totals
    TopStudentName = ""
    TopStudentNames=[]
    topStudentResult = 0
    ClassTotalResult = 0
    passCount=0

    # Collect results for each student
    for i in range(numStudents):
        StudentName = (input(f'\nWhat is the name of student {i + 1} : '))
        StudentTotal = 0
        for j in range(numAssessments):
            result = get_positive_integer(f'What did {StudentName} get out of {AssessmentValues[j]} in the {AssessmentNames[j]} : ')
            if result == "":
                result = 0
            else:
                result = int(result)

            if result < 0:
                result = 0
            elif result > int(AssessmentValues[j]):
                result = int(AssessmentValues[j])

            # Calculate the percentage for the assessment and the grade
            assessmentPresentage = result / AssessmentValues[j] * 100
            grade = calculateGrade(assessmentPresentage)

            print(f'{result} out of {AssessmentValues[j]} is a {grade}')
            StudentTotal = StudentTotal + result
            # Update the pass student count
        if grade != "Fail":
            passCount+=1



        grade = calculateGrade(StudentTotal)
        print(f'{StudentName} has a total number of: {StudentTotal} ({grade})')

        # Update top student details if current student has a higher total score
        if StudentTotal > topStudentResult:
            TopStudentName = StudentName
            topStudentResult = StudentTotal
        elif StudentTotal == topStudentResult:
            TopStudentNames.append(TopStudentName)

        ClassTotalResult = ClassTotalResult + StudentTotal

    # Display the results
    print('\nAll marks are entered!')
    classAverage = round(ClassTotalResult / numStudents)
    print(f'The class average is {classAverage}')
    print(f'The top student is {TopStudentName} with a total mark of {topStudentResult}')
    print(f'\nThe number of passed students is {passCount}')
    passPercentage = round((passCount / numStudents) * 100, 2)
    print(f'\nThe pass percentage is {passPercentage}%')
    print(f'\n Equal higher mark students are {TopStudentName} {TopStudentNames}')

main()
