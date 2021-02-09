products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': 
		break
	price = input('請輸入商品價格:')
	p = [] #建立小清單包含商品和價格
	p.append(name)
	p.append(price)
	# p = [name, price] 取代上面三行
	products.append(p) #將小清單裝入大清單中
	#products.append([name, price])綜合以上程式碼
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
