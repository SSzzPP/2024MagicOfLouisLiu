import numpy as np

def HappyNewYear(name: str= "Random ghost" ,wherefrom: str= "nowhere", gender: str= "helicopter"):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    
    # Random four poker cards
    init_array = np.random.randint(1, 14, size=(4) )
    print(init_array)

    # Tear them apart, place them in the same direction.
    tear_array = init_array 
    init_array = np.concatenate((init_array, tear_array))
    print(init_array)

    # Order by name length
    nameLen = len(name) % len(init_array)
    # Put the {nameLen} card to the end
    rolled_array = np.roll(init_array, -nameLen)
    print(rolled_array)

    # Put the first three cards anywhere in the middle of the array.
    first_three = rolled_array[:3]
    # Must be inserted in the middle
    insert_pos = np.random.randint(1, len(rolled_array) - 3)
    rolled_array = np.insert(rolled_array[3:], insert_pos, first_three)
    print(rolled_array)

    # Throw away the top card
    the_card = rolled_array[0]
    rolled_array = rolled_array[1:]

    # south:1 north:2 nowhere:3
    if "south" in wherefrom:
        pick_num = 1
    elif "north" in wherefrom:
        pick_num = 2
    else:
        pick_num = 3
    picked_array = rolled_array[:pick_num]
    # Not required
    insert_pos = np.random.randint(0, len(rolled_array) - pick_num)
    rolled_array = np.insert(rolled_array[pick_num:], insert_pos, picked_array)
    print(rolled_array)


    # man1 woman:2
    if "man" in gender:
        drop_num = 1
    elif "woman" in gender:
        drop_num = 2
    else:
        drop_num = np.random.randint(1, 3)

    dropped_array = rolled_array[:drop_num]
    rolled_array = rolled_array[drop_num:]
  
    # Result
    magic_array = np.roll(rolled_array, -7) 
    print(magic_array)

    # Stay yood luck, throw away trouble.
    flag = True
    while len(magic_array) > 1:
        # put first card from magic_array to the end of magic_array 
        # and drop first card from magic_array
        # till magic_array has only one card
        if flag:
            luck_card = magic_array[0]
            magic_array = np.concatenate((magic_array[1:], [luck_card]))
            flag = False
        else:
            trouble_card = magic_array[0]
            magic_array = magic_array[1:]
            flag = True

    last_card = magic_array[0]
    print(f"Last-{last_card}")
    print(f"First-{the_card}")

if __name__ == '__main__':
    HappyNewYear("Terminal manager","sourth","man")
