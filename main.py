from tasks import task
import os
from dotenv import load_dotenv
load_dotenv()
theadmin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin_mode = input("would you like to open admin mode? yes/no:  ")

while True:
    if open_admin_mode.lower() == "yes":
        apple = input("pls enter the admin password: ")
        if apple == theadmin_password:
            print("you have joined admin mode")
            break
        else:
            print("oops wrong password")
            a = input("do you want to exit admin mode? yes/no: ")
            continue
    if a == "yes":
        print("ok you have left admin mode")
        break

    


name = input("hello may i know your name: ")
print("omg hi welcome", name)

for i in task:
    awnser_task = i["task"]

my_task = input(awnser_task)
print(f"{name} your task is {my_task}")


with open ("tasks.txt", "a") as task_awnser:
    task_awnser.write(f"{name} your task is {my_task}\n")