def get_todos(filepath='todos1.txt'):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath='todos1.txt'):
    with open(filepath,'w') as file_write:
        file_write.writelines(todos_arg)

if __name__ =='__main__':
    print(get_todos())
    