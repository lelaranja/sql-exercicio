import sqlite3

conexao = sqlite3.connect('bancoalunos')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
#cursor.execute('INSERT INTO alunos VALUES(1,"Leticia", 30, "Engenharia")')
#cursor.execute('INSERT INTO alunos VALUES(2,"Paloma", 30, "Dados")')
#cursor.execute('INSERT INTO alunos VALUES(3,"Alexandre", 22, "Design")')
#cursor.execute('INSERT INTO alunos VALUES(4,"Pedro", 31, "Farmácia")')
#cursor.execute('INSERT INTO alunos VALUES(5,"Aline", 28, "Arquitetura")')
#cursor.execute('INSERT INTO alunos VALUES(6,"Lucas", 20, "Engenharia")')

# 3.Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas: 
# a) Selecionar todos os registros da tabela "alunos".
#dado = cursor.execute('SELECT * FROM alunos')
#for alunos in dado:
#    print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dado = cursor.execute('SELECT nome, idade FROM alunos WHERE idade >20')
#for alunos in dado:
#    print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
#dado = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
#for alunos in dado:
#    print(alunos)
    
# d) Contar o número total de alunos na tabela
#dado = cursor.execute('SELECT COUNT(DISTINCT id) FROM alunos')
#for alunos in dado:
#    print(alunos)

# 4. Atualização e Remoção 
# a) Atualize a idade de um aluno específico na tabela
#cursor.execute('UPDATE  alunos SET idade = 26 WHERE nome ="Lucas"')

# b) Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos where id = 5')

# 5.Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) 
# e saldo (float). Insira alguns registros de clientes na tabela.
#cursor.execute('CREATE TABLE clientes(id_clientes INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

#cursor.execute('INSERT INTO clientes VALUES(1,"Maria", 35, 2350.50)')
#cursor.execute('INSERT INTO clientes VALUES(2,"Paloma", 30, 12500.45)')
#cursor.execute('INSERT INTO clientes VALUES(3,"Joelma", 45, 1534.11)')
#cursor.execute('INSERT INTO clientes VALUES(4,"Pedro", 31, 125.45)')


# 6.Consultas e Funções Agregadas
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
#dado = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for alunos in dado:
#    print(alunos)


# b) Calcule o saldo médio dos clientes
#dado = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for alunos in dado:
#    print(alunos)

# c) Encontre o cliente com o saldo máximo
#dado = cursor.execute('SELECT id, nome, MAX(saldo) FROM clientes')
#for alunos in dado:
#    print(alunos)

# d) Conte quantos clientes têm saldo acima de 1000
#dado = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
#for alunos in dado:
#    print(alunos)

# 7.Atualização e Remoção com Condições
#cursor.execute('UPDATE  clientes SET saldo = 2534.98 WHERE id_clientes =2')

# b) Remova um cliente pelo seu ID
#cursor.execute('DELETE FROM clientes where id_clientes = 4')

# 8. Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id 
# (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, 
# o produto e o valor de cada compra.

#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, produto VARCHAR(100), valor REAL, id_compras INT, FOREIGN KEY (id_compras) REFERENCES clientes (id_clientes))')

#cursor.execute('INSERT INTO compras VALUES(1,"Bicicleta", 850.00, 8)')
#cursor.execute('INSERT INTO compras VALUES(2,"Quebra-Cabeça", 82.00, 2)')
#cursor.execute('INSERT INTO compras VALUES(3,"Computador", 5400.00, 1)')
#cursor.execute('INSERT INTO compras VALUES(4,"Microfone", 154.00, 3)')


dado = cursor.execute('SELECT nome, produto, valor FROM clientes FULL JOIN compras ON clientes.id_clientes = compras.id_compras')
for usuario in dado:
    print(usuario)


conexao.commit()  # enviar a conexão
conexao.close  # fechar a conexão
