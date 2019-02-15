# --------------
#Code starts here
import sys

def palindrome(num):
 numstr = str(num)
 for i in range(num+1,sys.maxsize):
  if str(i)== str(i)[::-1]:
   return i

palindrome(123)


# --------------
#Code starts here

from collections import Counter

def a_scramble(str_1,str_2):
    list_str1 = Counter(str_1.lower())
    print(list_str1)

    list_str2 = Counter(str_2.lower())
    print(list_str2)

    if not list_str2 - list_str1:
     return True
    else:
     return False

a_scramble("Tom Marvolo Riddle","Voldemort") 


# --------------
#Code starts here

import math

def isPerfectSquare(x):
 s = int(math.sqrt(x))
 return s*s == x

def check_fib(num):
 return isPerfectSquare(5*num*num + 4)or isPerfectSquare(5*num*num - 4)

check_fib(377)


# --------------
#Code starts here

def compress(word):
 string = word.lower()
 res = ""

 count = 1

 res += string[0]

 for i in range(len(string)-1):
  if(string[i]==string[i+1]):
   count+=1
  else:
   if(count >= 1):
    res += str(count)
   res += string[i+1]
   count = 1
 if(count >= 1):
  res += str(count)
 return res

compress("abbs")


# --------------
#Code starts here
#Code starts here
from collections  import Counter

def k_distinct(string,k):
 c  = Counter(string.lower())
 if k==len(c.keys()):
  return True
 return False
    

k_distinct('Messoptamia',8)
k_distinct('SUBBOOKKEEPER',7)


