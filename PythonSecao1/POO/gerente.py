from POO.funcionario import Funcionario


class Gerente(Funcionario):

    def __init__(self, nome, endereco, cpf, data_nascimento, cargo, matricula, senha, salario, qtd_funcionarios):
        super().__init__(nome, endereco, cpf, data_nascimento, cargo, matricula, senha, salario)
        self._qtd_funcionarios == qtd_funcionarios

    def calcular_gratificacao(self):
        return self._salario * 0.15

