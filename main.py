#print [Ctrl + / to comment]
# print('hello world')
# country = input('enter the country : ')
# print('the entered value is ' + country)

#numbers
print('#numbers : ');
print(2+2)
print(2**3)
print(3//4)
print(4%3)
print(type(2*5))
print(type(3.01))
print(type(1>9))

print('\n#maths : ')
print(round(3.1))
print(abs(-31.2))

print('\n#binary : ')
print(bin(5))
print(int('0b101',2))

print('\n#variables : ')
a,b,c = 1,2,3
print(a)
print(b)
print(c)

print('\n#long strings : ')
long_str = '''
WOW
0 0
---
'''
print(long_str)

print('\n#formatted strings : ')
name = 'Johnny'
age = 45
print(f'New Style: Hi {name}. You are {age} years old')
print('Old Style: Hi {}. You are {} years old'.format(name,age))

print('\n#indexed access : ')
str_dex = '01234567'
#[start:stop:stepover]
print(str_dex[0:8] + ' ==> exclude stop')
print(str_dex[0:8:2] + ' ==> jump by 2')
print(str_dex[1:] + ' ==> start from 1')
print(str_dex[:5] + ' ==> stop at 5')
print(str_dex[::1] + ' ==> default behaviour')
print(str_dex[-1] + ' ==> last element')
print(str_dex[::-1] + ' ==> reverse string')
print(str_dex[::-2] + ' ==> reverse by 2')

print('\n#inbuilt functions vs methods : ')
test_str = 'this is a random string'
print(len(test_str)) #inbuilt
print(test_str.upper()) #method



      






