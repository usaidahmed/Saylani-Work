todo_list = []
flag = True
while flag:
    user_input = int(input("kindly enter 1 to enter a task in your todo_list\nkindly enter 2 to delete a task from your todo_list\nkindly enter 3 to close your todo_list"))
    if user_input == 1:
        append_stuff = input("kindly enter the task you want to insert")
        print(todo_list)
        todo_list.append(append_stuff)
    elif user_input == 2:
        delete_value = input("kindly enter the task you want to delete")
        todo_list.remove(delete_value)
        print(todo_list)
    elif user_input == 3:
        flag = False
    else:
        print("you enter wrong value ")
