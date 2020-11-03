print('------------------------')
print('SISTEMA DE MONITORAMENTO DE MACACOS')
print('------------------------')
print("Indique se o macaco está sorrindo.")
print("Digite S para sim e N para não.")

macaco1_sorrindo = input("Macaco 1 está sorrindo?:")
macaco2_sorrindo = input("Macaco 2 está sorrindo?:")

if macaco1_sorrindo == macaco2_sorrindo :
  print("Em sincronia")
else:
  print("Fora de sincronia")