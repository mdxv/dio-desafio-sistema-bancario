import textwrap

def menu():

  menu = """ ━━━━━━━━━━━━━━━ MENU ━━━━━━━━━━━━━━━
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nu]\tNovo Usuário
  [nc]\tNova Conta
  [lc]\tListar Contas
  [q]\tSair
  >> """
  return input(menu)

def banner_sistema():
  banner = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        SISTEMA BANCÁRIO.py         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
  return print(banner)

def banner_extrato():
  banner = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          EXTRATO DA CONTA          ┃
"""
  return print(banner)

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    print(f"[✓] Depósito de R$ {valor:.2f} realizado com sucesso!\n")
    extrato += f"\tDepósito: R$ {valor:.2f}\n"
  else:
    print("[!] Operação falhou! Informe um valor válido.")
  
  return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  if valor > saldo:
    print("[!] Operação falhou! Você não tem saldo suficiente.")

  elif valor > limite:
    print("[!] Operação falhou! O valor do saque excede o limite.")

  elif numero_saques >= limite_saques:
    print("[!] Operação falhou! Número máximo de saques excedido.")

  elif valor > 0:
    saldo -= valor
    print(f"[✓] Saque de R$ {valor:.2f} realizado com sucesso!\n")
    extrato += f"\tSaque: R$ {valor:.2f}\n"
    numero_saques += 1

  else:
    print("[!] Operação falhou! Informe um valor válido.")

  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  if extrato:
    banner_extrato()
    print(extrato)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
  else:
    banner_extrato()
    print(" [!] Não foram realizadas movimentações.")
    print("\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

  print(f"\nSaldo: R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
  cpf = input("\n[+] Informe o CPF (somente números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("[!] Já existe um usuário com esse CPF!")
    return

  nome = input("[+] Informe o nome completo: ")
  data_nascimento = input("[+] Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("[+] Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print("[✓] Usuário criado com sucesso!\n")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("\n[+] Informe o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("[✓] Conta criada com sucesso!\n")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  print("[!] Usuário não encontrado, fluxo de criação de conta encerrado!\n")

def listar_contas(contas):
  banner = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         CONTAS CADASTRADAS         ┃"""
  print(banner)
  for conta in contas:
    linha = f"""
    Agência:\t{conta['agencia']}
    C/C:\t\t{conta['numero_conta']}
    Titular:\t{conta['usuario']['nome']}\n"""

  print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
  print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  
  
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  banner_sistema()

  while True:

    opcao = menu()


    match (opcao):
      case "d":
        valor = float(input("\n[+] Informe o valor do depósito: R$"))
        saldo, extrato = depositar(saldo, valor, extrato)

      case "s":
        valor = float(input("\n[-] Informe o valor do saque: R$"))
        
        saldo, extrato = sacar(
          saldo=saldo,
          valor=valor,
          extrato=extrato,
          limite=limite,
          numero_saques=numero_saques,
          limite_saques=LIMITE_SAQUES
        )

      case "e":
        exibir_extrato(saldo, extrato=extrato)

      case "nu":
        criar_usuario(usuarios)

      case "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
          contas.append(conta)
      
      case "lc":
        listar_contas(contas)

      case "q":
        break
      case _:
        print("\n[!] Operação inválida, por favor selecione novamente a operação desejada.\n")


if __name__ == "__main__":
  main()