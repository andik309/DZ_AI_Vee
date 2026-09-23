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

ml_data = data[["grade", "course", "level", "lessons_completed", "total_lessons", "hours_spent", "attempts", "start_month", "start_weekday", "average_score"]]

ml_data = ml_data[ml_data["average_score"].notna()]
# LSP говорит что не может получить notna, но всё работает

print(
    ml_data.shape,
    ml_data.dtypes,
    # LSP говорит что не может получить dtypes, но всё работает
    f"Пропусков: { ml_data.isna().sum().sum() }",
    f"Пропусков в average_score: { ml_data["average_score"].isna().sum() }",
    # LSP говорит что не может получить isna, но всё работает
    ml_data[:5],
    sep='\n',
)

data.to_csv("ml_data.csv", index=False)


# LSP которая мне ложно говорит что нету isna, dtypes, notna и остальных, тратит гигабайт моей памяти, при этом она ещё работает через Node.js