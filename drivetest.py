drining = input('Have you drived before?')
if drining != 'yes' and drining != 'no':
	print('Please input "yes" or "no" only.')
	raise SystemExit

else:
	if drining == 'yes':
		age = input ('How old are you?')
		if int(age)>=18:
			print('Ok you are passed.')
		elif int(age)<18:
			print('So, you are lying me.')
	else:
		print('Go to get a pass please.')
	
