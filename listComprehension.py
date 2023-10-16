li = [1,2,3,4,5]
mul = [i*3 for i in li if i%2!=0]
print(mul)

div  = [i if i%2==0  else 0 for i in li ]
print(div)