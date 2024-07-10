from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("bdre/phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
phonebook = []
for row in contacts_list:
  phonebook.append(((" ".join(row[:3])).split(' '))[:3] + row[-4:])

phonebook2 = []
for row in phonebook:
  numbers = ",".join(row)
  regex = r"(\+7|8)\s*\(*(\d+)\)*[-|\s]*(\d+)[-|\s]*(\d+)[-|\s]*(\d+)[-|\s]*\(*(доб.)*[\s]*(\d+)*\)*"
  result = re.sub(regex, "+7(\\2)\\3-\\4-\\5 \\6 \\7", numbers)
  if row[:2] not in [x[:2] for x in phonebook2]:
    phonebook2.append(result.split(','))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("bdre/phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(phonebook2)