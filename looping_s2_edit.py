f1 = open('r1_list.txt', 'r')
f2 = open('r2_list.txt', 'r')

f1_line = f1.readline()
f2_line = f2.readline()

line_no = 1
while f1_line != '' or f2_line != '':
	f1_line = f1_line.rstrip()
	f2_line = f2_line.rstrip()


	if f1_line != f2_line:
		a_test = f1_line[10:17]
		print(a_test)
		b_test = f2_line[10:17]
		print(b_test)
		
		#print("this is: " + f1_line + "\n" + "this is: " + f2_line)
	print()

	# If a line does not exist on file1 then mark the output with + sign
	# if f1_line == '' and f2_line != '':
	# 	print("<+", "Line-%d" % line_no, f2_line)
 #        # otherwise output the line on file2 and mark it with < sign
	# elif f2_line != '':
	# 	print("<", "Line-%d" % line_no, f2_line)
	# print()

	f1_line = f1.readline()
	f2_line = f2.readline()
	line_no += 1

f1.close()
f2.close()