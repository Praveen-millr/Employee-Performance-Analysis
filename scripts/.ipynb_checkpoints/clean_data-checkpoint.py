import pandas as pd

# Load datasets
employees = pd.read_csv("data/employees.csv")
projects = pd.read_csv("data/projects.csv")
tasks = pd.read_csv("data/tasks.csv")

# 1️⃣ Clean Employees Data
employees.drop_duplicates(inplace=True)  # Remove duplicates
employees.dropna(inplace=True)  # Drop rows with missing values (optional)
employees.to_csv("data/cleaned_employees.csv", index=False)

# 2️⃣ Clean Projects Data
projects.drop_duplicates(inplace=True)  # Remove duplicates
projects.dropna(inplace=True)  # Drop rows with missing values (optional)
projects.to_csv("data/cleaned_projects.csv", index=False)

# 3️⃣ Clean Tasks Data
tasks.drop_duplicates(inplace=True)  # Remove duplicate tasks
tasks.fillna({"Time_Taken_Hours": 0}, inplace=True)  # Fill missing values
tasks["Completion_Date"] = pd.to_datetime(tasks["Completion_Date"])  # Format dates
tasks.to_csv("data/cleaned_tasks.csv", index=False)

print("Data Cleaning Completed for Employees, Projects, and Tasks!")
