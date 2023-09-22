import json
from datetime import datetime
def monetary_transaction():
    """ выводит на экран список из 5 последних выполненных клиентом операций"""
    with open("operations.json", "r", encoding="utf-8") as file:
     all_information = json.load(file)
     new_operation_sort = [] # будем сюда собирать словари с не пустыми значениями, а также с выполненными переводами
     for i in range(len(all_information)):
         if len(all_information[i]) != 0:
          data_operation = all_information[i]["date"]
          thedate = datetime.fromisoformat(data_operation)
          thedate1 = str(thedate).split(".")[0]
          all_information[i]["date"] = thedate1 #перевели данные в формат для сортировки
         if len(all_information[i]) != 0 and all_information[i]["state"] == "EXECUTED":
            new_operation_sort.append(all_information[i]) #добавили только словари с выполненными переводами

    new_operation_sort = sorted(new_operation_sort, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False)
    return new_operation_sort[::-1][0:5]

def change_number_card():
    """Функция для замены номера"""
    operation_client = monetary_transaction()
    for i in range(len(operation_client)):
        operation_word = "" # сюда собираем только слова ( название карты или слово "счет")
        operation_numb = "" # сюда собираем номер карты/счета и часть цифр меняем на звездочки
        result = "" # здесь соеденим название и цифры для конечного вывода
        if "from" in operation_client[i]: # проверка что в данных есть информация откуда идет перевод
            if operation_client[i]['from'][0] != "С": # проверяем какой вид перевода - счет или карта, в данном случае условие покажет перевед с карты
                for word in operation_client[i]['from']:
                    if not word.isnumeric() or word == " ":
                        operation_word += word
                    else:
                        operation_numb += word
                operation_numb = operation_numb[0:5] + " " + operation_numb[6:8] + "** ****" + " " + operation_numb[12:]
                result = operation_word + operation_numb
                operation_client[i]['from'] = result
        if "from" in operation_client[i] and operation_client[i]['from'][0] == "С": # здесь условие уже показывает, что идет перевод со счета
            for word in operation_client[i]['from']:
                if not word.isnumeric() or i == " ":
                    operation_word += word
                else:
                    operation_numb += word
            operation_numb = "**" + operation_numb[2:5]
            result = operation_word + operation_numb
            operation_client[i]['from'] = result
    return operation_client


print(change_number_card()[0])










