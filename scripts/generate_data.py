import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker for realistic names
fake = Faker()
np.random.seed(42)

# Define teams and roles
teams_roles = {
    "Dev": ["Software Engineer", "Backend Developer", "Frontend Developer"],
    "QA": ["QA Engineer", "Test Analyst", "Automation Engineer"],
    "Design": ["UI Designer", "UX Designer", "Graphic Designer"],
    "Management": ["Project Manager", "Scrum Master", "Product Owner"],
    "Admin": ["System Admin", "HR", "Office Manager"],
    "Data": ["Data Analyst", "Data Engineer", "ML Engineer"]
}

# Define projects
projects = ["Sopheon", "Revold World", "Planted", "SRMG", "NBC"]

# Generate Employee Data
employees = []
for i in range(1, 201):  # 200 employees
    team = random.choice(list(teams_roles.keys()))
    role = random.choice(teams_roles[team])
    employees.append([i, fake.name(), team, role])

employees_df = pd.DataFrame(employees, columns=["Employee_ID", "Name", "Team", "Role"])

# Generate Project Data
projects_df = pd.DataFrame({
    "Project_ID": range(1, len(projects) + 1),
    "Project_Name": projects,
    "Client": [fake.company() for _ in range(len(projects))]
})

# Generate Task Data
tasks = []
for i in range(1, 5001):  # 5000 tasks
    emp_id = random.randint(1, 200)
    project_id = random.randint(1, len(projects))
    task_desc = random.choice([
        "Feature Development", "Bug Fixing", "Testing", "Design Review",
        "Database Optimization", "Security Patching", "Performance Testing",
        "UI Enhancement", "Code Review", "Meeting"
    ])
    time_taken = random.randint(1, 12)  # Random work hours per task
    completion_date = fake.date_this_year()

    tasks.append([i, emp_id, project_id, task_desc, time_taken, completion_date])

tasks_df = pd.DataFrame(tasks, columns=["Task_ID", "Employee_ID", "Project_ID", "Task", "Time_Taken_Hours", "Completion_Date"])

# Save to CSV
employees_df.to_csv("data/employees.csv", index=False)
projects_df.to_csv("data/projects.csv", index=False)
tasks_df.to_csv("data/tasks.csv", index=False)

print("Realistic Sample Data Generated!")
