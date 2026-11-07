from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv 
import os 

load_dotenv()


name = input("enter your name: ")
print("welcome", name)

admin_mod = input("do you want admin mod? yes/no: ")
if admin_mod == "yes":
    password = input("enter admin password : ")
    if password == os.getenv("admin_pass"):
        print("admin mod is on ")
    else:
        print("wrong password")
tasks = load_tasks()
how_many = int(input("how many task do you want to do ? : "))

for i in range(how_many):
    task_name = input("enter a task: ")
    priority = input("enter a priority (low,medium high) : ").lower()
    task = {
        "name": task_name,
        "priority": priority
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)
load_tasks()