name = input("hello may i know your name: ")
print("omg hi welcome", name)

from tasks import task

for i in task:
    awnser_task = i["task"]

my_task = input(awnser_task)
print(f"{name} your task is {my_task}")


