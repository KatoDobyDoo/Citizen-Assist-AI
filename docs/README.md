# Citizen Assist AI — Assistente Digital de Orientação Cidadã e Inclusiva

**Global Solution — 2º Semestre de 2026 (Citizen Tech)**  
**Aluna:** Camila Kato de Godoi  
**RM:** 570229 | **Turma:** 1CCOA — FIAP  

---

## 1. Descrição do Problema e Público Beneficiado
Encontrar orientações confiáveis sobre serviços públicos e documentos cotidianos costuma ser difícil para o cidadão comum, principalmente para idosos e pessoas com baixo letramento digital. Instruções espalhadas em vários sites e cheias de termos complicados geram dúvidas, retrabalho e até riscos de golpes em sites não oficiais.

O **Citizen Assist AI** foi criado como um protótipo de assistente digital introdutório para facilitar esse acesso, organizando informações verificadas em linguagem simples, com foco em acessibilidade, transparência nas fontes e inclusão digital.

---

## 2. Estrutura da Base de Conhecimento e Busca
A base de conhecimento está armazenada no arquivo `data/base.json`, contendo **15 orientações verificadas** divididas em **3 grandes temas cidadãos**:
* **Documentação:** 2ª via de RG, regularização de CPF, renovação de CNH, Passaporte e Carteira de Trabalho Digital (CTPS).
* **Serviços:** Cartão SUS, 2ª via de conta de água, troca de titularidade de luz, agendamentos presenciais (Poupatempo) e consultas do INSS.
* **Orientações Comunitárias:** Coleta seletiva de lixo, campanhas de vacinação, solicitação de poda de árvores, reclamações no Procon e reparo de iluminação pública.

### Diferenciais de Implementação
* **Memória de Contexto Ativo:** O sistema guarda o último tema consultado na sessão para conseguir responder a perguntas complementares curtas (ex: *"como renovar?"*) sem obrigar o usuário a repetir todo o assunto.
* **Modo de Navegação Acessível (Idosos e Leitura):** Menu adaptado com números grandes e ícones visuais por categoria, acompanhado de indicação de leitura em voz alta e respostas diretas.
* **Tolerância a Erros de Digitação:** Uso da biblioteca nativa `difflib` para identificar termos parecidos (ex: *"erge"* $\rightarrow$ *"rg"*), perguntando ao usuário *"Acho que você quis dizer X. Está correto?"* antes de concluir a resposta.
* **Transparência e Limites:** Toda resposta exibe a fonte oficial consultada, a data da última verificação e um aviso claro de que o serviço é gratuito e não solicita dados pessoais.

---

## 3. Plano de Testes e Indicadores de Desempenho
O programa possui uma rotina de avaliação automatizada (Opção 3 do menu) que testa **15 cenários operacionais**, cobrindo os registros da base de dados, consultas fora de escopo e tratamento de entradas vazias.

### Métricas Obtidas nos Testes:
* **Total de Cenários Testados:** 15 situações (13 consultas diretas/reformulações + 2 testes de limitação/escopo).
* **Taxa de Acerto (Accuracy):** 100.0% (todos os registros localizados e retenções tratadas corretamente).
* **Tempo Médio de Consulta:** ~0.18 ms por requisição.

---

## 4. Como Executar o Projeto

### Pré-requisitos
* Python 3.x instalado na máquina (utiliza apenas bibliotecas padrão da linguagem: `json`, `os`, `time` e `difflib`).

### Execução no Terminal
```bash
python src/sistema.py