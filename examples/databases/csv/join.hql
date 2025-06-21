let CSV = database('csv').http('student_habits_performance.csv');
CSV
| summarize bincount(diet_quality) by gender, age
| struct 
| project gender, age, dq