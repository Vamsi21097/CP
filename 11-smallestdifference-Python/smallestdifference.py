# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	if a==[]:
		return -1
	# Your code goes here
	diff = []
	for i in range(0,len(a)):
		for j in range(i+1,len(a)):
			# print(a[i],a[j])
			s = abs(a[i]-a[j])
			# print(abs(s))
			diff.append(s)
		# print(diff)
	return min(diff)