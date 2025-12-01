import matplotlib.pyplot as plt
import os
import json
from dotenv import load_dotenv

# Carrega variáveis
load_dotenv()
DB_CANDIDATOS = os.getenv("JSON_PATH_CANDIDATOS")

def finalizar_votacao():
    print("\n--- PROCESSANDO RESULTADOS ---")
    
    # 1. Carregar dados do JSON manualmente para garantir leitura pura
    if not os.path.exists(DB_CANDIDATOS):
        print("Erro: Arquivo de candidatos não encontrado.")
        return

    with open(DB_CANDIDATOS, 'r', encoding='utf-8') as f:
        dados_candidatos = json.load(f)

    # 2. Ordenar candidatos: Quem tem mais votos aparece primeiro
    # A função sorted com reverse=True coloca o maior no topo
    candidatos_ordenados = sorted(dados_candidatos, key=lambda x: x['votos'], reverse=True)

    # 3. Preparar listas para o Matplotlib
    # Vamos filtrar para não mostrar candidatos com 0 votos se quiser (opcional)
    # Aqui vou mostrar todos
    nomes = [c['nome'] for c in candidatos_ordenados]
    votos = [c['votos'] for c in candidatos_ordenados]
    partidos = [c['partido'] for c in candidatos_ordenados]
    
    total_votos = sum(votos)
    
    if total_votos == 0:
        print("Nenhum voto computado ainda. Impossível gerar gráfico.")
        return

    print(f"Total de votos computados: {total_votos}")
    print(f"Vencedor: {candidatos_ordenados[0]['nome']} com {candidatos_ordenados[0]['votos']} votos.")

    # ==========================================
    # GERANDO O GRÁFICO COM MATPLOTLIB
    # ==========================================
    
    # Definir tamanho da figura (Largura, Altura)
    plt.figure(figsize=(10, 6))

    # Lógica de Cores: Ouro para o 1º lugar, Azul padrão para o resto
    cores = ['#FFD700' if i == 0 else '#1f77b4' for i in range(len(candidatos_ordenados))]

    # Criar as barras
    barras = plt.bar(nomes, votos, color=cores, edgecolor='grey')

    # Títulos e Rótulos
    plt.title('Resultado Final das Eleições', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Quantidade de Votos', fontsize=12)
    plt.xlabel('Candidatos', fontsize=12)
    
    # Limpa as bordas superior e direita para visual mais limpo
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Adicionar o texto com a contagem e porcentagem em cima de cada barra
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        porcentagem = (altura / total_votos) * 100
        
        # Monta o texto. Ex: 
        # 150
        # (35.5%)
        texto = f"{altura}\n({porcentagem:.1f}%)"
        
        plt.text(
            barra.get_x() + barra.get_width() / 2, # Posição X (centro da barra)
            altura + 0.1,                          # Posição Y (um pouco acima da barra)
            texto,
            ha='center', va='bottom', fontsize=10, fontweight='bold'
        )

    # Adiciona o nome do partido no eixo X junto com o nome (Opcional, mas fica legal)
    labels_eixo_x = [f"{n}\n({p})" for n, p in zip(nomes, partidos)]
    plt.xticks(ticks=range(len(nomes)), labels=labels_eixo_x, rotation=0)

    # Ajusta o layout para nada ficar cortado
    plt.tight_layout()

    print("Gerando gráfico visual...")
    plt.show() # Abre a janela com o gráfico
