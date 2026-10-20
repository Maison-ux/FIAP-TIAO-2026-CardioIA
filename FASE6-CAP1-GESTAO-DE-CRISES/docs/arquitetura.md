# Arquitetura CAP1

```text
Entrada -> Orquestrador/validação -> Analista de Risco -> tool prever_risco (Random Forest) -> Especialista em Protocolos -> tool consultar_protocolos -> Planejador de Resposta -> Orquestrador/resposta JSON v1.0
```

Histórico inicial em memória. Entrada inválida interrompe antes da inferência; modelo ausente/incompatível retorna erro; limiar sistêmico não informado fica pendente. A implementação SDK/handoffs ainda requer integração e teste.