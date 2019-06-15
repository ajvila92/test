#Chapter 2 Exercises in Python by Perkovic on pages 48 - 51

#Exercise 2.12 
#a 
1 + 2 + 3 + 4 + 5 + 6 + 7
#b 
(65 + 57 + 45)/3
#c 
2**20
#d 
4356 // 61
#e 
4356 % 61

# Exercise 2.13
s1 = '-'; s2 = '+';
#a
s1 + s2
#b
s1 + s2
#c
s2 + 2*s1
#d
2*(s2 + 2*s1)
#e
10*(s2 + 2*s1) + s2
#f
5*((s2 + s1 + 3*s2 + 2*s1)

# Exercise 2.14
s = 'abcdefghijklmnopqrstuvwxyz'; s[0]; s[2]; s[-1]; s[-2]; s[-10];

#Exercise 2.15
s = 'goodbye'
#a
s[0] == 'g'
#b
s[6] == 'g'
#c
s[0] == 'g' and s[1] == 'a'
#d
s[-2] == 'x'
#e
s[3] == 'd'
#f
s[0] == s[-1]
#g
s[-4] + s[-3] + s[-2] + s[1] == 'tion'

#Exercise 2.16
#a
a = 6; b = 7;
#b
c = (a + b)/2
#c
inventory = ['paper', 'staples', 'pencils']
#d
first = 'John'; middle = 'Fitzgerald'; last = 'Kennedy'
#e
fullname = first + ' ' + middle + ' ' + last

#Exercise 2.17
#a
17 - 9 < 10
#b
len(inventory) < 5*len(fullname)
#c
c < 24
#d
a < 6.75 < b
#e
len(last) < len(first) < len(middle)
#f
len(inventory) == 0 or len(inventory) < 10

#Exercise 2.18
#a
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
#b
'potato' in flowers
#c
flowers.append('thorny')
#d
poisonous = [flowers[-1]]
#e
dangerous = [ poisonous[0], flowers[-1]]

#2.19
#a
0**2 + 0**2 < 10**2
#b
10**2 + 10** < 10**2
#c
6**2 + 6**2 < 10**2
#d
7**2 + 8**2 < 10**2

#2.20
import math

#a
radiansA = (math.pi*75)/180; lenghtA = 16/ math.sin(radiansA); 
#b
radiansB = (math.pi*0)/180; lenghtB = 20/ math.sin(radiansB); 
#c
radiansC = (math.pi*45)/180; lenghtC = 24/ math.sin(radiansC); 
#d
radiansD = (math.pi*80)/180; lenghtD = 24/ math.sin(radiansD); 

#2.21
s = 'top'
s = s[-1] + s[-2] + s[-3]

#2.22
s = 'Angelo Vila'

#2.23
lst = [3, 7, -2, 12]
range = max(lst) - min(lst)

#2.24
#a

#2.25
#a
0 == (1 == 2)
#b
2 + (3 == 4) + 5 == 7
#c
(1 < -1) == (3>4)

#2.26
import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
s.bye()

