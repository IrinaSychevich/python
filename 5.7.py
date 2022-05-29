import json
with open(r"new_f_5.7.txt", 'r', encoding='utf-8') as f1:
    content = f1.readlines()
    all_firm = []
    all_profit = []
    n = 0
    for el in content:
        el = el.split(' ')
        firm = el[0]
        revenue = int(el[2])
        costs = int(el[3])
        profit = revenue - costs
        all_profit.append(profit)
        all_firm.append(firm)
        n += 1
    new_all_profit = [all_profit[i] for i in range(0, len(all_profit)) if all_profit[i] > 0]
    average_profit = sum(new_all_profit) / n
    dict_result = {}
    k = 0
    while k < len(all_firm):
        dict_result.update({all_firm[k]: all_profit[k]})
        k += 1
    dict_average_profit = ({'average_profit': average_profit})
    list_result = (dict_result, dict_average_profit)
    print(list_result)
    with open("new_f_5.7.json", "w") as f2:
        json.dump(list_result, f2)

