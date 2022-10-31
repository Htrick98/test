import requests, time, locale, random

from requests.structures import CaseInsensitiveDict
baseUrl="https://z7api.superlozzi.com/v2/"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVhMDI1MTVmZSJ9.eyJpYXQiOjE2NjU3MTQyNjg5OTYsImV4cCI6MTY2ODMwNjI2ODk5NiwiYXVkIjoibXlhdWQiLCJpc3MiOiJteWlzc3VlciIsInN1YiI6IjdhZmM5ZGE4LWQxY2YtNGY5ZC05NDkwLWFiOTgxMTJiYzRlZiIsImp0aSI6IjE2NjU3MTQyNjg5OTYifQ.ntrcv27MkLzlkURR8um6YnF6d1I5E0FL0XNuc0tRDDQ"

headers = CaseInsensitiveDict()
headers["host"] = "z7api.superlozzi.com"
headers["x-locale"] = "en"
headers["content-language"] = "en"
headers["user-agent"] = "locale=en_US|lang_code=en|country_code=AA|version_code=33|os_type=os_tp_android|version_name=3.3"
headers["accept"] = "application/x-www-form-urlencoded"
headers["content-type"] = "application/x-www-form-urlencoded"
#headers["user-timezone"] = "Africa/Cairo"
headers["accept-encoding"] = "gzip"
headers["device_id"] = "A1665714246-535811b5-b7a4-6708-b89a-b89c0364034b"
headers["access_token"] = token
#headers["refresh_token"] = token
headers["authorization"] = "Bearer "+token

auto=0
def XC_USER_INFO():
	path="XC_USER_INFO"
	U_Info = requests.get(baseUrl+path, timeout=60, headers=headers)
	U_Info_J=U_Info.json()
	#print(U_Info_J)
	xc_amount=int(U_Info_J["xc_amount"])
	#issue_mine=int(float((xc_amount/248)))
	print(f"{xc_amount:,}")
	#print(f"{issue_mine:,}")
	#print(U_Info_J["etc_info"]["issue_mine"])
	print(f'issue_mine : {U_Info_J["etc_info"]["issue_mine"]}')
	XC_EXCHANGE_TO_LOTTO(xc_amount)
	
def NA_SIGN_IN():
	try:
		path = "NA_SIGN_IN"
		headers["content-type"] = "application/x-www-form-urlencoded"
		data = f"user_email=htrick198@gmail.com&google_id=N&signup_cd_id=SIGNUP_TYPE_COMMON&device_id=535811b5-b7a4-6708-b89a-b89c0364034b&push_key=N&google_uid=N&user_pass=#Meza2022"
		resp = requests.post(baseUrl+path, headers=headers, data=data)
		b=resp.json()
		headers["access_token"] = b["refreshToken"]
		headers["refresh_token"] = b["refreshToken"]
		headers["authorization"] = "Bearer "+b["refreshToken"]
		print(b["refreshToken"])
	except Exception as error:
		print(b)
		
def XC_ISSUE_AUTO():
	path="XC_ISSUE_AUTO"
	#path="XC_AUTO_RENEW"
	auto = requests.post(baseUrl+path, headers=headers)
	print(auto.json())

def XC_BOX():
	try:
		path="XC_ISSUE_DEF"
		XC_DEF = requests.post(baseUrl+path, timeout=60, headers=headers)
		XC_DEF_J=XC_DEF.json()
		#print(XC_DEF_J)
		WITHOUT_ADD=0
		WITH_ADD=0
		BOX_GOLDD=0
		for box in XC_DEF_J["box_common"]:
			if box["xc_tp_cd_id"] == "XC_EVNT_0003":
				r1=WITHOUT_AD(box)
				WITHOUT_ADD+=r1["xc_amount"]
			elif box["xc_tp_cd_id"] == "XC_EVNT_0004":
				r2=WITH_AD(box)
				WITH_ADD+=r2["xc_amount"]
				
			else:
				print(box["xc_tp_cd_id"])
				
		for box in XC_DEF_J["box_gold"]:
			r3=BOX_GOLD(box)
			BOX_GOLDD+=r3["xc_amount"]
			
			
		print("WITHOUT_AD ", WITHOUT_ADD)
		print("WITH_AD ", WITH_ADD)
		print("BOX_GOLD ", BOX_GOLDD)
	except requests.exceptions.ConnectionError:
		#print("requests.exceptions.ConnectionError")
		XC_BOX()
	except Exception as error:
		print(error)
		print("1")
		
		
def SET_USER_STATUS():
		path="SET_USER_STATUS"
		data="push_key=N"
		SET_STATUS = requests.post(baseUrl+path, timeout=60, headers=headers, data=data)
		SET_STATUS_J=SET_STATUS.json()
		print(SET_STATUS_J)
		
def BOX_GOLD(box):
	try:
		path="XC_ISSUE_BOX_GOLD"
		data3=f'seq_no={box["seq_no"]}&box_key={box["box_key"]}'
		ISSUE3 = requests.post(baseUrl+path, timeout=60, headers=headers, data=data3)
		ISSUE3_J=ISSUE3.json()
		return ISSUE3_J
	except requests.exceptions.ConnectionError:
		BOX_GOLD(box)
	except Exception as error:
		print(error)
		print("2")
		
def WITH_AD(box):
	try:
		path="XC_ISSUE_BOX_COMMON_WITH_AD"
		data2=f'seq_no={box["seq_no"]}&box_key={box["box_key"]}'
		ISSUE2 = requests.post(baseUrl+path, timeout=60, headers=headers, data=data2)
		ISSUE2_J=ISSUE2.json()
		return ISSUE2_J
	except requests.exceptions.ConnectionError:
		WITH_AD(box)
	except Exception as error:
		print(error)
		print("3")
		
def WITHOUT_AD(box):
	try:
		path="XC_ISSUE_BOX_COMMON_WITHOUT_AD"
		data1=f'seq_no={box["seq_no"]}&box_key={box["box_key"]}'
		ISSUE1 = requests.post(baseUrl+path, timeout=60, headers=headers, data=data1)
		ISSUE1_J=ISSUE1.json()
		return ISSUE1_J
	except requests.exceptions.ConnectionError:
		WITHOUT_AD(box)
	except Exception as error:
		print(error)
		print("4")
		

def XC_EXCHANGE_TO_LOTTO(xc):
	path="XC_EXCHANGE_TO_LOTTO"
	issue_cnt=xc/248
	data4=f'issue_cnt={int(issue_cnt)}&xc_amount={xc}'
	r=requests.post(baseUrl+path, timeout=60, headers=headers, data=data4)
	print(r.json())		
	

SET_USER_STATUS()
#XC_USER_INFO()
for x in range(99999):
	XC_BOX()
	if auto >= 2200:
		SET_USER_STATUS()
		#XC_ISSUE_AUTO()
		auto=0
	else:
		auto+=30
	print()
	time.sleep(30.0)
