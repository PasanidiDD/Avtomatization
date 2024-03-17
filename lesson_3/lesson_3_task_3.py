from address import Address
from mailing import Mailing

letter = Mailing(Address("353450", "Novorossiysk", "Udalova", "10","apartment_109"), 
                 Address("353483",  "Gelendgik", "Tihaya", "1","apartment_1"), 
                 "$10", "1234567890")

print(f"Отправление {letter.track} из {letter.from_address}")