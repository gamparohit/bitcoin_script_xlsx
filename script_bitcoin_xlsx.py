#!/usr/bin/python3
from pycoingecko import CoinGeckoAPI
import xlsxwriter
import time
cg = CoinGeckoAPI()
n = 0
filename='bitcoin_%s'%datetime.datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
workbook = xlsxwriter.Workbook(filename+'.xlsx')
worksheet = workbook.add_worksheet('prices')
worksheet.write(n, 0, 'last_updated')
worksheet.write(n, 1, 'current_price')
worksheet.write(n, 2, 'total_volume')
n+=1
while True:
	try:
		data=cg.get_coins_markets('usd',ids='bitcoin')[0]
		if n==1:
			worksheet.write(n, 0, data['last_updated'])
			worksheet.write(n, 1, data['current_price'])
			worksheet.write(n, 2, data['total_volume'])
			n+=1
			myresult=data['current_price']
		elif n>=10000:
			workbook.close()
			n=0
			filename='bitcoin_%s'%datetime.datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
			workbook = xlsxwriter.Workbook(filename+'.xlsx')
			worksheet = workbook.add_worksheet('prices')
			worksheet.write(n, 0, 'last_updated')
			worksheet.write(n, 1, 'current_price')
			worksheet.write(n, 2, 'total_volume')
			n+=1
			worksheet.write(n, 0, data['last_updated'])
			worksheet.write(n, 1, data['current_price'])
			worksheet.write(n, 2, data['total_volume'])
			n+=1
			myresult=data['current_price']
		else:
			if abs(int(myresult)-int(data['current_price']))>=2:
				worksheet.write(n, 0, data['last_updated'])
				worksheet.write(n, 1, data['current_price'])
				worksheet.write(n, 2, data['total_volume'])
				n+=1
				myresult=data['current_price']
			else:
				continue
	except Exception as e:
		print(e)
		continue
	time.sleep(1)