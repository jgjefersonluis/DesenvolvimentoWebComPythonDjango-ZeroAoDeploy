def divisao(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print('Forneça um número diferente de zero!')
    except TypeError:
        print('Forneça um número.')

print(divisao(12, 2))
print(divisao(12, 0))
print(divisao(12, '5'))

