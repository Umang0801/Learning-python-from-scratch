to_do_list = []

def show_tasks():
    if len(to_do_list) == 0:
        print('No tasks in the to-do list.')
    else:
        for i, task in enumerate(to_do_list, start=1):
            print(f'{i}. {task}')

while True:
    print('Options: (1) Add task (2) View tasks (3) Delete task (4) Quit')
    choice = input('Choose an option: ').strip().lower()

    if choice == '1' or choice == 'one' or choice == 'add task':
        task = input('Enter a new task: ')
        to_do_list.append(task)
        print(f'"{task}" added to the list.')
    
    elif choice == '2' or choice == 'two' or choice == 'view tasks':
        print('Your To-Do List:')
        show_tasks()

    elif choice == '3' or choice == 'three' or choice == 'delete task':
        show_tasks()
        if len(to_do_list) > 0:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(to_do_list):
                removed_task = to_do_list[task_num - 1]  
                del to_do_list[task_num - 1] 
                print(f'"{removed_task}" removed from the list.')
            else:
                print("Invalid task number.")
    
    elif choice == "4" or choice == 'four' or choice == 'quit':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
