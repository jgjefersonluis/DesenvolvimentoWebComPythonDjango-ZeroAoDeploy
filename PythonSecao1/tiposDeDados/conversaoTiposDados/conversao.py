print(3.14, int(3.14))
print(3.9999, int(3.9999))       # Isto não arredonda até o inteiro mais próximo!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note que o resultado é mais próximo de zero

print("2345", int("2345"))        # interpreta a string para produzir um int
print(17, int(17))                # int inclusive funciona com inteiros!
print(int("23garrafas"))

print("123.45")
print(float("123.45"))
