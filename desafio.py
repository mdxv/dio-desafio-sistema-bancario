banner_sistema = """
###########################
#   SISTEMA BANCÁRIO.py   #
###########################"""
banner_extrato = """
###########################
#     EXTRATO DA CONTA    #
"""

menu = """
Opções:
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
  
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(banner_sistema)

while True:

  opcao = input(menu)


  match (opcao):
    case "d":
      valor = float(input("[+] Informe o valor do depósito: R$"))
      if valor > 0:
        saldo += valor
        print(f"[✓] Depósito de R$ {valor:.2f} realizado com sucesso!")
        extrato += f"  Depósito: R$ {valor:.2f}\n"
      else:
        print("[!] Operação falhou! Informe um valor válido.")

    case "s":
      valor = float(input("[-] Informe o valor do saque: R$"))
      
      if valor > saldo:
        print("[!] Operação falhou! Você não tem saldo suficiente.")

      elif valor > limite:
        print("[!] Operação falhou! O valor do saque excede o limite.")

      elif numero_saques >= LIMITE_SAQUES:
        print("[!] Operação falhou! Número máximo de saques excedido.")

      elif valor > 0:
        saldo -= valor
        print(f"[✓] Saque de R$ {valor:.2f} realizado com sucesso!")
        extrato += f"  Saque: R$ {valor:.2f}\n"
        numero_saques += 1
      else:
        print("[!] Operação falhou! Informe um valor válido.")

    case "e":
      if extrato:
        print(banner_extrato)
        print(extrato)
        print("\n###########################")
      else:
        print("[!] Não foram realizadas movimentações.")

      print(f"\nSaldo: R$ {saldo:.2f}")

    case "q":
      break
    case _:
      print("Operação inválida, por favor selecione novamente a operação desejada.")
