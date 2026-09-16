# CardioIA — Fase 5
## Assistente Cardiológico Inteligente: Experiência do Paciente

Projeto acadêmico desenvolvido para a Fase 5 da FIAP.

---

# 1. Visão geral

A Fase 5 amplia o projeto CardioIA com recursos de interação conversacional,
processamento de informações clínicas simuladas e automação de dados.

O projeto está organizado em três frentes principais:

- Assistente conversacional com IBM Watson Assistant
- Interface Web integrada ao IBM Watson Web Chat
- Recursos adicionais dos módulos IR ALÉM 1 e IR ALÉM 2

Os dados clínicos utilizados nos testes são simulados e possuem finalidade
exclusivamente acadêmica.

---

# 2. IBM Watson Assistant

Foi configurado um assistente denominado:

CardioIA

O assistente utiliza um fluxo conversacional desenvolvido no IBM Watson
Assistant.

## 2.1 Intents configurados

Foram configurados os seguintes intents:

- #saudacao
- #sintomas
- #duracao_sintoma
- #pressao_arterial
- #frequencia_cardiaca
- #exame_ecg
- #orientacao
- #despedida

## 2.2 Entidades

Foram utilizadas entidades para reconhecimento de informações relacionadas
ao contexto cardiológico.

Entre elas está:

@medida_cardiaca

Valores relacionados:

- frequencia
- pressão

Exemplos de termos utilizados:

- frequência cardíaca
- batimentos
- bpm
- batimento cardíaco
- pressão
- pressão arterial
- minha pressão

## 2.3 Nós do diálogo

O fluxo conversacional contempla:

1. Saudação
2. Identificação de sintomas
3. Registro da duração
4. Pressão arterial
5. Frequência cardíaca
6. Exame ECG
7. Orientação
8. Despedida

Também foi configurado tratamento para entradas não reconhecidas utilizando
anything_else.

---

# 3. Testes do IBM Watson

Foram realizados testes utilizando o recurso Try it out do IBM Watson
Assistant.

Exemplos registrados:

## Sintomas

Entrada:

Estou com palpitações

Reconhecimento:

#sintomas

## Pressão arterial

Entrada:

Minha pressão está 120 por 80

Reconhecimento:

#pressao_arterial

Entidade:

@medida_cardiaca:pressão

## Frequência cardíaca

Entrada:

Minha frequência está em 110 bpm

Reconhecimento:

#frequencia_cardiaca

Entidade:

@medida_cardiaca:frequencia

## ECG

Entrada:

Como funciona o ECG?

Reconhecimento:

#exame_ecg

## Despedida

Entrada:

Obrigado pela ajuda

Reconhecimento:

#despedida

## Entrada não reconhecida

Entrada:

Quero saber sobre futebol

Reconhecimento:

anything_else

---

# 4. Interface Web

Foi criada uma interface Web para disponibilizar o assistente por meio do
IBM Watson Web Chat.

Arquivo:

frontend/index.html

O código de incorporação foi obtido na integração Web chat do IBM Watson
Assistant e inserido na página HTML.

## 4.1 Execução local

A interface pode ser executada com:

python -m http.server 8000 --bind 127.0.0.1

A aplicação pode ser acessada em:

http://127.0.0.1:8000

## 4.2 Teste da interface

O Web Chat foi carregado com sucesso na página local.

O botão do assistente foi exibido e as mensagens enviadas pela interface
foram processadas pelo IBM Watson Assistant.

---

# 5. IR ALÉM 1
## IA Generativa e Extração de Informações Clínicas

O IR ALÉM 1 implementa um fluxo acadêmico de processamento de texto clínico
simulado.

## 5.1 Entrada

Arquivo:

ir_alem1/entrada_clinica.txt

Exemplo:

O paciente relata palpitações há aproximadamente 30 minutos.
Informa frequência cardíaca de 110 bpm e pressão arterial de
150/95 mmHg. Faz uso de medicamento para pressão.

## 5.2 Estrutura esperada

As informações são organizadas nos campos:

- sintomas
- pressao_arterial
- frequencia_cardiaca
- duracao
- medicamentos
- observacoes

## 5.3 Implementação

Arquivo principal:

ir_alem1/ai_generativa.py

O módulo possui funções para:

- criação do prompt estruturado;
- definição dos campos esperados;
- validação da estrutura;
- conversão da resposta JSON em estrutura Python.

## 5.4 Saída

Arquivo:

ir_alem1/saida_clinica.json

A saída representa as informações clínicas de forma estruturada.

## 5.5 Testes

Arquivo:

ir_alem1/teste_ir_alem1.py

Resultado confirmado:

4 testes aprovados.

4 passed in 0.09s

---

# 6. IR ALÉM 2
## Automação Inteligente com RPA, IA e Dados Híbridos

O IR ALÉM 2 implementa um fluxo de automação utilizando banco relacional,
processamento automatizado, análise dos dados e armazenamento de eventos em
estrutura não relacional.

## 6.1 Banco relacional

Foi utilizado SQLite.

Arquivo:

database/database.py

A tabela dados_clinicos armazena:

- paciente
- pressão sistólica
- pressão diastólica
- frequência cardíaca
- adesão ao tratamento

## 6.2 Análise automatizada

Arquivo:

backend/ai_analysis.py

O módulo identifica possíveis situações de atenção com base nos dados
clínicos simulados.

São avaliados:

- frequência cardíaca;
- pressão arterial;
- adesão ao tratamento.

## 6.3 Automação RPA

Arquivo:

backend/automation.py

O processo automatizado:

1. consulta o banco relacional;
2. obtém os dados clínicos;
3. executa a análise;
4. identifica alertas;
5. registra o resultado;
6. grava o evento no armazenamento não relacional.

## 6.4 Banco não relacional

Foi utilizada uma estrutura baseada em JSON.

Arquivo:

backend/cardioia_nosql.json

Os eventos armazenados incluem:

- tipo;
- origem;
- paciente;
- pressão;
- frequência cardíaca;
- adesão;
- status;
- alertas;
- data e hora.

## 6.5 Testes

Arquivo:

tests/test_ai_analysis.py

Foram executados 5 testes automatizados.

Cenários:

- paciente normal;
- frequência cardíaca elevada;
- pressão arterial elevada;
- baixa adesão;
- múltiplos alertas.

Resultado:

5 testes aprovados.

## 6.6 Relatório técnico

O projeto possui relatório técnico específico do IR ALÉM 2 em:

docs/

O relatório documenta arquitetura, implementação, testes, rastreabilidade e
evidências do funcionamento do fluxo.

---

# 7. Estrutura do projeto

FASE5/
├── backend/
│   ├── ai_analysis.py
│   ├── automation.py
│   ├── cardioia_nosql.json
│   └── nosql.py
│
├── database/
│   ├── database.py
│   └── cardioia.db
│
├── docs/
│   ├── ir_alem1/
│   │   └── README.md
│   ├── watson/
│   │   └── README.md
│   └── README_FASE5.md
│
├── frontend/
│   └── index.html
│
├── ir_alem1/
│   ├── ai_generativa.py
│   ├── entrada_clinica.txt
│   ├── saida_clinica.json
│   └── teste_ir_alem1.py
│
├── tests/
│   └── test_ai_analysis.py
│
├── main.py
├── README.md
└── requirements.txt

---

# 8. Tecnologias utilizadas

- Python
- SQLite
- JSON
- pytest
- IBM Watson Assistant
- IBM Watson Web Chat
- HTML
- JavaScript

---

# 9. Execução

## IR ALÉM 1

python .\ir_alem1\ai_generativa.py

Testes:

python -m pytest .\ir_alem1\teste_ir_alem1.py

## IR ALÉM 2

python main.py

Testes:

python -m pytest

## Interface Web

cd .\frontend
python -m http.server 8000 --bind 127.0.0.1

Acesso:

http://127.0.0.1:8000

---

# 10. Organização e versionamento

O projeto está versionado em Git e publicado no GitHub.

A Fase 5 mantém separadas suas estruturas de:

- backend;
- banco de dados;
- interface;
- testes;
- documentação;
- módulos IR ALÉM.

---

# 11. Considerações acadêmicas

O CardioIA apresentado nesta fase é um protótipo acadêmico.

Os dados clínicos utilizados nos testes são simulados.

O sistema não constitui diagnóstico médico e não substitui avaliação de
profissional de saúde.

---

# 12. Status

## Concluído

- Configuração do IBM Watson Assistant
- Intents e entidades
- Fluxo conversacional
- Tratamento anything_else
- Integração do Web Chat com página HTML
- IR ALÉM 1 com implementação e testes
- IR ALÉM 2 com RPA, IA e dados híbridos
- Testes automatizados
- Documentação dos componentes

## Pendências finais

- Integração adicional entre backend Python e o assistente, caso seja
  exigida como comunicação direta pela avaliação.
- Evidências/documentação final da entrega.
- Vídeo demonstrativo solicitado na atividade.

---

# 13. Conclusão

A Fase 5 do CardioIA reúne uma camada conversacional baseada em IBM Watson
Assistant, uma interface Web com Web Chat, processamento estruturado de
informações clínicas simuladas e um fluxo de automação utilizando dados
relacionais e não relacionais.

Os componentes implementados possuem testes automatizados e documentação
correspondente, permitindo a reprodução do projeto em ambiente local.
