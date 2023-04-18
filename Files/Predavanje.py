FILE_PATH = "names.txt"

def write_string_to_file(string_to_write):
    f = open(FILE_PATH, "a")
    f.write(string_to_write)
    f.write("\n")
    f.close()

f = open(FILE_PATH, "r")
print(f.read())
print(type(f.readline()), end="")
print(f.readline())
print(type(f.readlines()))
print(f.read())