n = 2

# if control
if 0 == n:
	print('n is equal 0')
elif 1 == n:
	print('n is equal 1')
else:
	print('n is ' + str(n))

# while control
i = 0

while i < 10:
	i += 1
	print(i)


# try control
try:
  risky()
except:
  print('risky failed')


