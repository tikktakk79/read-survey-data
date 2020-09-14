def add_calc(ans_arr):
    new_arr = []

    for ans in ans_arr:
        ans_dict = {}
        ans_dict["department"] = ans[0]
        ans_dict["question"] = ans[1]
        ans_dict["gender"] = ans[2]
        ans_dict["data"] = ans[3]
        ans_dict["percentages"] = []

        if sum(ans[3]) == 0:
            ans_dict["percentages"] = [0, 0, 0, 0, 0, 0, 0]
            ans_dict["index"] = ans_dict["share_1_2"] = ans_dict["share_5_6"] = 0
        else:
            numbers = ans[3]

            print("NUMBERS ", numbers)
            for i, x in enumerate(numbers[:-1]):
                ans_dict["percentages"].append(round(100 * x/numbers[7]))

            this_sum = 0

            for j, q in enumerate(numbers[:-2], 1):
                this_sum += q * j

            # The number of respondents who have given a reply on the scale
            no_replies = numbers[7] - numbers[6]

            ans_dict["index"] = round(100 * (this_sum / (no_replies * 6)), 1)

            ans_dict["share_1_2"] = round(100 * (sum(numbers[:2]) / no_replies))

            ans_dict["share_5_6"] = round(100 * (sum(numbers[4:6]) / no_replies))

        new_arr.append(ans_dict)

    return new_arr


