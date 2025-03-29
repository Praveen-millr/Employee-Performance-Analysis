import pandas as pd
import matplotlib.pyplot as plt

# Load data
employee_performance = pd.read_csv("results/employee_performance.csv")
project_performance = pd.read_csv("results/project_performance.csv")
team_performance = pd.read_csv("results/team_performance.csv")

# Save Employee Performance Chart
plt.figure(figsize=(10, 5))
plt.bar(employee_performance["Employee_ID"], employee_performance["Total_Tasks"], color='skyblue')
plt.xlabel("Employee ID")
plt.ylabel("Total Tasks Completed")
plt.title("Employee Performance")
plt.xticks(rotation=90)
plt.savefig("results/employee_performance.png")  # Saves the chart
plt.close()

# Save Project Performance Chart
plt.figure(figsize=(10, 5))
plt.bar(project_performance["Project_ID"], project_performance["Total_Tasks"], color='orange')
plt.xlabel("Project ID")
plt.ylabel("Total Tasks Assigned")
plt.title("Project Performance")
plt.xticks(rotation=45)
plt.savefig("results/project_performance.png")  # Saves the chart
plt.close()

# Save Team Performance Chart
plt.figure(figsize=(10, 5))
plt.bar(team_performance["Team"], team_performance["Total_Tasks"], color='green')
plt.xlabel("Team Name")
plt.ylabel("Total Tasks Completed")
plt.title("Team Performance")
plt.xticks(rotation=45)
plt.savefig("results/team_performance.png")  # Saves the chart
plt.close()

print("Charts saved in the 'results' folder!")
