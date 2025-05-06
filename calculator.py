a=0
b=0
def somme(a,b):
    sum = a+b
    return sum

def soustract(a,b):
    sous = a-b
    return sous

def divide(a,b):
    div = a/b
    return div


def multiplicator(a,b):
    mult = a*b
    return mult

a=1
b=2
sum_res=somme(a,b)
sous_res=soustract(a,b)
mult_res=multiplicator(a,b)
div_res=divide(a,b)
print(f"************la somme de {a} et {b} est {sum_res}********************la soustraction de {a} et {b} est {sous_res}********" \
f"************la division de {a} et {b} est {div_res}********************" \
f"la multiplication de {a} et {b} est {mult_res}" )

