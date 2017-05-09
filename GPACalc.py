def populate():
    file = open("gpa.txt", "r")
    f = file.read()
    f = f.upper()
    l = f.split()
    return l

def calcGPA(l):
    GPAdict = {'A+':90, 'A':85, 'A-':80, 'B+':76, 'B':72, 'B-':68, 'C+':64, 'C':60, 'C-':55, 'D':50, 'F':0}
    total = 0
    for i in l:
        total += GPAdict[i]
    return total/len(l)

l = populate()
print('Grades: ', l)
print('GPA: ', round(calcGPA(l), 2),'%')



