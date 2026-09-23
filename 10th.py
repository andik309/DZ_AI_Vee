def calc_avg(lst):
    return sum(lst)/len(lst)
    
import pandas as pd

data = pd.read_csv(
    "school_progress.csv",
    index_col="enrollment_id"
)

pivot_table = data.pivot_table(
    index="student_id",
    columns="course",
    values="average_score",
    aggfunc="mean"
)

courses_count_for_each_student = pivot_table.transpose().count()
students_with_more_than_3_courses = courses_count_for_each_student[courses_count_for_each_student >= 3]

print(
    pivot_table[:10],
    students_with_more_than_3_courses,
    sep='\n'
)