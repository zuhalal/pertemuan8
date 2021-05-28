#rekursi?
#Fungsi yang memanggil dirinya sendiri 

#Secara matematis, fungsi faktorial dapat didefinisikan:
#n! = n x (n – 1) x (n – 2) x  . . . . . .  x 2 x 1

#Secara rekursif, fungsi faktorial dapat didefinisikan:*
#n! = n x (n – 1)!

def faktorial(num): # header fungsi faktorial

    # 0! atau 1! mengembalikan 1
    if (num == 0) or (num == 1): #BASE CASE
        return 1

    # untuk num > 1, gunakan rekursi
    return num * faktorial(num-1) #RECURSION CASE

#Ingat fungsi power tadi?
def pangkat(num, n):

    # base case: num pangkat 0 hasilnya 1
    if n == 0:
        return 1

    # recursion case
    return num * pangkat(num, n-1)

#menghitung total nilai dari sebuah list
def sum(lst):

	if len(lst)==1:
		return lst[0]
	else:
		return lst[0] + sum(lst[1:])

#palindrom
def palindrom(a_str):

	if len(a_str)==0:
		return True
	elif len(a_str)==1:
		return True
	else:
		if a_str[0]==a_str[-1]:
			return palindrom(a_str[1:-1])
		else:
			return False

#Rekursi butuh BASE Case jika tidak akan terjadi stackoverlow error
