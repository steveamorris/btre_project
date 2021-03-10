Model/DB Fields 

## Listing 

id: INT 
realtor: INT (foreign key [realtor])
Title: Str
Address: str
City: str
State: str
Zip: str
Descriptipn: Text
price: int
bedrooms: int
bath: int
garage: int [0]
list_date: date
square_ft: int
lot_size: float
is_published: bool [true]
photo_main: str
photo_1: str
photo_2: str
photo_3: str
photo_4: str
photo_5: str
photo_6: str





## Realtor 
id: int
name: str
photo: str
desciption: text
email: str
phopne: str
is_mvp: bool [0]
hire_date: date


## Contact 

id: int
user_id: int
listing: int
listing_id: int
name: str
email: str
phone: str
message txt
contact_date: date
