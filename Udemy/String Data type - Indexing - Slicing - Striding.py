s = "Python Sample String"
#print(s[7:10])
print(s[:6])
#print(s[7:])

#Stride
#print(s[::3])
#print(s[::-1])
#print(s[::-2])

#itera por cada caracter
#for value in s:
#	print(value)
#itera por cada dos caracteres
#for value in s[::2]:
#	print(value)

#help(str)
#print(dir(str))

##Funcion : "format"

num1 = 100
num2 = 200
#print("Value of num1 is",num1,"Value of num2 is",num2)
#print("Value of num1 is {1} value of num2 {0}".format(num1,num2))
#print("Value of num1 is {val2} value of num2 {val1}".format(val1=num1,val2=num2))

s = "python sample string"

#se asigna a s1 un nuevo string
#s1 = s.capitalize()
#print(s1)

#upper
#lower
#title

#print(s.upper())
#print(s.lower())
#print(s.title())

#islower
#istitle
#isupper

##Funciones : "split,join"
s = "HTML,CSS,PYTHON,JAVA,Django"
l = s.split(",")
print(l)

s1 = (" ").join(l)
print(s1)

s1 = "abcd"
s2 = "1234"

s3 = "Python Sample string abcd "

##Funciones : "maketrans,tranlate"

#table = str.maketrans(s1,s2)
#result = s3.translate(table)
#print(result)

##Funciones : "index,find,rfind"

s = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))
#print(s.index("python"))
print(s.find("python"))
print(s.find("PYTHON"))

print(s.rfind("PYTHON"))