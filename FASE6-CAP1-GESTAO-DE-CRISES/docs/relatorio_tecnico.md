# Relatório técnico — CAP1

O protótipo gera 5.000 registros sintéticos (seed 42) e treina Random Forest para prever `pico_risco`. A divisão estratificada é 70% treino, 15% validação e 15% teste. As métricas reais devem ser preenchidas após executar `python -m src.train_model`; não inserir números presumidos.

O fluxo previsto reúne Analista de Risco, Especialista em Protocolos, Planejador de Resposta e Orquestrador, com ferramentas determinísticas e envelope JSON v1.0. A versão atual é um scaffold de lógica local; a integração efetiva com OpenAI Agents SDK e handoffs ainda precisa ser completada e testada.

Limitações: dados sintéticos; `score_risco` não é necessariamente probabilidade calibrada; temperatura segue o enunciado (média 24, desvio 5, limites 10–40) e não entra no rótulo; o limiar de risco sistêmico alto não foi informado e permanece pendente. Não usar para decisões clínicas reais.

Completar com métricas verificadas, integrantes/RMs e revisão final antes da submissão.