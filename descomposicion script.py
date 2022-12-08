import sys
if len(sys.argv) == 2:
    num = int(sys.argv[1])
    if num > 0:
        chain = str(num)
        long = len(chain)
        for i in range(len(chain)):
            print(f'{int(chain[long-1-i])*10**i:04d}')
    else:
        print('El número a ingresar debe ser positivo.')
else:
    print('Debe ingresar sólo un número.')