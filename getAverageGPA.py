import pandas as pd


csv = pd.read_csv('CourseDatav3.csv')
courseKey = set(csv['Course'].tolist())
output = pd.DataFrame(columns=['Course','Year','GPA'])
tys = csv['Year'].tolist()

yearss = []
for ty in tys:
    t,y = ty.split()
    yearss.append(y)
    
csv['Y'] = yearss
for course in courseKey:
    c = csv[csv['Course']==course]
    years = set(c['Y'].tolist())
    years = list(years)
    years.sort()
    # print years
    for year in years:
        cy = c[(c['Y']==year) &(c['GPA']!=0)]
        if len(cy) == 0: continue
        gpaAverage  = sum(cy['GPA'].tolist())/float(len(cy))    
        row = [{'Course':course, 'Year':year, 'GPA':gpaAverage}]
        output = output.append(row)


output.to_csv('output3.csv',index=None)
