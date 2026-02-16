def average_passing_grades(grades):
    passing_grades = [grade for grade in grades if grade >= 50]
    
    if len(passing_grades) == 0:
        return 0   
    
    return sum(passing_grades) / len(passing_grades)
students=int(input('Enter the number of students:'))
l=[]
for x in range(students):
    x=int(input('Enter the grade:'))
    l.append(x)
print('The average of grades:',average_passing_grades(l)) 
    
