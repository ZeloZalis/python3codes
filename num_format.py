#print( "{:>30}".format("palabra") )
pal = "palabra"
print(f'{pal:>30}')
print(f'{pal:30}')
print(f'{pal:^10}')
print(f'{pal:^20}')
print(f'{pal:^30}')
print(f'{pal:^40}')
print(f'{pal:.3}')
print(f'{pal:>30.3}')
num1 = 10
num2 = 100
num3 = 1000
print(f'{num1:4d}')
print(f'{num2:4d}')
print(f'{num3:4d}')
#Formateo de números rellenado con 0
print(f'{num1:04d}')
print(f'{num2:04d}')
print(f'{num3:04d}')
#Formateo de números flotantes
numft1 = 3.1415926
numft2 = 153.21
print(f'{numft1:7.3f}')
print(f'{numft1:07.3f}')
print(f'{numft2:7.3f}')