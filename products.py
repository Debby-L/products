products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': 
		break
	price = input('請輸入商品價格:')
	# 如果price = int(price) 直接輸入數字，下方寫入時字串和數字結合將修改
	p = [] #建立小清單包含商品和價格
	p.append(name)
	p.append(price)
	# p = [name, price] 取代上面三行
	products.append(p) #將小清單裝入大清單中
	#products.append([name, price])綜合以上程式碼
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding= 'utf-8') as f: 
# txt = text, csv = excel
#解決亂碼問題, encoding= 'utf-8'解決中文便亂碼問題
#excel匯入csv資料：data-->external data-->text-->utf-8-->分隔符號:選comma
    f.write('商品,價格\n') #在商品前置入標題欄位
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 0=商品名稱 , 1=價格 + \n 換行 ','做區隔
#因為上方price設定為數字，所以字串與數字結合要修改為 str(p[1]),修改為字串與字串結合

