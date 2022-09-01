import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

phone_format = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
phone_standart = r'+7(\3)\6-\8-\10 \12\13'

# # TODO 1: выполните пункты 1-3 ДЗ
def main(contact_list: list):
  new_list = list()
  for item in contact_list:
    fio = ' '.join(item[:3]).split(' ')
    result = [fio[0], fio[1], fio[2], item[3], item[4],
              re.sub(phone_format, phone_standart, item[5]),
              item[6]]
    new_list.append(result)
  return union(new_list)

def union(deduplication: list):
  for data in deduplication:
    surname = data[0]
    name = data[1]
    for new_data in deduplication:
      new_surname = new_data[0]
      new_name = new_data[1]
      if surname == new_surname and name == new_name:
        if data[2] == "": data[2] = new_data[2]
        if data[3] == "": data[3] = new_data[3]
        if data[4] == "": data[4] = new_data[4]
        if data[5] == "": data[5] = new_data[5]
        if data[6] == "": data[6] = new_data[6]

  result_list = list()
  for i in deduplication:
    if i not in result_list:
      result_list.append(i)

  return result_list
#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook_new.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))
print("Данные записаны")