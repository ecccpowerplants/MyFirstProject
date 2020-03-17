import numpy as np

def print_func(n):
	for i in range(n):
		print('Hey there cowboy...')
		
def concat_func(boi1, boi2):
	c = []
	for b1, b2 in zip(boi1.flatten(), boi2.flatten()):
		c.append(b1 + b2)
	return np.array(c)
