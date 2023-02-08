
#Files
file_amazing = open("file_amazing.txt", "r+")
content = file_amazing.read()
print(content)
file_amazing.close()
file_astounding = open("file_astounding.txt", "w")
file_astounding.write("Heya cruel world ")
file_astounding.close()

Amazing = "C:\\Users\\Adriaan\\Desktop\\Amazing.txt"
file = open(Amazing, "r")
print(file.read())
