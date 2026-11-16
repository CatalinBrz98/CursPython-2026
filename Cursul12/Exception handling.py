from Recapitulare.Jocuri_carti import war_manager

def read_float():
    while True:
        try:
            number = float(input("Enter a number: "))
            print(1/number)
            return number
        except ValueError:
            print("The input is not a number. Please try again.")

if __name__ == "__main__":
    # nr = read_float()
    # print(nr)
    print(war_manager())
