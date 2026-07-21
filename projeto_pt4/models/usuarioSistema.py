import os
import json
from exceptions.usuario_excepition import *

class UsuarioSistema:
    def __init__(self):
        self.arquivo = 'projeto_pt4/dados/usuarios.json'  # Caminho para o arquivo JSON
        self.criar_arquivo()  # Garante que o arquivo exista
        self.usuarios = self.ler_usuarios()  # Carrega usuários do arquivo

    def criar_arquivo(self):
        # Cria a pasta 'dados' se não existir
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        
        # Cria o arquivo se não existir
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump([], f)  # Inicializa o arquivo como uma lista vazia

    def ler_usuarios(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError: #tratamento para arquivo nao encontrado
            raise ArquivoNaoEncontradoException() #lança exceção personalizada
        except json.JSONDecodeError: #tratamento para arquivo nao encontrado
            raise ErroDeDecodificacaoException() #lanca excecao personalizada

    def create(self):
        novo_usuario = input("Digite o nome do novo usuário: ")
        self.usuarios.append(novo_usuario)
        self.salvar_usuarios()  # Salva a lista atualizada no arquivo
        print(f"Usuário {novo_usuario} cadastrado com sucesso!")

    def read(self):
        print("Usuários cadastrados:")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")

    def update(self):
        self.read()  # Exibe a lista de usuários
        try:
            indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
            if 0 <= indice < len(self.usuarios):
                novo_nome = input(f"Digite o novo nome para {self.usuarios[indice]}: ")
                self.usuarios[indice] = novo_nome
                self.salvar_usuarios()  # Salva as alterações
                print(f"Usuário atualizado para {novo_nome} com sucesso!")
            else:
                raise UsuarioInvalidoException()
        except ValueError: #tratamento para entrada invalida
            raise EntradaInvalidaException() #lança excecao personalizada

    def delete(self):
        self.read()  # Exibe a lista de usuários
        try:
            indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
            if 0 <= indice < len(self.usuarios):
                removido = self.usuarios.pop(indice)
                self.salvar_usuarios()  # Salva as alterações
                print(f"Usuário {removido} excluído com sucesso!")
            else:
                raise UsuarioInvalidoException()
        except ValueError: #tratamento para entrada invalida
            raise EntradaInvalidaException() #lanca excecao personalizada
        
            
    def salvar_usuarios(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.usuarios, f, ensure_ascii=False)  # Salva a lista de usuários no arquivo
