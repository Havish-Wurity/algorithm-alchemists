def average_passing_grades(grades):
    passing_grades = [grade for grade in grades if grade >= 50]
    
    if len(passing_grades) == 0:
        return 0   
    
    return sum(passing_grades) / len(passing_grades)
