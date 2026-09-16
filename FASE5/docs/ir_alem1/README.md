@"
# CardioIA — Fase 5 — IR ALÉM 1

## IA Generativa e Extração de Informações Clínicas

Componente acadêmico do projeto CardioIA desenvolvido para a Fase 5 da FIAP.

### Objetivo

Demonstrar o processamento de informações clínicas simuladas, utilizando um prompt estruturado e organização da resposta em formato JSON.

### Fluxo

1. Carregamento do texto clínico simulado.
2. Preparação do prompt.
3. Definição dos campos clínicos esperados.
4. Estruturação da resposta em JSON.
5. Validação da estrutura.
6. Geração de `saida_clinica.json`.
7. Execução dos testes automatizados.

### Dados utilizados

- Sintoma: palpitações
- Duração: aproximadamente 30 minutos
- Frequência cardíaca: 110 bpm
- Pressão arterial: 150/95 mmHg
- Medicamento: medicamento para pressão

Os dados são simulados e utilizados exclusivamente para fins acadêmicos.

### Campos estruturados

- `sintomas`
- `pressao_arterial`
- `frequencia_cardiaca`
- `duracao`
- `medicamentos`
- `observacoes`

### Arquivos

- `ir_alem1/ai_generativa.py` — implementação do processamento
- `ir_alem1/entrada_clinica.txt` — entrada clínica simulada
- `ir_alem1/saida_clinica.json` — saída estruturada
- `ir_alem1/teste_ir_alem1.py` — testes automatizados

### Validação

O módulo verifica a validade do JSON e a presença dos campos obrigatórios.

### Testes

Resultado confirmado:

4 testes aprovados.

```text
4 passed in 0.09s