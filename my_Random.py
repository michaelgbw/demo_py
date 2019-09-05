import math
import random

def MaxMinNormalization(x,Max=62,Min=1):
	x = float(x - Min) / float(Max - Min);
	return float(x);


def which_part(n, w):
	for i, v in enumerate(w):
		if n < v:
			return i
	return len(w) - 1


def weighting_choice(x, data, weightings):
	s = sum(weightings)
	w = [float(x)/s for x in weightings]
	t = 0
	for i, v in enumerate(w):
		t += v
		w[i] = t
	c = which_part(MaxMinNormalization(x=x,Max=62,Min=1), w)
	try:
		return data[c]
	except IndexError:
		return data[-1]

if __name__ == '__main__':
	group = ['a', 'b','c','d']
	group_rat = [20, 20, 30, 30]
	'''
	res = {}
	for i in group:
		res[i] = 0
	
	for i in range(0,1000):
		res[(weighting_choice(x,group,group_rat))] += 1
	'''


	#usage:
	m2 = '92da9a3ed74495f8d005587bf6acbca4'	
	x = ord(m2[-1])
	res = weighting_choice(x,group,group_rat)
	print(res)


