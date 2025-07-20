class BaseDeConhecimento:
    def __init__(self):
        self.fatos = []
        self.regras = []

    def adicionar_fato(self, fato):
        self.fatos.append(fato)

    def adicionar_regra(self, condicao, conclusao):
        self.regras.append((condicao, conclusao))

class SistemaEspecialista:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

    def inferir(self):
        novos_fatos = True
        while novos_fatos:
            novos_fatos = False
            for condicao, conclusao in self.base_conhecimento.regras:
                if all(fato in self.base_conhecimento.fatos for fato in condicao):
                    if conclusao not in self.base_conhecimento.fatos:
                        self.base_conhecimento.fatos.append(conclusao)
                        novos_fatos = True

# Criando a base de conhecimento
base = BaseDeConhecimento()

# Adicionando fatos
base.adicionar_fato("infecção respiratória")
base.adicionar_fato("dificuldade para respirar")

# Adicionando regras
base.adicionar_regra(["febre alta", "tosse"], "infecção respiratória")
base.adicionar_regra(["infecção respiratória", "dificuldade para respirar"], "pneumonia")

# Criando o sistema especialista
sistema = SistemaEspecialista(base)

# Executando a inferência
sistema.inferir()

# Exibindo os fatos atualizados
print("Fatos inferidos:")
print(base.fatos)