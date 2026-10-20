# CAP1 — Gestão de Crises com Sistema Preditivo em IA

Fase 6 — Coração Sob Controle (CardioIA). Scaffold inicial; executar treinamento, testes e validar integração antes da entrega. **Não usar em decisões clínicas reais.**

## Instalação
```bash
pip install -r requirements.txt
python -m src.train_model
pytest -q
```
Configure `OPENAI_API_KEY` no ambiente para a integração SDK. Nunca versionar segredos.

## Estrutura
- `data/`: dados sintéticos gerados localmente
- `docs/`: relatório e arquitetura
- `src/`: geração, treinamento, validação, ferramentas e agentes
- `notebook_treinamento.ipynb`: notebook Colab inicial

O conjunto sintético mantém os parâmetros oficiais, incluindo temperatura com média 24, desvio 5 e limites 10–40; temperatura não entra no rótulo. `score_risco` não é probabilidade clínica calibrada. O limiar de risco sistêmico alto não foi informado e permanece pendente. Histórico apenas em memória.

## Checklist
- [ ] Executar treinamento e registrar métricas reais
- [ ] Validar integração OpenAI Agents SDK, handoffs e histórico
- [ ] Executar testes
- [ ] Exportar arquitetura PDF (até 3 páginas)
- [ ] Completar relatório (até 2 páginas)
- [ ] Inserir integrantes/RMs e vídeo não listado (até 4 min)
- [ ] Conferir submissão e permissões FIAP
