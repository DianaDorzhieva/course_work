from utils import monetary_transaction, change_number_card
from datetime import datetime

operation_client = change_number_card()
for i in range(5):
    date_client = datetime.fromisoformat(operation_client[i]['date']).strftime("%d-%m-%Y")
    print(date_client, operation_client[i]["description"])
    if "from" in operation_client[i]:
     print(f"""{operation_client[i]["from"]}  -> {operation_client[i]["to"][0:5]}**{operation_client[i]["to"][7:11]} """)
    else:
        print(f"""Перевод на {operation_client[i]["to"][0:5]}**{operation_client[i]["to"][7:11]}""")
    print(operation_client[i]["operationAmount"]["amount"], operation_client[i]["operationAmount"]["currency"]["name"])
    print("-------")