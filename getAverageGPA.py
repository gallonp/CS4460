import pandas as pd


csv = pd.read_csv('CourseDatav3.csv')
courseKey = set(csv['Course'].tolist())
output = pd.DataFrame()
tys = csv['Year'].tolist()

# yearss = []
# for ty in tys:
#     t,y = ty.split()
#     yearss.append(y)
# csv['Y'] = yearss
newOutput = pd.DataFrame()
for course in courseKey:
    c = csv[csv['Course']==course]
    years = set(c['Year'].tolist())
    years = list(years)
    years.sort()
    # print years
    for year in years:
        cy = c[(c['Year']==year) &(c['GPA']!=0)]
        if len(cy) == 0: continue
        gpaAverage  = sum(cy['GPA'].tolist())/float(len(cy))
        Aaverage  = sum(cy['A'].tolist())/float(len(cy))
        Baverage  = sum(cy['B'].tolist())/float(len(cy))
        Caverage  = sum(cy['C'].tolist())/float(len(cy))
        Daverage  = sum(cy['D'].tolist())/float(len(cy))
        Faverage  = sum(cy['F'].tolist())/float(len(cy))
        Waverage  = sum(cy['W'].tolist())/float(len(cy))
        s,y = year.split()
        newOutput = newOutput.append(
            [{'Course':course, 
            'AverageGPA':gpaAverage,
            'A':Aaverage,
            'B':Baverage,
            'C':Caverage,
            'D':Daverage,
            'F':Faverage,
            'W':Waverage,
            'semester':s,
            'year':y}])
        # semesters = []   
        # for each in cy['Year'].tolist():
        #     s,y = each.split()
            # semesters.append(s)
        # cy['AverageGPA'] = gpaAverage
        # cy['Semester']  = semesters

        # print cy 
        # exit()
        # output= output.append(cy)
        # print output
        # exit()
        # for semester,semesterGPA in :
        #    output = output.append([{'Course':course, 'Year':year, 'AverageGPA':gpaAverage,'SemesterGPA':semesterGPA,"Semester":semester}])

# output['Year'] = output['Y']

newOutput.to_csv('output5.csv',index=None, columns=['Course','AverageGPA','A','B','C','D','F','W','semester','year'])
