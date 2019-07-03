op=input()
for i in range(0,len(op)):
   if(op[i].isalpha() and op[i].isdigit()):
    print("No")
else:
  print("Yes")
