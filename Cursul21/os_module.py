import os

if __name__ == '__main__':
    # print(os.getcwd())
    # print(os.listdir())
    # os.chdir(r"salut")
    # print(os.listdir())
    # with open("hello.txt", "r") as f:
    #     print(f.read())

    # os.mkdir("test")
    # os.makedirs('test/test3/test5')
    #
    # os.rmdir('test/test3/test5')
    # os.removedirs("test/test3")

    # print(os.stat("salut"))
    # print(os.stat("hello.txt"))
    # print(os.stat("sys_module.py"))

    for path, dir, files in os.walk('../'):
        print(path)
        print(dir)
        print(files)
        print()
