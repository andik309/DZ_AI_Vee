def calc_avg(lst):
    return sum(lst)/len(lst)
    
import pandas as pd

data = pd.read_csv(
    "school_progress.csv",
    index_col="enrollment_id"
)

data["start_date"] = pd.to_datetime(data["start_date"])
data["end_date"] = pd.to_datetime(data["end_date"])

data["start_month"] = data["start_date"].dt.month
data["start_weekday"] = data["start_date"].dt.dayofweek 
data["course_duration_days"] = data["end_date"] - data["start_date"]

average_score_groupedby_start_month = data.groupby("start_month")["average_score"].mean()
average_hours_spent_of_ended_courses = data[data["status"] == "completed"]["hours_spent"].mean()

print(
    average_score_groupedby_start_month,
    average_hours_spent_of_ended_courses,
    "потому-что это значения которые она сама должна спрогнозировать",
    sep='\n',
)