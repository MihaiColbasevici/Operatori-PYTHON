num = int(input("Dați un număr mai mic de 10,000 \n"))
print("Ultima cifră a acestui număr este ", num % 10)
rest = num % 10
num = num // 10
print("Penultima cifră a acestui număr este ", num % 10)
num = num * 10 + rest
print("Restul împărțirii lui", num, "la 9 este ", num % 9)
print("Câtul împărțirii lui", num, "la 9 este ", num //9)
suma = 0
for cif in str(num) :
  suma = suma + int(cif)
print("Suma cifrelor lui", num, "va fi egală cu ", suma)