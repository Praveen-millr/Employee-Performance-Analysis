import pandas as pd

df = pd.read_csv("data/merged_data.csv")

# Employee Performance
employee_performance = df.groupby("Employee_ID").agg(
    Total_Tasks=("Task", "count"),
    Avg_Time_Per_Task=("Time_Taken_Hours", "mean"),
    Total_Hours_Worked=("Time_Taken_Hours", "sum")
).reset_index()

# Project Performance
project_performance = df.groupby("Project_ID").agg(
    Total_Tasks=("Task", "count"),
    Total_Hours_Worked=("Time_Taken_Hours", "sum")
).reset_index()

# Team Performance
team_performance = df.groupby("Team").agg(
    Total_Tasks=("Task", "count"),
    Total_Hours_Worked=("Time_Taken_Hours", "sum")
).reset_index()

employee_performance.to_csv("results/employee_performance.csv", index=False)
project_performance.to_csv("results/project_performance.csv", index=False)
team_performance.to_csv("results/team_performance.csv", index=False)

print("Performance Metrics Calculated!")
