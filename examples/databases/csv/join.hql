let Females = database('csv').http('student_habits_performance.csv')
| where gender == "Female"
;
let Males = database('csv').http('student_habits_performance.csv')
| where gender == "Male"
;
Females
| join Males on age
| project age, diet_quality
| summarize dq=make_list(diet_quality) by age
| take 10