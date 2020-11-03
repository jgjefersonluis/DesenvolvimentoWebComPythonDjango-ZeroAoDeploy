print("-------------------------")
print("PET SHOP")
print("-------------------------")

atendimentos = int(input("Caes atendidos: "))
final_de_semana_usuario = input("Final de semana (S/N)?: ")
final_de_semana = final_de_semana_usuario == "S"

if final_de_semana:
  if atendimentos >= 20 and atendimentos <= 40:
    print("SUCESSO")
  else:
    print("FRACASSO")
else:
  if atendimentos >= 20 and atendimentos <= 30:
    print("SUCESSO")
  else:
    print("FRACASSO")