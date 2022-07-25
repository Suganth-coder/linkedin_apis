from basefiles import StoreData 
import json
# l = LinkedIn('test','test')
# l.test()


import requests

sd = StoreData()

buff = sd.operate_file(f_name='test.txt',mode="r")
dic = json.loads(buff)

# headers = dic
# print(headers)
headers = {}
headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"  

        
company_link = 'https://www.linkedin.com/voyager/api/identity/profiles/ACoAAAC2eqYB5Eg-JCzGJxAmnBCGS72UBnYyaA8/networkinfo'

with requests.session() as s:
    
    for key,value in dic['suganthwork@gmail.com'].items():
        s.cookies[key]=value
        

    s.headers = headers
    s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
    print(s.headers["csrf-token"])
    response = s.get(company_link)
    response_dict = response.json()
    print(response_dict)

