def fullArrange(l, start, end):
	if start == end:
		print(l)
	else:
		j = start
		for i in range(start, end):
			l[i], l[j] = l[j], l[i]
			fullArrange(l, start+1, end)
			l[i], l[j] = l[j], l[i]



if __name__ == '__main__':
	print(fullArrange(['a','b','c'],0,len(['a','b','c'])))
