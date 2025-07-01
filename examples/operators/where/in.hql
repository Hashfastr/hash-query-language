database('csv').http('student_habits_performance.csv')
| where age in (23, 22, 21)
| summarize count() by age
