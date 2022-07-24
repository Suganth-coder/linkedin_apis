import requests as req

web_link = input("Enter the website link: ")
resp = req.get(web_link)

print(resp.status_code)

