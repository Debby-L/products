#加入作業系統檢查檔案
import os 

#讀取檔案
products = [] #無論是否有找到檔案，先列清單，後面還可以寫入
if os.path. isfile('products.csv'): #輸入相對入徑檢查是不是在目前資料夾中，如果要檢查是否在莊志忠則需要寫入絕對入徑	
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue  #只能再迴圈內,繼續下一回
			name, price = line.strip().split(',')
			# strip()除掉, split('')分割,顯示結果是清單
			products.append([name, price])
	print(products)


else:
	print('找不到檔案....')


#請使用者輸入
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

#列出所有商品購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding= 'utf-8') as f: 
# txt = text, csv = excel
#解決亂碼問題, encoding= 'utf-8'解決中文便亂碼問題
#excel匯入csv資料：data-->external data-->text-->utf-8-->分隔符號:選comma
    f.write('商品,價格\n') #在商品前置入標題欄位
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 0=商品名稱 , 1=價格 + \n 換行 ','做區隔
#因為上方price設定為數字，所以字串與數字結合要修改為 str(p[1]),修改為字串與字串結合

