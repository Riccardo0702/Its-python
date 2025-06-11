PATH: str = "Lezione15/example.txt"
mode: str = "r"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)
message: str= "cacca"
output: str = file.write(message)
print(message)
file.close()