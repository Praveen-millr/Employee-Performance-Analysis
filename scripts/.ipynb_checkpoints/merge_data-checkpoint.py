import pandas as pd

# Load cleaned data
employees = pd.read_csv("data/cleaned_employees.csv")
projects = pd.read_csv("data/cleaned_projects.csv")
tasks = pd.read_csv("data/cleaned_tasks.csv")

# Merge data
df = tasks.merge(employees, on="Employee_ID")
df = df.merge(projects, on="Project_ID")

df.to_csv("data/merged_data.csv", index=False)
print("Merging Completed!")
