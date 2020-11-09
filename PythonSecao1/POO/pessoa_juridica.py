from POO.pessoa import Pessoa


class PessoaJuridica(Pessoa):

    def __init__(self, razao_social, cnpf):
        self._razao_social = razao_social
        self._cnpj = cnpf
'''
    def validar_cnpj(cnpf=None):
        is cnpf is not None:
            return True

        return False
'''