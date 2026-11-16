if __name__ == "__main__":
    # with open("input.txt", "r") as f:
    #     for line in f:
    #         print(line, end="")
    # with open("output.txt", "a") as g:
    #     g.write("Salut!\n")

    with open("imagine.png", "rb") as f:
        content = f.read()

        for octet in content:
            print(octet)

        # with open("imagine_copy.png", "ab") as g:
        #     g.write(content)

    # text = "Salut!"
    # binar = text.encode()
    # print(text, type(text))
    # print(binar, type(binar))


