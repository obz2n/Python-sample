'''
Desafio:
Validador de senhas

Problema:
você trabalha em um sistema que precisa verificar se todas as senhas digitadas
por usuário são válidas

Para uma senha ser válida, ela precisa ter pelo menos 10 caracteres. Dentro desses caracteres, é necessário ter no minimo um caractere especial, uma letra maiuscula e um numero
'''
# Funções de validação
def tem_comprimento_minimo(senha, min_len=10):
    return len(senha) >= min_len

def tem_caractere_especial(senha):
    return any(c in "!@#$%^&*()-+" for c in senha)

def tem_letra_maiuscula(senha):
    return any(c.isupper() for c in senha)

def tem_numero(senha):
    return any(c.isdigit() for c in senha)

def validar_senha(senha):
    if not tem_comprimento_minimo(senha):
        return False, "Senha deve ter pelo menos 10 caracteres."
    if not tem_caractere_especial(senha):
        return False, "Senha deve conter pelo menos um caractere especial."
    if not tem_letra_maiuscula(senha):
        return False, "Senha deve conter pelo menos uma letra maiúscula."
    if not tem_numero(senha):
        return False, "Senha deve conter pelo menos um número."
    return True, "Senha válida.

# Exceção personalizada
class SenhaInvalidaError(Exception):
    pass

# Classe Gerenciador de Senhas
class GerenciadorSenhas:
    def __init__(self):
        self.senha = None

    def criar_senha(self):
        while True:
            senha_usuario = input('Digite a sua senha: ')
            valido, mensagem = validar_senha(senha_usuario)
            if valido:
                self.senha = senha_usuario
                print('Senha criada com sucesso!')
                break
            else:
                print(mensagem)

# Parte da Execução
if __name__ == "__main__":
    gerenciador = GerenciadorSenhas()
    gerenciador.criar_senha()
