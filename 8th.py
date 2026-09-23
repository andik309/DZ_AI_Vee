def calc_avg(lst):
    return sum(lst)/len(lst)
    
import pandas as pd

data = pd.read_csv(
    "school_progress.csv",
    index_col="enrollment_id"
)

grouped_by_agg = data.groupby(["course", "level"]).agg(
    records = ("student_id", "count"),
    avg_average_score = ("average_score", calc_avg),
    avg_hours_spent = ("hours_spent", calc_avg)
)

grouped_by_agg = grouped_by_agg[grouped_by_agg["records"] >= 5]

best_course_level = grouped_by_agg.sort_values("avg_average_score", ascending=False)[:5]
# LSP говорит что нету перегрузки sort_values для таких аргументов, но всё работает

print(
    best_course_level
)