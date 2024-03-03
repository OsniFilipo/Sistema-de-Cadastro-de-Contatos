class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome  # Define o nome do contato
        self.telefone = telefone  # Define o telefone do contato
        self.email = email  # Define o email do contato

class Agenda:
    def __init__(self):
        self.contatos = []  # Inicializa uma lista vazia para armazenar os contatos

    def adicionar_contato(self, contato):
        self.contatos.append(contato)  # Adiciona o novo contato à lista de contatos
        print("Contato adicionado com sucesso.")  # Informa ao usuário que o contato foi adicionado com sucesso

    def listar_contatos(self):
        if self.contatos:  # Verifica se há contatos na lista
            print("Lista de Contatos:")
            for contato in self.contatos:  # Itera sobre os contatos na lista
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")  # Exibe os detalhes do contato
        else:
            print("A agenda de contatos está vazia.")  # Informa ao usuário que a agenda de contatos está vazia

def main():
    agenda = Agenda()  # Cria uma instância da classe Agenda para representar a agenda de contatos

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu

        if escolha == "1":
            nome = input("Digite o nome do contato: ")  # Solicita ao usuário o nome do novo contato
            telefone = input("Digite o telefone do contato: ")  # Solicita ao usuário o telefone do novo contato
            email = input("Digite o email do contato: ")  # Solicita ao usuário o email do novo contato
            novo_contato = Contato(nome, telefone, email)  # Cria um novo objeto Contato com os dados fornecidos
            agenda.adicionar_contato(novo_contato)  # Adiciona o novo contato à agenda
        elif escolha == "2":
            agenda.listar_contatos()  # Lista os contatos armazenados na agenda
        elif escolha == "3":
            print("Encerrando o programa...")  # Informa ao usuário que o programa será encerrado
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")  # Informa ao usuário que a opção escolhida é inválida

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
