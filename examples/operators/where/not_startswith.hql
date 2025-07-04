database('csv').http('student_habits_performance.csv')
| where parental_education_level !startswith "mas"
| summarize count() by parental_education_level
