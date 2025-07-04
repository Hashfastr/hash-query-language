database('csv').http('student_habits_performance.csv')
| where parental_education_level has "STE"
| summarize count() by parental_education_level
