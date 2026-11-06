import sys

if __name__ == '__main__':
    # with open("output.txt", "w") as sys.stdout:
    # print(dir(sys))
    print(sys.version)
    print(sys.implementation)
    print(sys.platform)
    print(sys.path)
    val = 1
    print(sys.getsizeof(val))
    print(sys.argv)