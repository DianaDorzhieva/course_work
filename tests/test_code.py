from utils import monetary_transaction,change_number_card
import json
def test_monetary_transaction():
    assert monetary_transaction()[0] == {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}

def test_change_number_card():
    assert change_number_card()[0] == {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}

