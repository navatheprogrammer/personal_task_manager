from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os 




name = input(" hello may i know your name pls: ")
print("welcome to my project  ", name)
admin = input("do you want to enter adin mode? yes/no: ")
if admin == "yes":
    password = input("enter admin password: ")
    if password == os.getenv("admin_password"):
        print("admin mode has been activated")
    else:
        print("oops! wrong password")




tasks = load_tasks()
count = int(input("how many tasks do you want to add?: "))

for i in range(count):
    task = input("enter a task pls: ")
    tasks.append(task)


show_tasks(tasks)
save_tasks(tasks)