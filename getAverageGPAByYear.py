import pandas as pd


csv = pd.read_csv('CourseDatav2.csv')
courseKey = set(csv['Course'].tolist())
output = pd.DataFrame()
sys = csv['Year'].tolist()

yearss = []
smst = []
for sy in sys:
    s,y = sy.split()
    smst.append(s)
    yearss.append(y)

csv['Y'] = yearss
csv['Semester'] = smst
newOutput = pd.DataFrame()
for course in courseKey:
    c = csv[csv['Course']==course]
    years = set(c['Y'].tolist())
    years = list(years)
    years.sort()

    for year in years:
        cy = c[(c['Y']==year) &(c['GPA']!=0)]
        if len(cy) == 0: continue
        gpaAverage  = sum(cy['GPA'].tolist())/float(len(cy))
        # s,y = year.split()
        newOutput = newOutput.append([{'Course':course, 'Year':y, 'GPA':gpaAverage}])
 
newOutput.to_csv('output7.csv',index=None)
