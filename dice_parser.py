from random import randint

def dice_parser(query_string):
    total = 0
    results = ""
    if "-" in query_string or "d0" in query_string:
        raise ValueError
    if "+" in query_string:  #TODO refactor whatever this hack is
        individual_rolls = query_string.split("+")
        for item in individual_rolls:
            if "d" in item:
                roll_info = item.split("d")
                results = results + "["
                if len(roll_info[0]) > 6:
                    roll = (int(roll_info[1]) + 1) * (int(roll_info[0]) / 2)
                    results = results + "Law of large numbers, "
                    total += int(roll)
                else:
                    for i in range(0, int(roll_info[0])):
                        roll = randint(1, int(roll_info[1]))
                        results = results + str(roll) + ", "
                        total += roll
                results = results[0:-2] + "], "
            else:
                total += int(item)
        results = results[0:-2]
        response = "You rolled " + str(total) + " (" + results + ")."
        if len(response) > 2000:
            response = "You rolled " + str(total) + " (Discrete dice limit exceeded)."
    else:
        roll_info = query_string.split("d")
        if len(roll_info[0]) > 6:
            roll = (int(roll_info[1]) + 1) * (int(roll_info[0]) / 2)
            results = results + "Law of large numbers, "
            total += int(roll)
        else:
            for i in range(0, int(roll_info[0])):
                roll = randint(1, int(roll_info[1]))
                results = results + str(roll) + ", "
                total += roll
        response = "You rolled " + str(total) + " (" + results[0:-2] + ")."
        if len(response) > 2000:
            response = "You rolled " + str(total) + " (Discrete dice limit exceeded)."

    return response

def max_dice_parser(query_string):
    total = 0
    results = ""
    if "-" in query_string or "d0" in query_string:
        raise ValueError
    if "+" in query_string:  #TODO refactor whatever this hack is
        individual_rolls = query_string.split("+")
        for item in individual_rolls:
            if "d" in item:
                roll_info = item.split("d")
                results = results + "["
                if len(roll_info[0]) > 6:
                    roll = (int(roll_info[1])) * (int(roll_info[0]))
                    results = results + "Law of large numbers, "
                    total += int(roll)
                else:
                    for i in range(0, int(roll_info[0])):
                        roll = roll_info[1]
                        results = results + str(roll) + ", "
                        total += roll
                results = results[0:-2] + "], "
            else:
                total += int(item)
        results = results[0:-2]
        response = "You rolled " + str(total) + " (" + results + ")."
        if len(response) > 2000:
            response = "You rolled " + str(total) + " (Discrete dice limit exceeded)."
    else:
        roll_info = query_string.split("d")
        if len(roll_info[0]) > 6:
            roll = (int(roll_info[1])) * (int(roll_info[0]))
            results = results + "Law of large numbers, "
            total += int(roll)
        else:
            for i in range(0, int(roll_info[0])):
                roll = int(roll_info[1])
                results = results + str(roll) + ", "
                total += roll
        response = "You rolled " + str(total) + " (" + results[0:-2] + ")."
        if len(response) > 2000:
            response = "You rolled " + str(total) + " (Discrete dice limit exceeded)."

    return response
