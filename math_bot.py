import time
import random

list1 = [1, 2, 3, 4, 5, 7, 7, 8, 9]
list2 = [10, 12, 13, 14, 15, 17, 19, 18, 20]

list_names = []

c = random.choice(list1)
b = random.choice(list1)
y = 0
a = 0
while True:
    a = str(input("Enter s to start the game- "))
    break
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Boom")
if a == 's':
    print("\n Game is started...\n")
    for x in range(4):
        names = input("Enter your name ")
        list_names.append(names)

    print(list_names)

    # """for y in range(len(list_names)):"""

    while (True):
        c = random.choice(list1)
        b = random.choice(list1)
        print(f"{list_names[y]}, it's your turn.")
        print(f"\nMutliply {c} x {b}")
        d = int(
            input("=")
        )  # int is used to get input in int form  and to make sure if will work only then
        t = c * b

        if (t == d):
            print("\nCheers!\n")
        else:
            print(
                f"{list_names[y]}, You're eliminated. Correct answer is {t}\n."
            )
            list_names.remove(list_names[y])
            y = 0
            print(list_names)

        if len(list_names) == 1:
            print(f" {list_names[y]} is the Winner. ")
            break
        y += 1
        if len(list_names) == y:
            y = 0

else:
    print("Wrong command, Game is aborted")


def timer():
    for z in range(1, 101, 1):
        time.sleep(0.1)
    nb = z / 10
    print(f"Total {int(nb)} seconds")
