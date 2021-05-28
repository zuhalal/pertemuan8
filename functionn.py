#warming up
# print("Hello, Andi!") 
# print("Hello, Budi!")
# print("Hello, Cici!") 

#Why Function?
#Fungsi di dalam python didekralasikan dengan def
#Fungsi mengurangi repetisi dalam program yang kita buat dengan sifat fungsi yang resuable di dalam program
#fungsi dapat memakai parameter ataupun tidak sesuai dengan kebutuhan
# def hello_name(name):
#     print("Hello " + name)

# hello_name("Andi")


#more  function?
# def factorial(n): 
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result #return digunakan jika ingin mengembalikan nilai suatu fungsi

#sekarang kita panggil fungsinya
# print(factorial(3))
# print(factorial(5))
# print(factorial(6))

#tanpa fungsi? contoh 3 factorial, bayangkan jika kode tersebut direpetisi untuk factorial 5 dan 6 kode dalam program akan panjang
# result = 1
# for i in range(1,3+1):
#     result *= i
# print(result)

# #return vs no return
# def hello_name1(name):
#     print("Hello " + name)

# def hello_name2(name):
#     return "Hello " + name

# hello_name2("Andi")
# hello_name1("Andi")

# print(hello_name1("Andi"))
# print(hello_name2("Andi"))

# #multiple return statements
# def power(a, n): 

#     res = 1
#     for i in range(abs(n)):
#         res *= a
#     if n >= 0:
#         return res
#     else:
#         return 1 / res

# power(2.5,3)
# print(power(2.5,3))

#default value
# def hi(name = "Stranger"):
#     print("Hi, " + name + "!")
# hi()

#scoping
# x = "Hello, Python!"
# def fun():
#     x = 5
#     print(f"Inside 'fun', x has the value {x}")

# fun()
# print(f"Outside 'fun', x has the value {x}")


#more scoping
# x = 5
# def fun(y):
#     y = 7
#     print(y)

# fun(x)
# print(x)

#overriding global vars
# def f():
#     s = "Oh, no :("
#     print(s)

# s = "Can't wait for pre-midterm quiz!"
# f()

