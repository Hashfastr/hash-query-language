let Females = database('csv').http('student_habits_performance.csv');
let Males = database('csv').http('student_habits_performance.csv');
Females
| project age, diet_quality
| summarize make_mv(diet_quality) by age
| project age, dq=len(diet_quality)