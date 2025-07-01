database('csv').http('student_habits_performance.csv')
| where age <= 23
| summarize count() by age
