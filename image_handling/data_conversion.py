def make_numbers(occ_arr):
    short_arr = []

    for value in occ_arr:
        temp_arr = []
        for i, val2 in enumerate(value):
            if not (isinstance(val2, str) or len(val2) == 0):
                for j in val2:
                    temp_arr.append([i, j])
        temp_arr.sort(key = lambda x: x[1])
        short_arr.append(temp_arr)

    numbers_arr = []

    for q in short_arr:
        temp_str = ""
        for z in q:
            temp_str = temp_str + str(z[0])

        if temp_str.isnumeric():
            numbers_arr.append(int(temp_str))
        else:
            numbers_arr.append(0)

    return numbers_arr


