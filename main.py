# 1-misol
kvadratlar = [x**2 for x in range(1, 11)]
print(kvadratlar)

# 2-misol
juft_sonlar = [x for x in range(1, 21) if x % 2 == 0]
print(juft_sonlar)

# 3-misol
toq_sonlar = [x for x in range(10, 31) if x % 2 != 0]
print(toq_sonlar)

# 4-misol
sozlar = ["apple", "banana", "pear"]
uzunliklar = [len(soz) for soz in sozlar]
print(uzunliklar)

# 5-misol
soz = "Soz"
harflar = [harf for harf in soz]
print(harflar)

# 6-misol
kublar = [x**3 for x in range(1, 5)]
print(kublar)

# 7-misol
matn = ["dog", "cat", "mouse"]
bosh_harflar = [soz[0].upper() for soz in matn]
print(bosh_harflar)

# 8-misol
sonlar = [-5, 3, -1, 0, 7, -2]
musbat_sonlar = [x for x in sonlar if x > 0]
print(musbat_sonlar)

# 9-misol
natija = ["juft" if x % 2 == 0 else "toq" for x in range(1, 11)]
print(natija)

# 10-misol
import math

kv_ildizlar = [math.sqrt(x) for x in range(1, 11)]
print(kv_ildizlar)
