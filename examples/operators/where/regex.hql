database('csv').http('student_habits_performance.csv')
| where parental_education_level matches regex ".a.t.r"
| summarize count() by parental_education_level
