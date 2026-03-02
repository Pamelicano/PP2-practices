import re
import json

with open("Practice 5/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# TASK 1
costing = {}
cost = r'Стоимость\n((?:.*\n){%d})' % 1
x = re.findall(cost, text)
sum = 0
for i, block in enumerate(x, 1):
    s = block.rstrip()
    # print(f'\n{block.rstrip()}\n')
    number = float(s.replace(" ", "").replace(",", "."))
    sum += number
last = x[-1].rstrip()

#TASK 2
y = re.findall(r'\b\d+\.\n(.*)', text)
for i, line in enumerate(y, 1):
    costing[line] = x[i-1]

# TASK 3
# print(sum)

#TASK 4
pattern = r"(\d{2})\.(\d{2})\.(\d{4}) (\d{2}):(\d{2}):(\d{2})"
w = re.search(pattern, text)
str23 = ""
if w:
    day, month, year, hour, minute, second = w.groups()
    str23 = day + "/"+month +"/"+year+" "+hour+":"+minute+":"+second
    # print(day, month, year, hour, minute, second)

last_es = re.escape(last)
pattern_next = last_es + r'\n(.*)'
match = re.findall(pattern_next, text)
new_ls = ""
if match:
    ls = match[1]
    new_ls = ls[0:-1]
    # print(new_ls)

costing.update({"Итог": sum})
costing.update({"Способ оплаты" : new_ls})

costing.update({"Дата покупки" : str23})
# for line in costing:
#     print(line + ":", costing[line])

json_string = json.dumps(costing, ensure_ascii=False, indent=4)
with open("data.json", "w", encoding="utf-8") as f:
    f.write(json_string)