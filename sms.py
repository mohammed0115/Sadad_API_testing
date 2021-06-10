import requests
message="السلام عليكم ورحمته تعالي وبركاته حبيبتي سعديه انا كم احبك واشتق اليك لقد ارسلت هذا عن طريق  تطبيق سداد        حبيبك الغالي محمد كمال"
phone="249991524441"



def sms(message,phone):
	url = "http://212.0.129.229/bulksms/webacc.aspx?user=sadad&pwd=806807&smstext="+message+"&Sender=sadad&Nums="+phone

	payload={}
	headers = {
  		'Content-Type': 'application/json'
	}

	return requests.request("GET", url, headers=headers, data=payload)
	
print(sms(message,phone))
