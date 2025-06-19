let Females = database('csv').http('student_habits_performance.csv')
| where gender == "Female"
;
let Males = database('csv').http('student_habits_performance.csv')
| where gender == "Male"
;
Females
| join kind=anti Males on age
| project student_id, tostring(age), diet_quality
| take 10