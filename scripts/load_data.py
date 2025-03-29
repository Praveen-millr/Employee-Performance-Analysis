import pandas as pd

# Load datasets
employees = pd.read_csv("data/employees.csv")
projects = pd.read_csv("data/projects.csv")
tasks = pd.read_csv("data/tasks.csv")

# Display first few rows
print("Employees Data:\n", employees.head())
print("\nProjects Data:\n", projects.head())
print("\nTasks Data:\n", tasks.head())
