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
Ipin,uu=Enaya.encryptIPIN("0000")
#uu=str(uuid.uuid1())
data={
"tranDateTime":tranDateTime,
"UUID":str(uu),
"PAN":"2222247701960189300",
"expDate":"2403",
"IPIN":Ipin,
"payeeId":"0010010001",
"paymentInfo": "MPHONE=0960629310",
"authenticationType":"00"

}
"""
{
    "tranDateTime": [
        "This field is required."
    ],
    "UUID": [
        "This field is required."
    ],
    "PAN": [
        "This field is required."
    ],
    "IPIN": [
        "This field is required."
    ],
    "expDate": [
        "This field is required."
    ],
    "payeeId": [
        "This field is required."
    ],
    "paymentInfo": [
        "This field is required."
    ],
    "tranAmount": [
        "This field is required."
    ]
}

"""

print(data)
result =Enaya.getbill(**data)
print(result)
