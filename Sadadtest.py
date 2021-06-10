
import re
import requests
import datetime
import uuid
from dateutil.tz import tzoffset
import json
import time
from EncriptIPIN import EnayaTechBase
""" YYYY-MM-
DDThh:mm:ssTZD"""
#tranDateTime =datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
#tranDateTime =datetime.datetime.now().strftime("%d%m%y%H%M%S")
tranDateTime=str(datetime.datetime.now())
print(tranDateTime)
# uui=str(uuid.uuid4())
Enaya=EnayaTechBase()
Ipin,uu=Enaya.encryptIPIN("0000")
# print(Ipin)
# print(uu)
# uui=str(uuid.uuid1())

data={
"tranDateTime":tranDateTime,
"UUID":str(uu),
"PAN":"2222247701960189300",
"expDate":"2403",
"IPIN":Ipin,
"authenticationType": "00",
"fromAccountType": "00",
"tranCurrency": "SDG",
"mbr": "0"
}
"""
data={
"tranDateTime":tranDateTime,
"UUID":str(uu),
"PAN":"2222247701542992353",
"expDate":"2403",
"IPIN":Ipin,
"authenticationType": "00",
"fromAccountType": "00",
"tranCurrency": "SDG",
"mbr": "0"
}
"""
print(data)
result =Enaya.Balance(**data)
print(result)



