database('csv').http('student_habits_performance.csv')
| where gender == "Female"
| project student_id, tostring(age), diet_quality
| take 10