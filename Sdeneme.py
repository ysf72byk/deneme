import requests
while 1:
	r=requests.get('https://siberdeyiz.com/u/onecame33/9394')
	print(r.status_code)
	#print(r.text)
	a=r.text.split('Görüntülenme =')[1].split('">')[0]
	print(a)
