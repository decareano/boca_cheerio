f1=open("r1_list.txt","r")
f2=open("r2_list.txt","r")
for line1 in f1:
   for line2 in f2:
      if line1 == line2:
         print("cannot match")
      else:
         print(line1 + line2)
      break
f1.close()
f2.close()
