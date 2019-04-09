import os, threading

def cls():
	os.system("cls")

global n1, n2, n3, n4, n5, n6, n7, n8, n9, n10

cls()

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0

val = 0
co = 9999

last_p = []

y = open("AllPhon.txt", "w")
y.write(" ")
y.close()

while True:
	n1 = int(n1)
	n2 = int(n2)
	n3 = int(n3)
	n4 = int(n4)
	n5 = int(n5)
	n6 = int(n6)
	n7 = int(n7)
	n8 = int(n8)
	n9 = int(n9)
	n10 = int(n10)

	n1 += 1

	if n1 == 10:
		n2 += 1
		n1 -= 10

	if n2 == 10:
		n3 += 1
		n2 -= 10

	if n3 == 10:
		n4 += 1
		n3 -= 10

	if n4 == 10:
		n5 += 1
		n4 -= 10

	if n5 == 10:
		n6 += 1
		n5 -= 10

	if n6 == 10:
		n7 += 1
		n6 -= 10

	if n7 == 10:
		n8 += 1
		n7 -= 10

	if n8 == 10:
		n9 += 1
		n8 -= 10

	if n9 == 10:
		n10 += 1
		n9 -= 10

	if n10 == 10:
		n10 -= 10


	n1 = str(n1)
	n2 = str(n2)
	n3 = str(n3)
	n4 = str(n4)
	n5 = str(n5)
	n6 = str(n6)
	n7 = str(n7)
	n8 = str(n8)
	n9 = str(n9)
	n10 = str(n10)
	val = int(val)

	p_num = "(" +n1+n2+n3+ ") - " +n4+n5+n6+ " - " +n7+n8+n9+n10
	if p_num not in last_p:
		last_p.append(p_num[:])

		y = open("AllPhon.txt", "a")
		y.write("			"+p_num)

		val = str(val)
		p1 = threading.Thread(target=print, args=(p_num,))
		p2 = threading.Thread(target=print, args=(val))

		p1.start()
		p2.start()

		p1.join()
		p2.join()
		val = int(val)
		if val >= co:
			cls()
			co += 9999

		val += 1