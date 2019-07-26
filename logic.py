a = 10
b = 20
output = (a<5) and (b>10) #conditional without 'if'
print(output)
#conditional with IF-ELSE
output = (a<5) or (b>10)
if output:
   print("Output is True")
else:
   print("Output is False")
#Nested IF
if b > 10:
   print("b > 10")
   if a == 10:
      print(" a = 10")
   else:
      print(" a <> 10")
elif b > 5: #use elif for else if
   print("b > 5")
else:
   print("b < 10")
# if in one row
if a>5 : print("Single Line IF. a > 5 ")