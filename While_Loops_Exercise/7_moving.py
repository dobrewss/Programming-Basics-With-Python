free_space = int(input()) * int(input()) * int(input())
space_filled = 0

while space_filled < free_space:
    box = input()  # number or DONE

    if box == "Done":
        print(f"{free_space - space_filled} Cubic meters left.")
        break

    space_filled += int(box)
else:
    print(f"No more free space! You need {space_filled - free_space} Cubic meters more.")