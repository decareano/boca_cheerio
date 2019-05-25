def file_len(fname):
   with open(fname) as f:
      for i, l in enumerate(f):
         pass
   return i + 1

print(file_len("r1_list.csv"))
print(file_len("r2_list.csv"))