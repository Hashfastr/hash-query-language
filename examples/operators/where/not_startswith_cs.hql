database('csv').http('student_habits_performance.csv')
| where parental_education_level !startswith_cs "Mas"
| summarize count() by parental_education_level
