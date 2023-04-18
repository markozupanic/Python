
PERSONAL_DATA_FILE_PATH = "personal_data.txt"

def read_file(number_of_rows):
    f = open(PERSONAL_DATA_FILE_PATH, "r")
    for _ in range(number_of_rows):
        print(f.readline())
    f.close()

def write_string_to_file(string_to_write):
    # f = open(PERSONAL_DATA_FILE_PATH, "a")
    with open(PERSONAL_DATA_FILE_PATH, "a") as f:
        f.write(string_to_write)
        f.write("\n")


def clear_file():
    # f = open(PERSONAL_DATA_FILE_PATH, "w")
    with open(PERSONAL_DATA_FILE_PATH, "w") as f:
        f.write("")


while True:
    option = input("1-read\n2-write\n3-clear\n")
    if option == "":
        break
    elif option == "1":
        number_of_rows = int(input("broj redaka: "))
        read_file(number_of_rows)

    elif option == "2":
        name = input("ime: ")
        age = input("godine: ")
        string_to_write = name + " | " + age
        write_string_to_file(string_to_write)

    elif option == "3":
        clear_file()