class Address:
 def __init__(self, zipcode, city, street, house_number, apartment): 
    self.zipcode = zipcode
    self.city = city
    self.street = street
    self.house_number = house_number  
    self.apartment = apartment  
 def __str__(self): return f"{self.zipcode}, {self.city}, {self.street}, {self.house_number}, {self.apartment} " 