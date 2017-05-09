GPAdict = {'A+':90, 'A':85, 'A-':80, 'B+':76, 'B':72, 'B-':68, 'C+':64, 'C':60, 'C-':55, 'D':50, 'F':0}
GPAdict2 = {'81': 3.75, '61': 2.1, '79': 3.6, '74': 3.1, '73': 3.0, '66': 2.55, '60': 2.0, '90': 4.33, '87': 4.1, '57': 1.7, '58': 1.8, '59': 1.9, '65': 2.5, '63': 2.3, '69': 2.7, '80': 3.7, '84': 3.9, '78': 3.5, '64': 2.4, '50': 1.0, '62': 2.2, '76': 3.3, '72': 2.95, '70': 2.8, '75': 3.2, '82': 3.8, '53': 1.3, '83': 3.85, '88': 4.2, '51': 1.1, '54': 1.4, '77': 3.4, '52': 1.2, '86': 4.0, '89': 4.3, '55': 1.5, '71': 2.9, '67': 2.6, '68': 2.65, '56': 1.6, '85': 3.95}


def populate():
    file = open("gpa.txt", "r")
    f = file.read()
    f = f.upper() # account for lower case grades
    l = f.split()
    return l

def calcPerc(l):
    total = 0
    for i in l:
        total += GPAdict[i]
    res = total/len(l)
    res = round(res, 2) # round to two decimal
    return res

def calcGPA(gpa):
    gpa = str(round(gpa)) # round to int
    return GPAdict2[gpa]

l = populate() # read letter grades from file
print('Grades:', l) 
gpapercent = calcPerc(l) # get GPA percentage
gpa = calcGPA(gpapercent) # get GPA/4.33
print('GPA percent: {}{}'.format(gpapercent,'%'))
print('GPA: {}/4.33'.format(gpa))
