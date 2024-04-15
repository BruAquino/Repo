class contaBancaria:
    def __init__(self, titular, saldo, numero, limite = 0):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.numero = numero
        self.estatusConta = False

    def saque(self, saldo):
        valorSaque = float(input("informe o valor do saque."))
        if  saldo >= valorSaque:
            saldo = saldo - valorSaque
            print ("Saque realizado com sucesso.")
        else:
            print ("O valor do saque desejado é superior ao seu saldo.")

    def depositar(self, saldo):
        valorDeposito = float(input("informe o valor do depósito."))
        saldo = saldo + valorDeposito
        print("Depósito realizado com sucesso.")


    def verificarSaldo(self, saldo):
        print(f"O valor do seu saldo é:", saldo)

    def bloqueio(self, estatusConta):
        if estatusConta == False:
            estatusConta = False
        else:
            estatusConta = True

    def mudarLimite(self, mudarLimite):
        mudarLimite = float(input("Digite o valor que você deseja alterar o limite."))
        limite = mudarLimite
        print("O valor do seu limite agora é:", limite)
