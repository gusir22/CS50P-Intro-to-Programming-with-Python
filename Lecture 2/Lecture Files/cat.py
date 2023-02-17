i = 0
while i < 3:
    print("meow")
    i += 1


print("")  # print \n


for _ in range(3):
    print("meow")


print("")  # print \n


print("meow\n"*3, end="")


print("")  # print \n


while True:
    n = int(input("How many times would you like to meow back? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")