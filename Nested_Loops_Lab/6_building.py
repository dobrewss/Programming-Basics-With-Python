floors = int(input())
rooms_per_floor = int(input())

flat_name = ""
flat_number = 0

for current_floor in range(floors, 0, -1):
    for apartment_num in range(rooms_per_floor):
        #number_apartment = apartment_num + current_floor
        if current_floor == floors:
            flat_name = f"L{current_floor}{apartment_num}"
        elif current_floor % 2 == 0:
            flat_name = f"O{current_floor}{apartment_num}"
        elif current_floor % 2 != 0:
            flat_name = f"A{current_floor}{apartment_num}"

        print(flat_name, end=" ")
    print()