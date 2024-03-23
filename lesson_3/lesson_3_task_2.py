from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Huawei", "Honor9x", "+79180408200"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79645321097"))
catalog.append(Smartphone("Realme", "Note50", "+79283451098"))
catalog.append(Smartphone("Xiomi", "RedmiNote13Pro", "+79996306049"))
catalog.append(Smartphone("Oppo", "F5", "+79237654238"))

for phone in catalog:
    print(f"{phone.phone_maker} - {phone.model}. {phone.phone_number}")