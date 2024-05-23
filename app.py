import sqlite3

def criar_tabela_clientes():
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        );
    ''')

    conexao.commit()
    conexao.close()

def inserir_cliente(nome, email, telefone):
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
    ''', (nome, email, telefone))

    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print('Não há clientes cadastrados.')
    else:
        for cliente in clientes:
            print(f'ID: {cliente[0]}')
            print(f'Nome: {cliente[1]}')
            print(f'E-mail: {cliente[2]}')
            print(f'Telefone: {cliente[3]}')
            print()

    conexao.close()

def editar_cliente(id_cliente):
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,))
    cliente = cursor.fetchone()

    if cliente is None:
        print('Cliente não encontrado.')
    else:
        print(f'ID: {cliente[0]}')
        print(f'Nome: {cliente[1]}')
        print(f'E-mail: {cliente[2]}')
        print(f'Telefone: {cliente[3]}')
        print()

        # Solicita os novos dados do cliente
        nome = input('Digite o novo nome: ')
        email = input('Digite o novo e-mail: ')
        telefone = input('Digite o novo telefone: ')

        # Atualiza os dados do cliente no banco de dados
        cursor.execute('''
            UPDATE clientes
            SET nome = ?, email = ?, telefone = ?
            WHERE id = ?
        ''', (nome, email, telefone, id_cliente))
        conexao.commit()

        print('Cliente atualizado com sucesso.')

    conexao.close()

def excluir_cliente(id_cliente):
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,))
    cliente = cursor.fetchone()

    if cliente is None:
        print('Cliente não encontrado.')
    else:
        cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
        conexao.commit()
        print('Cliente excluído com sucesso.')

    conexao.close()

# Cria a tabela de clientes no banco de dados, se ela não existir
criar_tabela_clientes()

while True:
    print('\n--- MENU DE CLIENTES ---')
    print('1. Cadastrar um novo cliente')
    print('2. Listar todos os clientes')
    print('3. Editar um cliente existente')
    print('4. Excluir um cliente')
    print('0. Sair do programa')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        # Solicita os dados do novo cliente
        nome = input('Digite o nome do cliente: ')
        email = input('Digite o e-mail do cliente: ')
        telefone = input('Digite o telefone do cliente: ')

        # Insere o novo cliente no banco de dados
        inserir_cliente(nome, email, telefone)
        print('Cliente cadastrado com sucesso.')

    elif opcao == '2':
        # Lista todos os clientes cadastrados
        listar_clientes()

    elif opcao == '3':
        # Solicita o ID do cliente a ser editado
        id_cliente = input('Digite o ID do cliente a ser editado: ')
        editar_cliente(int(id_cliente))

    elif opcao == '4':
        # Solicita o ID do cliente a ser excluído
        id_cliente = input('Digite o ID do cliente a ser excluído: ')
        excluir_cliente(int(id_cliente))

    elif opcao == '0':
        # Sai do programa
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida. Por favor, tente novamente.')
