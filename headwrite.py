products = []
while True:
		a = input('Please input number:')
		if a == 'q':
			break
		price = input('Please input price:')
		p = []
		p.append(a)
		p.append(price)
		products.append(p)
with open('Test.csv', 'w', encoding = 'UTF-8') as f:
	f.write('Number,Price\n')
	for i in products:
		f.write(str(i) + '\n') #新增商品title       