# Sistema de Gerenciamento de Vacinas 🦠💉

Este é um sistema simples de gerenciamento de vacinas, desenvolvido em Python, que permite criar, atualizar, excluir e consultar informações sobre vacinas em um banco de dados MySQL. Além disso, oferece funcionalidades adicionais, como busca por nome, fabricante, visualização de todo o estoque, identificação de lotes próximos ao vencimento e contagem total de estoque de vacinas.

## Requisitos 📋

- Python 3.x 🐍
- MySQL Server 🗄️
- Biblioteca `mysql-connector-python` 📚

## Configuração ⚙️

1. Instale a biblioteca `mysql-connector-python` executando o seguinte comando:

```shell
pip install mysql-connector-python
```

2. Configure as informações de conexão ao banco de dados no arquivo `main.py`. Você pode modificar as seguintes linhas para corresponder às suas configurações:

```python
host = "localhost"
user = "root"
password = ""
database = "bdi"
```

3. Execute o arquivo `main.py` para iniciar o sistema de gerenciamento de vacinas após baixar o BDI (Banco de Dados de Imunização). 💻

## Funcionalidades 🧰

1. **Criar registro de vacina:** Adicione informações sobre uma nova vacina, incluindo nome, fabricante, lote, tempo de imunidade, estoque e data de validade. 📝

2. **Atualizar registro de vacina:** Atualize as informações de uma vacina existente com base no ID. 🔄

3. **Excluir registro de vacina:** Remova um registro de vacina com base no ID. ❌

4. **Buscar por nome:** Localize vacinas pelo nome. 🔍

5. **Buscar por fabricante:** Encontre vacinas por fabricante. 🔍

6. **Visualizar toda a tabela de vacinas:** Exiba todos os registros de vacinas armazenados no banco de dados. 📊

7. **Encontrar lotes de vacinas perto do vencimento:** Identifique lotes de vacinas com estoque baixo. ⚠️

8. **Calcular a quantidade total de estoque de vacinas:** Obtenha a quantidade total de vacinas em estoque. 📈

9. **Encontrar as vacinas com data de vencimento em 30 dias:** Localize vacinas com data de vencimento nos próximos 30 dias. 📅

**Nota:** Certifique-se de que as informações de conexão ao banco de dados, como senha, sejam tratadas com segurança e não incluídas em repositórios públicos. Considere o uso de variáveis de ambiente ou arquivos de configuração separados para armazenar essas informações com segurança. 🔒

---
