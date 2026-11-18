# =====================================================================
# CITIZEN ASSIST AI - PROTÓTIPO DE ASSISTENTE DIGITAL DE ORIENTAÇÃO CIDADÃ
# Global Solution 2026.2 - FIAP
# Aluna: Camila Kato de Godoi | RM: 570229
# =====================================================================

import json
import os
import time
import difflib

# Localiza automaticamente a pasta raiz do projeto ('Citizen-Assist-AI')
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_BASE = os.path.join(DIRETORIO_RAIZ, "data", "base.json")

# Memória simples para guardar o último assunto pesquisado pelo usuário
contexto_usuario = {
    "ultimo_tema": None,
    "ultima_busca": None
}


def carregar_base():
    """Lê o arquivo JSON e trata erros caso ele não exista ou esteja vazio."""
    if not os.path.exists(CAMINHO_BASE):
        print("\n[ERRO] Arquivo 'data/base.json' não encontrado!")
        return []

    try:
        with open(CAMINHO_BASE, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados if isinstance(dados, list) else []
    except Exception as e:
        print(f"\n[ERRO] Não foi possível ler a base de dados: {e}")
        return []


def buscar_por_pergunta(pergunta_usuario, base_conhecimento):
    """Procura orientações por palavras-chave, usando memória e tolerância a erros."""
    global contexto_usuario
    pergunta_limpa = pergunta_usuario.lower().strip()

    if not pergunta_limpa:
        return []

    # Se a pessoa digitar uma pergunta muito curta (ex: "como renovar"), lembra o último tema
    if len(pergunta_limpa.split()) <= 2 and contexto_usuario["ultimo_tema"]:
        pergunta_limpa += f" {contexto_usuario['ultimo_tema']}"

    resultados = []
    for item in base_conhecimento:
        pontos = 0
        for kw in item["palavras_chave"]:
            if kw.lower() in pergunta_limpa:
                pontos += 1

        if pontos > 0:
            resultados.append((item, pontos))

    resultados.sort(key=lambda x: x[1], reverse=True)

    # Se achou uma resposta direta
    if resultados:
        contexto_usuario["ultimo_tema"] = resultados[0][0]["tema"]
        contexto_usuario["ultima_busca"] = pergunta_usuario
        return [r[0] for r in resultados]

    # Se não achou direto, tenta ver se a pessoa digitou alguma palavra parecida (ex: "erge" -> "rg")
    todas_palavras = []
    mapa_palavras = {}
    for item in base_conhecimento:
        for kw in item["palavras_chave"]:
            todas_palavras.append(kw.lower())
            mapa_palavras[kw.lower()] = item

    for palavra in pergunta_limpa.split():
        parecidas = difflib.get_close_matches(palavra, todas_palavras, n=1, cutoff=0.6)
        if parecidas:
            sugestao = parecidas[0]
            item_sugerido = mapa_palavras[sugestao]
            print(f"\n[🔊 SISTEMA]: Acho que você quis dizer algo sobre '{item_sugerido['tema']}' ({sugestao.upper()}).")
            confirmacao = input("Está correto? Digite 1 para SIM ou 2 para NÃO: ").strip()
            if confirmacao == "1":
                contexto_usuario["ultimo_tema"] = item_sugerido["tema"]
                return [item_sugerido]
            else:
                print("\nEntendido! Vamos tentar por outro caminho.")
                return []

    return []


def exibir_orientacao_acessivel(item):
    """Mostra a resposta de forma clara, simples e com a fonte oficial."""
    print("\n---------------------------------------------------------------------")
    print(f"📌 TEMA: {item['tema'].upper()}")
    print("🔊 [LEITURA EM VOZ ALTA DISPONÍVEL]")
    print(f"💡 O QUE FAZER: {item['orientacao']}")
    print(f"🔗 FONTE CONSULTADA: {item['fonte']}")
    print(f"📅 DATA DE VERIFICAÇÃO: {item['data_verificacao']}")
    print("⚠️ AVISO: Este serviço é gratuito e informativo. Não informe senhas a ninguém!")
    print("---------------------------------------------------------------------")


def menu_acessivel_idosos(base_conhecimento):
    """Menu simplificado com números grandes e ícones para facilitar a navegação."""
    print("\n=====================================================================")
    print("   🔊 MODO NAVEGAÇÃO FACILITADA E ACESSÍVEL (IDOSOS / LEITURA)")
    print("=====================================================================")
    print("Escolha o assunto digitando apenas o NÚMERO:")
    print("  [ 1 ] 📄 DOCUMENTOS (RG, CPF, CNH, Passaporte, CTPS)")
    print("  [ 2 ] 🏥 SAÚDE E POSTO (Cartão SUS, Remédios, Vacinas)")
    print("  [ 3 ] 💡 CONTAS E SERVIÇOS (Água, Luz, INSS, Agendamentos)")
    print("  [ 4 ] 🌳 BAIRRO E RUA (Lixo, Árvores, Procon, Iluminação)")
    print("  [ 0 ] ⬅️ Voltar ao menu principal")

    op = input("\nDigite o número da opção (1, 2, 3, 4 ou 0): ").strip()

    mapeamento = {
        "1": "Documentação",
        "2": "Serviços",
        "3": "Serviços",
        "4": "Orientações Comunitárias"
    }

    if op in mapeamento:
        tema_escolhido = mapeamento[op]
        itens = [it for it in base_conhecimento if it["tema"] == tema_escolhido]
        print(f"\n--- ORIENTAÇÕES SOBRE: {tema_escolhido.upper()} ---")
        for item in itens:
            exibir_orientacao_acessivel(item)
    elif op != "0":
        print("\n⚠️ Opção inválida. Digite apenas 1, 2, 3, 4 ou 0.")


def rodar_bateria_de_testes(base_conhecimento):
    """Executa 15 cenários de teste alinhados com os 15 registros da base."""
    print("\n=====================================================================")
    print("      EXECUTANDO BATERIA DE TESTES AUTOMATIZADOS (15 CENÁRIOS)")
    print("=====================================================================")

    perguntas_teste = [
        {"q": "Como faço para tirar a segunda via do RG?", "esperado_id": 1},
        {"q": "Preciso regularizar meu CPF", "esperado_id": 2},
        {"q": "Quais os passos para renovação da CNH?", "esperado_id": 3},
        {"q": "Como solicitar o passaporte na polícia federal?", "esperado_id": 4},
        {"q": "Onde baixo a carteira de trabalho digital?", "esperado_id": 5},
        {"q": "Como fazer o cartão do SUS no posto de saúde?", "esperado_id": 6},
        {"q": "Segunda via da conta de água", "esperado_id": 7},
        {"q": "Como fazer a troca de titularidade da conta de luz?", "esperado_id": 8},
        {"q": "Como funciona o agendamento no poupatempo?", "esperado_id": 9},
        {"q": "Como consultar meu extrato no meu inss?", "esperado_id": 10},
        {"q": "Que dia passa a coleta seletiva de lixo no bairro?", "esperado_id": 11},
        {"q": "Onde tem campanha de vacinação de gripe?", "esperado_id": 12},
        {"q": "Como pedir poda de árvore na rua?", "esperado_id": 13},
        {"q": "Como comprar um carro financiado?", "esperado_id": None},  # Fora do escopo
        {"q": "   ", "esperado_id": None}  # Entrada vazia
    ]

    acertos = 0
    total = len(perguntas_teste)
    tempos = []

    for idx, teste in enumerate(perguntas_teste, 1):
        inicio = time.time()
        res = buscar_por_pergunta(teste["q"], base_conhecimento)
        fim = time.time()

        tempo_ms = (fim - inicio) * 1000
        tempos.append(tempo_ms)

        id_obtido = res[0]["id"] if res else None

        if id_obtido == teste["esperado_id"]:
            status = "ACERTO"
            acertos += 1
        else:
            status = "DIVERGÊNCIA"

        q_texto = teste["q"].strip() if teste["q"].strip() else "[Entrada Vazia]"
        print(f"Teste #{idx:02d} | Pergunta: '{q_texto}' -> {status} ({tempo_ms:.2f} ms)")

    taxa_acerto = (acertos / total) * 100
    tempo_medio = sum(tempos) / total

    print("---------------------------------------------------------------------")
    print("📊 RESUMO DOS INDICADORES DE DESEMPENHO:")
    print(f"  • Total de cenários testados: {total}")
    print(f"  • Acertos (incluindo retenções corretas): {acertos}")
    print(f"  • Taxa de Acerto: {taxa_acerto:.1f}%")
    print(f"  • Tempo Médio de Resposta: {tempo_medio:.3f} ms")
    print("---------------------------------------------------------------------\n")


def menu():
    base_conhecimento = carregar_base()
    if not base_conhecimento:
        return

    while True:
        print("\n=====================================================================")
        print("          CITIZEN ASSIST AI - ORIENTAÇÃO CIDADÃ E INCLUSIVA          ")
        print("=====================================================================")
        print("1. Consultar por Pergunta em Texto (Com Memória de Contexto)")
        print("2. Modo de Navegação Acessível por Ícones (Idosos e Leitura)")
        print("3. Executar Bateria de Testes Automáticos (15 Cenários)")
        print("0. Sair do Sistema")

        opcao = input("\nEscolha a opção desejada: ").strip()

        if opcao == "1":
            pergunta = input("\nDigite sua dúvida sobre documentos ou serviços públicos: ").strip()
            if not pergunta:
                print("\n⚠️ Nenhuma pergunta foi digitada. Tente novamente.")
                continue

            resultados = buscar_por_pergunta(pergunta, base_conhecimento)
            if resultados:
                exibir_orientacao_acessivel(resultados[0])
            else:
                print("\n⚠️ AVISO: Não encontramos essa orientação exata na nossa base.")
                print("Lembre-se: O assistente não inventa respostas e não substitui o atendimento oficial.")

        elif opcao == "2":
            menu_acessivel_idosos(base_conhecimento)

        elif opcao == "3":
            rodar_bateria_de_testes(base_conhecimento)

        elif opcao == "0":
            print("\nObrigado por utilizar o Citizen Assist AI. Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida! Digite 1, 2, 3 ou 0.")


if __name__ == "__main__":
    menu()