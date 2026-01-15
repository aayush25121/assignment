# PROBLEM 1: ARRANGING CLOTHES IN AN ALMIRAH (n shelves)

def arrange_almirah(n_shelves, clothes_list):
    # Step 1: Create empty lists to store clothes based on their usage frequency
    daily_use_clothes = []     # clothes used daily (easy access needed)
    weekly_use_clothes = []    # clothes used weekly (normal access)
    rare_use_clothes = []      # clothes used rarely (least access)

    # Step 2: Separate clothes into the above lists
    for cloth in clothes_list:

        # If the cloth is used daily, store it in daily_use_clothes list
        if cloth in ["casual", "innerwear", "school_wear"]:
            daily_use_clothes.append(cloth)

        # If the cloth is used weekly, store it in weekly_use_clothes list
        elif cloth in ["formal", "gym_wear"]:
            weekly_use_clothes.append(cloth)

        # Otherwise, store it in rare_use_clothes list
        else:
            rare_use_clothes.append(cloth)

    # Step 3: Create a dictionary to represent shelves of the almirah
    # Key = shelf number, Value = list of clothes placed on that shelf
    shelves = {}

    # Step 4: Initialize each shelf as empty
    for shelf_number in range(1, n_shelves + 1):
        shelves[shelf_number] = []   # empty shelf created

    # Step 5: Choose the middle shelf because it is easiest to access
    middle_shelf = (n_shelves // 2) + 1

    # Step 6: Put daily-use clothes in the middle shelf for quick access
    shelves[middle_shelf] = daily_use_clothes

    # Step 7: Place weekly-use clothes in the shelf next to middle shelf if possible
    left_shelf = middle_shelf - 1
    right_shelf = middle_shelf + 1

    # If left shelf exists, place weekly clothes there
    if left_shelf >= 1:
        shelves[left_shelf] = weekly_use_clothes

    # If right shelf exists, place weekly clothes there (only if not already filled)
    if right_shelf <= n_shelves and shelves[right_shelf] == []:
        shelves[right_shelf] = weekly_use_clothes

    # Step 8: Fill the remaining shelves with rare-use clothes
    for shelf_number in range(1, n_shelves + 1):
        # If shelf is still empty, place rare-use clothes there
        if shelves[shelf_number] == []:
            shelves[shelf_number] = rare_use_clothes

    # Step 9: Print the final shelf arrangement
    print("✅ FINAL ALMIRAH ARRANGEMENT:\n")
    for shelf_number in range(1, n_shelves + 1):
        print("Shelf", shelf_number, "->", shelves[shelf_number])

    # Step 10: Return the final shelves dictionary (optional)
    return shelves