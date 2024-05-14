"""
Fuel Gauge

In a file called fuel.py, implement a program that prompts the user for a
fraction, formatted as X/Y, wherein each of X and Y is an integer, and then
outputs, as a percentage rounded to the nearest integer, how much fuel is in
the tank. If, though, 1% or less remains, output E instead to indicate that the
tank is essentially empty. And if 99% or more remains, output F instead to
indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead
prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch
any exceptions like ValueError or ZeroDivisionError.
"""

if __name__ == "__main__":
    while True:
        frac = input("Fraction: ").strip()
        
        numer, denom = frac.split('/')
        
        try:
            res = int(numer) / int(denom)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        
        if res > 1:
            continue
        
        break
    
    if res == 1:
        print('F')
    elif res == 0:
        print('E')
    else:
        print(f'{int(res * 100)}%')
    