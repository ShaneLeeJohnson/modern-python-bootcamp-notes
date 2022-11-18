# w - writes and erases existing contents
# with open("haiku.txt", "w") as file:
# 	file.write("Here's one more haiku\n")
# 	file.write("What about the other one?\n")
# 	file.write("Let's go check it out")

# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR
# with open("haiku.txt", "a") as file:
# 	file.seek(0)
# 	file.write(":)\n")

# r+ will overwrite whatever content exists at its position for each character being written
# with open("haiku.txt", "r+") as file:
# 	file.write(":)")
# 	file.seek(10)
# 	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "r+") as file:
	file.write("HELLO!!!")