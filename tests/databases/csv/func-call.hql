database('csv').file('./student_habits_performance.csv')
| where gender == "Female"
| project toint(age)
| take 10