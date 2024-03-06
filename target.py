'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def verifica_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Loop para gerar a sequência de Fibonacci até o número exceder o valor informado
    while b < numero:
        # Verifica se o número informado pertence à sequência de Fibonacci
        if b == numero:
            return True
        # Calcula o próximo número na sequência de Fibonacci
        a, b = b, a + b
    
    # Se o número não for encontrado na sequência, retorna False
    return False

# Função principal para entrada de usuário e verificação
def main():
    # Solicita ao usuário que informe um número para verificar se pertence à sequência de Fibonacci
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    # Verifica se o número informado pertence à sequência de Fibonacci e exibe uma mensagem correspondente
    if verifica_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

# Chama a função principal
if __name__ == "__main__":
    main()

"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""

import json

def carregar_faturamento_mensal(faturamento_mensal.json):
    with open(arquivoname, 'r') as faturamento_mensal.json:
        faturamento_mensal = json.load(faturamento_mensal.json)
    return faturamento_mensal

def calcular_estatisticas_faturamento(faturamento_diario):
    # Remove os valores de faturamento diário iguais a zero (dias sem faturamento)
    faturamento_diario = [valor for valor in faturamento_diario if valor > 0]
    
    # Calcula o menor e o maior valor de faturamento diário
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    
    # Calcula a média mensal de faturamento (desconsiderando os dias sem faturamento)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    # Calcula o número de dias em que o faturamento diário foi superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

# Função principal para entrada de usuário e cálculo de estatísticas
def main():
    # Carrega os dados de faturamento mensal a partir de um arquivo JSON
    faturamento_mensal = carregar_faturamento_mensal("faturamento_mensal.json")
    
    # Calcula as estatísticas de faturamento
    menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas_faturamento(faturamento_mensal)
    
    # Exibe os resultados
    print("Menor valor de faturamento diário:", menor_valor)
    print("Maior valor de faturamento diário:", maior_valor)
    print("Número de dias com faturamento diário superior à média mensal:", dias_acima_da_media)

# Chama a função principal
if __name__ == "__main__":
    main()

 """   4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

def calcular_percentual_faturamento(faturamento_estados):
    # Calcula o total do faturamento mensal da distribuidora
    total_faturamento = sum(faturamento_estados.values())
    
    # Calcula o percentual de representação de cada estado
    percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_estados.items()}
    
    return percentuais

# Função principal para cálculo dos percentuais
def main():
    # Dicionário com o valor de faturamento mensal por estado
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    # Calcula os percentuais de representação de cada estado
    percentuais = calcular_percentual_faturamento(faturamento_estados)
    
    # Exibe os resultados
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# Chama a função principal
if __name__ == "__main__":
    main()

""""5) Escreva um programa que inverta os caracteres de um string."""

    def inverter_string(string):
    # Inicializa uma string vazia para armazenar o resultado invertido
    string_invertida = "Beatriz"
    
    # Itera sobre os caracteres da string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Adiciona o caractere atual à string invertida
        string_invertida += string[i]
    
    return string_invertida

# Função principal para entrada de usuário e inversão da string
def main():
    # Solicita ao usuário que informe uma string
    string = input("Informe uma string para inverter: ")
    
    # Inverte a string utilizando a função definida
    string_invertida = inverter_string(string)
    
    # Exibe a string invertida
    print("String invertida:", string_invertida)

# Chama a função principal
if __name__ == "__main__":
    main()
