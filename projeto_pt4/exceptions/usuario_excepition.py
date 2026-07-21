class UsuarioException(Exception): #tratamentos especifico de erros no sistema relacionado a user

    """classe base para exeções relacionadas ao usuario.""" # = docstrings,(anotacao),
    #documentam pra q serve modulos,classes, metodo e funçõens; podem, ser acessadas 
    # pelo atributo; " atributo.__doc__ "

    pass #permite a definicao da classe sem implementacao adicional


#class UsuarioSistema:
#   def __init__(self):
#       self.arquivo = 'projeto_pt4/dados/usuario.json' #caminho para o arquivo JSON
#       self.criar_arquivo() #garante que o arquivo exista
#       self.usuarios = self.ler_usuarios() #carrega usuarios do arquivo
#por algum motivo quando esta parte nao esta o programa consegue rodar; aparentemente ele esta puxando 
# o arquivo do " usuarioSistema.py " mas nao era para estar puxando


class ArquivoNaoEncontradoException(UsuarioException):
    """exceção para quando o arquivo de usuarios não é encontrado."""
    def __init__(self):
        super().__init__("o arquivo de usuario nao foi encontrado. verifique o caminho se esta " \
        "correto.")
class UsuarioInvalidoException(UsuarioException):
    """exceção para quando o indice do usuario é invalido."""
    def __init__(self):
        super().__init__("indice de usuario invalido. escolha um numero valido.")
class ErroDeDecodificacaoException(UsuarioException):
    """excecao para o erro ao decodificar o JSON do arquivo usuarios."""
    def __init__(self):
        super().__init__("Erro ao decodificar o arquivo JSON. Verifique se o arquivo esta"
        " corrompido")
class EntradaInvalidaException(UsuarioException):
    """excecão para quando a entrada do usuario é invalida (não é um numero)."""
    def __init__(self):
        super().__init__("Entrada invalida. por favor, digite um numero")