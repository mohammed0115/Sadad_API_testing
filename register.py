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
"userName":"mohammed kamal",
"entityId":"249994195556",
"entityType":"Phone NO",
"entityGroup":"MTN",
"phoneNo":"249994915556",
"registrationType":"01"
}


print(data)
headers = {
            'content-type': "application/json",
                   }
url = 'http://45.77.252.45/Card/register/Virtual/'
response = requests.request( 'POST', url, json=data, headers=headers)
print(response.text)

