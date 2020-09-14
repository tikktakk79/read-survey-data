import xlsxwriter
import copy

def xsort(departments, questions, in_arr):
    new_arr = []

    for dep in departments:
        cont_arr = [""] * 20
        dep_arr = []
        for q in questions:
            this_arr = copy.copy(cont_arr)
            this_arr[0] = q
            dep_arr.append(this_arr)

        for i in in_arr:
            if i["department"] == dep:
                temp_arr = []
                for j in i["data"][:-2]:
                    temp_arr.append(j)
                temp_arr.append("")
                temp_arr.append(i["share_1_2"])
                temp_arr.append(i["share_5_6"])


                for q_index, q in enumerate(questions, 0):
                    temp_start = 1
                    if i["question"] == q:
                        if i["gender"] == "Man":
                            temp_start = 11
                        counter = 0
                        for s in range(temp_start, temp_start + 9):
                            dep_arr[q_index][s] = temp_arr[counter]
                            counter += 1

        dep_arr.insert(0, [dep])
        new_arr.append(dep_arr)

    return new_arr


    # sorted_arr = sorted(in_arr, key = lambda i: (i['department'], i['gender'], i['question']))

def xwrite(arr):
    wb = xlsxwriter.Workbook('arrays.xlsx')
    ws = wb.add_worksheet()

    label_row_1 = ["", "Kvinnor", "", "", "", "", "", "", "", "", "",
                    "Män", "", "", "", "", "", "", "", "", "",]
    label_row_2 = ["", "%1", "%2", "%3", "%4", "%5", "%6", "", "% 1 eller 2", "% 5 eller 6","",
                    "%1", "%2", "%3", "%4", "%5", "%6", "", "% 1 eller 2", "% 5 eller 6"]
    row = 0
    for loc_arr in arr:
        for i, data in enumerate(loc_arr):
            ws.write_row(row, 0, data)
            if i == 0:
                row += 1
                ws.write_row(row, 0, label_row_1)
                row += 1
                ws.write_row(row, 0, label_row_2)
            row += 1
        row += 1

    wb.close()




















# def xwrite(in_arr):
