country = input('請輸入你的國家: ')
age = input ('請輸入年齡: ')
age = int(age)
if country == ('台灣'):
	if age >= 18:
		print('你可以學開車 ')
	else :
		print('你還不能學開車喔')
if country == ('美國'):
	if age >= 16:
		print('你可以學開車 ')
	else :
		print('你還不能學開車喔 ')