'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

def main():
	'''
	@author : SandhyaKamisetty
	To print number of times the string 'bob' occurs in s.
	'''
	n_m = input()
	s_m = "bob"
	c_m = 0
	for i_m in range(0, len(n_m) - 2):
		j_m = 0
		k_m = i_m
		v_m = 0
		while(j_m < 3 and n_m[k_m] == s_m[j_m]):
			v_m += 1
			k_m += 1
			j_m += 1
	    if v_m == 3:
	    	c_m += 1
	print(c_m)
	# the input string is in s
	# remove pass and start your code here
	pass

if __name__== "__main__":
	main()
