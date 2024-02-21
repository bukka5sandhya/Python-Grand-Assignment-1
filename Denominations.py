N = int(input()) #8593(input)
thousand = int(N/1000)
a = str(thousand)
remaining =  N%1000

five = int(remaining/500)
b= str(five)
remaining_1 = remaining%500 

hundred = int(remaining_1 /100)
c = str(hundred)
remaining_2 = remaining_1%100

fifty = int(remaining_2/50)
d = str(fifty)
remaining_3 = remaining_2%50 

twenty = int(remaining_3/20)
e = str(twenty)
remaining_4 = remaining_3%20 

five = int(remaining_4 /5)
f = str(five)
remaining_5 = remaining_4%5 

one = str(remaining_5)
print("1000:"+a)
print("500:"+b)
print("100:"+c)
print("50:"+d)
print("20:"+e)
print("5:"+f)
print("1:"+one)
