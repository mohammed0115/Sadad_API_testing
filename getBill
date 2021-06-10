#TransactionStatus

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
#Ipin,uu=Enaya.encryptIPIN("0000")
uu=str(uuid.uuid1())
data={
"tranDateTime":tranDateTime,
"UUID":str(uu),
 "originalTranUUID":"fc4cd9ea-707b-4885-ba46-e6a9a9bf6fbc"
}

print(data)
result =Enaya.transactionStatus(**data)
print(result)
