import argparse
import os
import json
import pickle
import sys

# TODO List Command line application

# function that adds a todo to todo list
def add_todo(todo_list):
    todo = input("Enter a task: ")
    todo_list.append(todo)
    print("Todo has been added")

# function that lists todos
# 1: Go shopping
# 2:...
def list_todos(todo_list):
    print("\nTodo list:")
    for i, todo in enumerate(todo_list):
        print(f"{i+1}: {todo}")


# remove todo from the list
def remove_todo(todo_list):
    list_todos(todo_list)
    todo_number = int(input("Enter todo number to remove: "))
    todo_list.pop(todo_number - 1)
    print("Todo removed")


# mark a todo complete
# x Go shopping
def complete_todo(todo_list):
    list_todos(todo_list)
    todo_number = int(input("Enter todo number to complete: "))
    todo_list[todo_number - 1] = '✔ ' + todo_list[todo_number - 1]
    print("Todo completed")


# Show one todo
def show_todo(todo_list):
    list_todos(todo_list)
    todo_number = int(input("Enter todo number to show: "))
    print(todo_list[todo_number - 1])


# handling commandline arguments
def get_parser():
    parser = argparse.ArgumentParser(description="Todo Application")
    parser.add_argument('-a', '--add', help='Add a new todo', action='store_true')
    parser.add_argument('-l', '--list', help='List all todos', action='store_true')
    # add the rest of the commands

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    todo_list = []
    if os.path.exists('todos.json'):
        with open('todos.json') as f:
            todo_list = json.load(f)
    elif os.path.exists('todo.pickle'):
        with open('todo.pickle', 'rb') as f:
            todo_list = pickle.load(f)

    if args.add:
        add_todo(todo_list)
    elif args.list:
        list_todos(todo_list)
    # handle the rest
    else:
        parser.print_help()

    with open('todo.json', 'w') as f:
        json.dump(todo_list, f)

    with open('todo.pickle', 'wb') as f:
        pickle.dump(todo_list, f)



if __name__ == "__main__":
    main()


