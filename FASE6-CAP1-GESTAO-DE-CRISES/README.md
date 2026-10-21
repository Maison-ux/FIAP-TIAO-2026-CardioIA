# ❤️ CardioIA
>> ## Projeto FIAP – Inteligência Artificial
>> 
>> Projeto acadêmico desenvolvido no curso de **Inteligência Artificial da FIAP**, organizado em diferentes fases de desenvolvimento e evolução tecnológica.
>> 
>> ---
>> 
>> # 📚 Fases do Projeto
>> 
>> | Fase | Descrição |
>> |---|---|
>> | [FASE 1](./FASE1) | Desenvolvimento inicial do projeto |
>> | [FASE 2](./FASE2) | Evolução da solução e processamento inteligente |
>> | [FASE 3](./FASE3) | Continuidade do desenvolvimento |
>> | [FASE 4](./FASE4) | Classificação de arritmias cardíacas com CNN |
>> | [FASE 5](./FASE5/README.md) | Assistente Cardiológico Inteligente: Experiência do Paciente |
>> | ⭐ [FASE 6 — CAP1](./FASE6-CAP1-GESTAO-DE-CRISES/README.md) | Gestão de Crises com Sistema Preditivo em IA |
>> 
>> ---
>> 
>> # ⭐ FASE 6 — Coração Sob Controle
>> 
>> A Fase 6 amplia o CardioIA com um protótipo de **gestão de crises apoiado por Machine Learning, regras determinísticas e agentes inteligentes**.
>> 
>> O sistema utiliza dados sintéticos para identificar situações classificadas como pico de risco, consultar protocolos operacionais predefinidos e produzir uma resposta estruturada.
>> 
>> ### Principais componentes
>> 
>> - Geração de dados sintéticos;
>> - Modelo supervisionado Random Forest;
>> - Predição de pico de risco;
>> - Analista de Risco;
>> - Especialista em Protocolos;
>> - Planejador de Resposta;
>> - Orquestrador de agentes;
>> - OpenAI Agents SDK e configuração de handoffs;
>> - Ferramentas determinísticas para consulta de protocolos;
>> - Validação de entradas;
>> - Histórico de execução em memória;
>> - Respostas estruturadas em JSON;
>> - Testes automatizados;
>> - Documentação técnica.
>> 
>> ### Documentação da Fase 6
>> 
>> ➡️ **[README técnico e instruções de execução](./FASE6-CAP1-GESTAO-DE-CRISES/README.md)**
>> 
>> ➡️ [Relatório técnico — versão Markdown](./FASE6-CAP1-GESTAO-DE-CRISES/docs/relatorio_tecnico.md)
>> 
>> ➡️ [Arquitetura do sistema — versão Markdown](./FASE6-CAP1-GESTAO-DE-CRISES/docs/arquitetura.md)
>> 
>> ➡️ [Notebook de treinamento](./FASE6-CAP1-GESTAO-DE-CRISES/notebook_treinamento.ipynb)
>> 
>> ➡️ [Métricas do modelo](./FASE6-CAP1-GESTAO-DE-CRISES/artifacts/metricas.json)
>> 
>> ---
>> 
>> # 🫀 Sobre o CardioIA
>> 
>> O CardioIA é um projeto acadêmico voltado à aplicação de Inteligência Artificial em cenários relacionados à saúde cardiovascular.
>> 
>> Ao longo das fases, o projeto evolui desde o processamento de informações de ECG até o desenvolvimento de interfaces conversacionais, automação, classificação preditiva e coordenação de agentes inteligentes.
>> 
>> > **Aviso:** o CardioIA é um protótipo acadêmico. Os dados utilizados na Fase 6 são sintéticos e as previsões não representam probabilidades clínicas calibradas. O sistema não substitui avaliação, diagnóstico ou decisão de profissionais de saúde e não deve ser utilizado para decisões clínicas reais.
>> 
>> ---
>> 
>> # 👨‍💻 Integrantes
>> 
>> - **Maison Wendrel Bezerra Ramos** – RM: 565616
>> - **Ítalo Domingues** – RM: 561787
>> 
>> ---
>> 
>> # 👨‍🏫 Professores
>> 
>> ### Tutor(a)
>> 
>> - Caique Nonato da Silva Bezerra
>> 
>> ### Coordenador(a)
>> 
>> - André Godoi Chiovato
>> 
>> ---
>> 
>> # 🛠️ Tecnologias
>> 
>> - Python
>> - NumPy
>> - pandas
>> - Scikit-Learn
>> - Random Forest
>> - TensorFlow e Keras
>> - OpenAI Agents SDK
>> - JSON
>> - pytest
>> - Git
>> - GitHub
>> - Google Colab
>> 
>> ---
>> 
>> # 🔗 Repositório
>> 
>> [FIAP-TIAO-2026-CardioIA](https://github.com/Maison-ux/FIAP-TIAO-2026-CardioIA)
>> '@ | Set-Content -LiteralPath "$repo\README.md" -Encoding UTF8
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> 
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> 
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> # =====================================================
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> # README TÉCNICO DA FASE 6
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> # =====================================================
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> 
PS C:\Users\MAISO\FIAP-TIAO-2026-CardioIA> @'
>> # ❤️ CardioIA
>> ## Fase 6 — CAP1: Gestão de Crises com Sistema Preditivo em IA
>> 
>> **Tema:** Coração Sob Controle
>> 
>> Projeto acadêmico desenvolvido no curso de Inteligência Artificial da FIAP.
>> 
>> ---
>> 
>> # 🎯 Objetivo
>> 
>> Desenvolver um protótipo de gestão de crises utilizando Machine Learning, protocolos determinísticos e agentes inteligentes para analisar dados sintéticos, identificar situações de pico de risco e organizar respostas estruturadas.
>> 
>> O sistema reúne quatro papéis:
>> 
>> - **Orquestrador:** coordena o fluxo de processamento;
>> - **Analista de Risco:** utiliza o modelo de Machine Learning;
>> - **Especialista em Protocolos:** consulta as regras explícitas;
>> - **Planejador de Resposta:** organiza a síntese da resposta.
>> 
>> ---
>> 
>> # 🧠 Modelo de Machine Learning
>> 
>> O projeto utiliza um classificador **Random Forest** treinado com 5.000 registros sintéticos.
>> 
>> O treinamento utiliza divisão estratificada de:
>> 
>> - 70% para treino;
>> - 15% para validação;
>> - 15% para teste.
>> 
>> As métricas geradas são armazenadas em:
>> 
>> `artifacts/metricas.json`
>> 
>> O modelo serializado está em:
>> 
>> `artifacts/random_forest_cardioia.joblib`
>> 
>> As métricas representam somente o desempenho sobre dados sintéticos. Como o rótulo deriva de regras aplicadas às próprias variáveis sintéticas, os resultados não demonstram capacidade de previsão clínica real.
>> 
>> ---
>> 
>> # 🤖 Arquitetura multiagente
>> 
>> O fluxo planejado é:
>> 
>> ```text
>> Entrada do caso
>>       |
>>       v
>> Validação de entrada
>>       |
>>       v
>> Orquestrador
>>       |
>>       v
>> Analista de Risco
>>       |
>>       v
>> Ferramenta de previsão
>> (Random Forest)
>>       |
>>       v
>> Especialista em Protocolos
>>       |
>>       v
>> Consulta determinística
>> de protocolos
>>       |
>>       v
>> Planejador de Resposta
>>       |
>>       v
>> Resposta estruturada JSON
>> python -m venv .venv
>> .\.venv\Scripts\Activate.ps1
>> pip install -r requirements.txt
>> python -m pytest -q
>> python -m src.train_model
>> FASE6-CAP1-GESTAO-DE-CRISES/
>> ├── artifacts/
>> │   ├── metricas.json
>> │   └── random_forest_cardioia.joblib
>> ├── data/
>> │   └── dados_sinteticos.csv
>> ├── docs/
>> │   ├── arquitetura.md
>> │   ├── pendencias_entrega.md
>> │   └── relatorio_tecnico.md
>> ├── src/
>> │   ├── agents/
>> │   │   ├── analista.py
>> │   │   ├── especialista.py
>> │   │   └── planejador.py
>> │   ├── config.py
>> │   ├── contracts.py
>> │   ├── data_generator.py
>> │   ├── orchestrator.py
>> │   ├── tools.py
>> │   ├── train_model.py
>> │   └── validation.py
>> ├── tests/
>> │   └── test_validation.py
>> ├── notebook_treinamento.ipynb
>> ├── requirements.txt
>> └── README.md
>> 
>> ### 2. Confira o resultado
>> 
>> Depois que o terminal informar que os dois arquivos foram atualizados, execute:
>> 
>> ```powershell
>> Set-Location "C:\Users\MAISO\FIAP-TIAO-2026-CardioIA"
>> 
>> git diff --check
>> git status --short
>> 
