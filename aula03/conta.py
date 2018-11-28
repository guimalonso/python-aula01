class Conta():
    '''Tentando abstrair uma conta corrente'''
    def __init__(self, n_cont, saldo=0):
        self.conta = n_cont
        self.saldo = saldo
        #print('método construtor')

    def sacar(self, valor:int) -> bool:
        '''Funcao para sacar o valor da conta'''
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta):
        try:
            if not self.sacar(valor):
                raise ValueError("Falha na transferencia")
            try:
                conta.depositar(valor)
            except AttributeError:
                print("Objeto destino nào possui o metodo depositar")
                self.depositar(valor)
        except Exception as e:
            print('Erro: {}'.format(e))

    def __str__(self):
        return 'Conta: {} Saldo: {}'.format(self.conta, self.saldo)

class Poupanca(Conta):
    '''classe poupança'''
    def __init__(self, n_cont, saldo=0):
        super().__init__(n_cont, saldo)
        self.taxa_juros = 0.005

    def render_juros(self):
        self.saldo += self.saldo * self.taxa_juros