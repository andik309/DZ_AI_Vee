def calc_avg(lst):
    return sum(lst)/len(lst)
    
import pandas as pd

data = pd.read_csv(
    "school_progress.csv",
    index_col="enrollment_id"
)

students = data.drop_duplicates("student_id", keep="first")[["student_id", "student_name", "grade", "class_letter", "city"]]

enrollments = data[["student_id", "course", "level", "status", "average_score", "hours_spent", "attempts"]]

merged = enrollments.merge(
    students,
    on="student_id",
    how="left",
)

print(
    merged,
    f"число строк после объединения не изменилось: {len(enrollments)==len(merged)}",
    sep='\n'
)