import pandas as pd


csv = pd.read_csv('cs_data_year.csv')
courseKey = set(csv['Course'].tolist())
output = pd.DataFrame(columns=['Course','Year','GPA'])
for course in courseKey:
    c = csv[csv['Course']==course]
    years = set(csv['Year'].tolist())
    for year in years:
        cy = c[(c['Year']==year) &(c['GPA']!=0)]
        if len(cy) == 0: continue
        gpaAverage  = sum(cy['GPA'].tolist())/float(len(cy))    
        row = [{'Course':course, 'Year':year, 'GPA':gpaAverage}]
        output = output.append(row)


output.to_csv('output.csv',index=None)
