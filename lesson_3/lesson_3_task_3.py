from address import Address
from mailing import Mailing

letter = Mailing(Address("353450", "Новороссийск", "Удалова", "10","кв_109"), 
                 Address("353483",  "Геленджик", "Тихая", "1","кв_1"), 
                 "1000", "1234567890")

print(f"Отправление {letter.track} из {letter.from_address} в {letter.to_address}. Стоимость {letter.cost} рублей")