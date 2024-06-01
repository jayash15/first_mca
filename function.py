def get_todos(filepath="todo.txt"): # =filename will be by default argument where ever we call the function if we dont pass argument
    ''' open file in read mode for show ''' # these are document string

    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos #it will return values store in todos


def write_todos(todos,filepath="todo.txt"):
    ''' open file in write mode for edit and delete'''
    with open('todo.txt', 'w') as file:
        file.writelines(todos)

print(__name__) #for testing purpose
if __name__=="__main__":  # with this both these print will not execute in main function and it will match both files

    print(help(get_todos))
    print("hello")

