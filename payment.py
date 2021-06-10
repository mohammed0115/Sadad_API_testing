

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
print("Now can make card to card transfer")
Enaya=EnayaTechBase()
Ipin,uu=Enaya.encryptIPIN("0000")
print(Ipin)
print(uu)

data={
"tranDateTime":tranDateTime,
"UUID":str(uu),
"PAN":"2222247701960189300",
"expDate":"2403",
"IPIN":Ipin,
"authenticationType": "00",
"mbr": 0,
"payeeId" : "0010020001",
"paymentInfo": "METER=04111111111",
"fromAccountType": "00",
"tranAmount": 10
}



print(data)
headers = {
            'content-type': "application/json",
                   }
url = 'http://45.77.252.45/Payment/'
response = requests.request( 'POST', url, json=data, headers=headers)
print(response.text)
