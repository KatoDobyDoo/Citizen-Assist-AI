# Relatório de Uso Crítico e Responsável de Inteligência Artificial

**Aluna:** Camila Kato de Godoi  
**RM:** 570229 | **Turma:** 1CCOA — FIAP  

---

## 1. Ferramentas Utilizadas
No desenvolvimento do projeto *Citizen Assist AI*, utilizei ferramentas de Inteligência Artificial generativa (Gemini) como apoio técnico e organizacional nas seguintes etapas:
* Auxílio na estruturação inicial dos 15 registros de orientação cidadã em formato JSON.
* Revisão de boas práticas para tratamento de exceções (`try/except`) e manipulação de caminhos relativos de arquivos (`os.path`) em Python.
* Apoio na revisão ortográfica e organização dos tópicos da documentação em Markdown e do roteiro do vídeo.

---

## 2. Validação Crítica e Ajustes Autorais
Todas as sugestões geradas pela IA passaram por revisão, teste e validação humana antes de serem incorporadas ao repositório:
* **Verificação das Fontes Oficiais:** Cada uma das 15 orientações foi conferida manualmente em portais governamentais reais (`gov.br`, `poupatempo.sp.gov.br`, Receita Federal, Detran e Meu INSS) para garantir que nenhuma informação inventada fosse incluída na base.
* **Adequação ao Nível Acadêmico:** O código-fonte em `src/sistema.py` foi ajustado para utilizar exclusivamente estruturas e bibliotecas compatíveis com o conteúdo estudado nas fases do curso (listas, dicionários, leitura de JSON e `difflib`), garantindo total domínio e compreensão sobre cada linha escrita.
* **Ajuste dos Testes Automatizados:** A bateria de testes foi calibrada para cobrir os 15 cenários correspondentes aos registros da base, validando na prática a taxa de acerto e o tempo de resposta no terminal do PyCharm.
* **Foco em Privacidade e Acessibilidade:** Foram adicionadas travas lógicas e avisos explícitos para garantir que o sistema não colete dados pessoais e ofereça navegação simplificada por ícones para idosos.