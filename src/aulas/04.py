class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'


class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'

# Métodos de classe
print(Funcionario.prefixo)
print(Funcionario.info())

# Métodos estáticos
print(FolhaDePagamento.log())