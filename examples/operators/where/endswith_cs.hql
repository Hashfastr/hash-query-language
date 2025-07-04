database('csv').http('student_habits_performance.csv')
| where parental_education_level endswith_cs "ter"
| summarize count() by parental_education_level
