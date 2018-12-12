# Wednesday, December 12, 2018

	Ken Recommends:

		https://coderbyte.com/

		# Big O Cheat Sheet O(n)
		http://bigocheatsheet.com/

	Udacity Recommendations:

		Books
		Cracking the Code Interview
		Elements of Programming Interviews
		Web Resources

		Interview Guide: Machine Learning
		Project Euler
		The Matasano Crypto Challenges
		List of Programming Interview Questions

		Online Practice Platforms
		LeetCode
		CodeKata
		Coderust
		Interview Cake
		Codewars
		HackerRank
		Career Resource Center



"""
Quiz #1
"""

# Palindrome Method, Boolean.

# Phillip's Answer
"""
def is_palindrome(s):
    s = s.strip()
    return s == reverse(s)

print ("Yes")
print (is_palindrome("racecar"))
"""

"""
Program to check if a string is palindrome or not.
Palindrome question is a warm-up question.

""" 

# change this value for a different output
my_str = 'AmanaplanacanalPanama'


my_str = my_str.strip()
# add a replace function.

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")


"""
Quiz #2:
"""

# What happens when you go to google.com?

