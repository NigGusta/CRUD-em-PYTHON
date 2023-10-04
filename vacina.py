# pip install mysql-connector-python
import mysql.connector
import datetime

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bdi"
    )

# Função para criar um novo registro em VACINA
def create(nome, fabricante, lote, tempoImunidade, estoque, validade):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade) VALUES (%s, %s, %s, %s,%s,%s)"
        data = (nome, fabricante, lote, tempoImunidade, estoque, validade)

        cursor.execute(sql, data)
        connection.commit()

        userid = cursor.lastrowid

        print(
            f"Registro criado com sucesso. ID: {userid}, Nome: {nome}, Fabricante: {fabricante}, Lote: {lote}, Tempo de Imunidade: {tempoImunidade}, Estoque: {estoque}, Validade: {validade}")

        return userid
    finally:
        cursor.close()
        connection.close()

# Função para ler uma linha inteira em VACINA com base no ID
def buscaPorId(id):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT * FROM vacina WHERE id = %s"

        cursor.execute(sql, (id,))
        result = cursor.fetchone()

        if result:
            return result  # Retorna a linha completa se encontrada
        else:
            return None  # Retorna None se nenhum registro for encontrado com o ID especificado
    finally:
        cursor.close()
        connection.close()

# Função para atualizar um registro em VACINA --------------- AJEITAR
def update(id, nome=None, fabricante=None, lote=None, tempoImunidade=None, estoque=None, validade=None):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        # Crie uma lista para atualizações de colunas e uma lista para manter os valores a serem atualizados
        updates = []
        values = []

        if nome is not None:
            updates.append("nome = %s")
            values.append(nome)

        if fabricante is not None:
            updates.append("fabricante = %s")
            values.append(fabricante)

        if lote is not None:
            updates.append("lote = %s")
            values.append(lote)

        if tempoImunidade is not None:
            updates.append("tempoImunidade = %s")
            values.append(tempoImunidade)

        if estoque is not None:
            updates.append("estoque = %s")
            values.append(estoque)

        if validade is not None:
            updates.append("validade = %s")
            values.append(validade)

        if not updates:
            return 0

        # Construa a consulta SQL com base nas atualizações
        sql = f"UPDATE vacina SET {', '.join(updates)} WHERE id = %s"
        values.append(id)

        cursor.execute(sql, tuple(values))
        connection.commit()

        records_affected = cursor.rowcount

        if records_affected > 0:
            print(
                f"Registro atualizado com sucesso. ID: {id}")
            print(buscaPorId(id))
        return records_affected
    
    finally:
        cursor.close()
        connection.close()

# Função para excluir um registro
def delete(id):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "DELETE FROM vacina WHERE id = %s"
        data = (id,)

        cursor.execute(sql, data)
        connection.commit()

        records_affected = cursor.rowcount

        return records_affected
    finally:
        cursor.close()
        connection.close()

# Método para buscar por nome
def buscaPorNome(nome):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT * FROM vacina WHERE nome = %s"

        cursor.execute(sql, (nome,))
        results = cursor.fetchall()

        if results:
            for registro in results:
                print(registro)  # Imprime cada registro encontrado
        else:
            print("Nenhum registro encontrado com o nome especificado.")
    finally:
        cursor.close()
        connection.close()

# Método para buscar por fabricant
def buscaPorFab(fabricante):
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT * FROM vacina WHERE fabricante = %s"

        cursor.execute(sql, (fabricante,))
        results = cursor.fetchall()

        if results:
            for registro in results:
                print(registro)  # Imprime cada registro encontrado
        else:
            print("Nenhum registro encontrado com o fabricante especificado.")
    finally:
        cursor.close()
        connection.close()

# metodo pra listar todos os objetos da tabela
def exibeTudo():
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT * FROM vacina"

        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            for registro in results:
                print(registro)  # Imprime cada registro encontrado
        else:
            print("Nenhum registro encontrado com o nome especificado.")
    finally:
        cursor.close()
        connection.close()
        
# metodo pra encontrar lotes de vacinas perto do vencimento
def baixoEstoque():
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT nome, lote, estoque FROM vacina WHERE estoque < 10"

        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            for registro in results:
                print("-----------------------------------")
                print(registro)  # Imprime cada registro encontrado
                print("-----------------------------------")
        else:
            print("Nenhum lote acabando.")
    finally:
        cursor.close()
        connection.close()

def vencimentoProximo():
    try:
        x=90
        connection = conectar_banco()
        cursor = connection.cursor()

        # Obtenha a data atual
        data_atual = datetime.date.today()

        # Calcule a data de vencimento dentro dos próximos dias
        data_prox_vencimento = data_atual + datetime.timedelta(days=x)

        # Consulta SQL para selecionar vacinas com data de validade dentro dos próximos dias
        sql = "SELECT * FROM vacina WHERE validade BETWEEN %s AND %s"
        data_inicio = data_atual.strftime("%Y-%m-%d")
        data_fim = data_prox_vencimento.strftime("%Y-%m-%d")

        cursor.execute(sql, (data_inicio, data_fim))
        results = cursor.fetchall()

        if results:
            print("Vacinas próximas à data de vencimento:")
            for registro in results:
                print(registro)  # Exibe cada registro encontrado
        else:
            print("Nenhuma vacina próxima à data de vencimento encontrada.")

    finally:
        cursor.close()
        connection.close()

def totalEstoque():
    try:
        connection = conectar_banco()
        cursor = connection.cursor()

        sql = "SELECT nome, fabricante, estoque FROM vacina"

        cursor.execute(sql)
        vacinas = cursor.fetchall()

        if vacinas:
            total_stock = 0
            for vacina in vacinas:
                nome, fabricante, estoque = vacina
                total_stock += estoque
                print(f"Vacina: {nome} - {fabricante} ::::: Estoque: |{estoque}|")

            print(f"Quantidade total de estoque disponível: {total_stock}")
        else:
            print("Nenhuma vacina cadastrada.")

    finally:
        cursor.close()
        connection.close()

def exibir_menu():
    print("\nMENU:")
    print("1. Criar registro de vacina")
    print("2. Atualizar registro de vacina")
    print("3. Excluir registro de vacina")
    print("4. Buscar por nome")
    print("5. Buscar por fabricante")
    print("6. Visualizar toda a tabela de vacinas")
    print("7. Encontrar lotes de vacinas perto do vencimento")
    print("8. Calcular a quantidade total de estoque de vacinas")
    print("9. Encontrar as vacinas com data de vencimento em 30 dias")
    print("10. Sair")


while True:
    exibir_menu()
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome da vacina: ")
        fabricante = input("Digite o fabricante da vacina: ")
        lote = input("Digite o lote da vacina: ")
        tempoImunidade = input(
            "Digite o tempo de imunidade da vacina (em meses): ")
        estoque = input("Digite o estoque da vacina: ")
        validade = input(
            "Digite a validade da vacina (no formato YYYY-MM-DD): \n")

        create(nome, fabricante, lote, tempoImunidade, estoque, validade)

    elif opcao == "2":
        id = input("Digite o ID do registro a ser atualizado: ")
        nome = input(
            "Digite o novo nome da vacina (ou pressione Enter para manter o mesmo): ")
        fabricante = input(
            "Digite o novo fabricante da vacina (ou pressione Enter para manter o mesmo): ")
        lote = input(
            "Digite o novo lote da vacina (ou pressione Enter para manter o mesmo): ")
        tempoImunidade = input(
            "Digite o novo tempo de imunidade da vacina (ou pressione Enter para manter o mesmo): ")
        estoque = input(
            "Digite o novo estoque da vacina (ou pressione Enter para manter o mesmo): ")
        validade = input(
            "Digite a nova validade da vacina (no formato YYYY-MM-DD, ou pressione Enter para manter a mesma): ")

        # Define como None se a entrada for vazia, caso contrário, usa a entrada fornecida
        #nome = None if nome == "" else nome
        #fabricante = None if fabricante == "" else fabricante
        #lote = None if lote == "" else lote
        #tempoImunidade = None if tempoImunidade == "" else tempoImunidade
        #estoque = None if estoque == "" else estoque
        #validade = None if validade == "" else validade
        
        if nome == "" : nome="none"
        if fabricante == "" : nome="none"
        if lote == "" : nome="none"
        if tempoImunidade == "" : nome="none"
        if estoque == "" : nome="none"
        if validade == "" : nome="none"

        records_affected = update(
            id, nome, fabricante, lote, tempoImunidade, estoque, validade)

        if records_affected > 0:
            print(f"Registro atualizado com sucesso. ID: {id}")
            print("Campos atualizados:")
            if nome is not None:
                print(f"nome = {nome}")
            if fabricante is not None:
                print(f"fabricante = {fabricante}")
            if lote is not None:
                print(f"lote = {lote}")
            if tempoImunidade is not None:
                print(f"tempoImunidade = {tempoImunidade}")
            if estoque is not None:
                print(f"estoque = {estoque}")
            if validade is not None:
                print(f"validade = {validade}")

    elif opcao == "3":
        id = input("Digite o ID do registro a ser excluído: ")
        delete(id)

    elif opcao == "4":
        nome = input("Digite o nome da vacina para buscar: ")
        buscaPorNome(nome)

    elif opcao == "5":
        fabricante = input("Digite o fabricante da vacina para buscar: ")
        buscaPorFab(fabricante)

    elif opcao == "6":
        exibeTudo()

    elif opcao == "7":
        baixoEstoque()

    elif opcao == "8":
        totalEstoque()

    elif opcao == "9":
        vencimentoProximo()

    elif opcao == "10":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.")

