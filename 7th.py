def calc_avg(lst):
    return sum(lst)/len(lst)
    
import pandas as pd

data = pd.read_csv(
    "school_progress.csv",
    index_col="enrollment_id"
)

data["average_score"] = data["average_score"].fillna(0)

grouped_by_agg = data.groupby(["course"]).agg(
    records = ("student_id", "count"),
    students = ("student_name", "nunique"),
    mean_score = ("average_score", calc_avg),
    mean_hours =  ("hours_spent", calc_avg),
    mean_attempts =  ("attempts", calc_avg),
    
)

grouped_by_agg = grouped_by_agg.sort_values("mean_score", ascending=False)
# LSP говорит что нету перегрузки sort_values для таких аргументов, но всё работает

print(grouped_by_agg[:3])

statuses = data.groupby(data["course"])["status"].value_counts()



