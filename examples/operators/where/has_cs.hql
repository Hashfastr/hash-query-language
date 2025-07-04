database('csv').http('student_habits_performance.csv')
| where parental_education_level has "ste"
| summarize count() by parental_education_level
