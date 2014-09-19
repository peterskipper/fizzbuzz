#fizz buzz v1 
#Unit 1 Lesson 4 Project
import sys

print "Fizz buzz counting up to 100"
limit = 100
for i in xrange(1,limit+1):
	fizzbuzz = False
	if i % 3 == 0:
		print "fizz",
		fizzbuzz = True
	if i % 5 == 0:
		print "buzz",
		fizzbuzz = True
	if not fizzbuzz:
		print str(i),
	print #get a new line

