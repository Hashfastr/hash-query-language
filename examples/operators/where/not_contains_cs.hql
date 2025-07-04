database('csv').http('student_habits_performance.csv')
| where parental_education_level !contains_cs "ste"
| summarize count() by parental_education_level
