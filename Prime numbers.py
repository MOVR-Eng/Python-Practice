for i in range(2,100):
 for x in range(2,int(i**0.5)+1):
  if i%x==0:
   break
 else:
    print(i)
