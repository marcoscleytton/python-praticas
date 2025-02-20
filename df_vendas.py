import pandas as pd

# Carregar os dados
df = pd.read_csv('vendas.csv')

# Converter a coluna 'Data da Venda' para o formato datetime
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])

# Criar uma coluna para representar o mês da venda
df['Mês'] = df['Data da Venda'].dt.month

# Calcular a quantidade total vendida por mês
quantidade_vendida = df.groupby('Mês')['Quantidade Vendida'].sum()

# Calcular o valor total arrecadado por mês
df['Valor Total'] = df['Quantidade Vendida'] * df['Preço Unitario']
valor_total = df.groupby('Mês')['Valor Total'].sum()

# Calcular o preço médio dos produtos vendidos por mês
preco_medio = df.groupby('Mês')['Preço Unitario'].mean()

# Criar um DataFrame com os resultados
relatorio = pd.DataFrame({
    'Quantidade Vendida': quantidade_vendida,
    'Valor Total Arrecadado': valor_total,
    'Preço Médio': preco_medio
})

# Exibir o relatório
print(relatorio)
