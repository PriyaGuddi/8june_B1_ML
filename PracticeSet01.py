Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Question2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%3;print(a)
2
50
>>>
>>> True * False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and(7<4)or(18==3))and(9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
 File "<pyshell#13>", line 1, in <module>
   False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False)or(False>True))and(False<=True)
False
>>>
>>> #Question3
>>> s1="Nice to have it"
>>> s2="here"
>>> print(s1+' '+s2)
Nice to have it here
>>>
>>> #Question4
>>>
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> print(a[3][1][2])
['hello']
>>>
>>> #Question5
>>> s1="Nice to have it"
>>> s2="here"
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>>
>>> #Question6
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> print(color_list_1.difference(color_list_2))
{'Black', 'White'}
SyntaxError: invalid syntax
>>>
>>> #Question8
>>> print(eval("{0}+{0}{0}+{0}{0}{0}".format(int(input("Enter a number: ")))))
Enter a number: 5
615
>>> #Question9
>>> s=input("Enter a string")
Enter a stringwithout,hello,bag,world
>>> print(' '.join(sorted(s.split(','))))
bag hello without world
>>>
SyntaxError: invalid syntax
>>> #Question10
>>> 
d={'Student':['Rahul','Kishore','Vidhya','Rakhi'],'Marks':[57,87,67,79]}
>>> output=max(d['Marks'])
>>> print(output)
87
>>> pos=d['Marks'].index(output)
>>> print(pos)
1
>>> print(d['Student'][pos])
Kishore
>>> 
