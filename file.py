# with open("highscore.txt",mode="w") as uday:
#     uday.write("Uday sai manoj")
#
# with open("highscore.txt",mode="a") as uday:
#     uday.write("\n\nUday sai manoj")

with open("highscore.txt",mode="r") as uday:
    content=uday.read()
    content=int(content)
    print(type(content))



uday.close()