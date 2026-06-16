<div align="center">

# FIAP - Faculdade de Informática e Administração Paulista

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Logo_FIAP.png" width="250">

# CardioIA – Assistente Cardiológico Virtual com Visão Computacional

## Fase 4 – Superando Limites: Era da Mobilidade e Visão Inteligente

</div>

---

## Integrante

- Maison Wendrel Bezerra Ramos

## Turma

- TIAO 2026

## Grupo

- Grupo 76

## Professor

- (Preencher)

## Tutor

- (Preencher)

---

# Objetivo do Projeto

Desenvolver uma solução baseada em Inteligência Artificial e Visão Computacional para auxiliar na análise de imagens médicas simuladas relacionadas ao contexto cardiológico.

O projeto contempla:

- Pré-processamento de imagens
- Treinamento de Redes Neurais Convolucionais (CNN)
- Avaliação de desempenho
- Geração de previsões
- Apoio à tomada de decisão clínica

---

# Dataset Utilizado

Foi utilizado um dataset público de imagens médicas para experimentação e treinamento dos modelos de aprendizado profundo.

Devido às limitações de armazenamento do GitHub, o dataset original não foi incluído neste repositório.

A documentação referente ao dataset encontra-se em:

```
FASE4/data/README_DATASET.md
```

---

# Estrutura do Projeto

```
FASE4
│
├── data
│   └── README_DATASET.md
│
├── src
│   ├── CardioIA_Fase4_Preprocessamento_FINAL.ipynb
│   └── README_MODELO.md
│
└── README.md
```

---

# Pipeline de Pré-processamento

As etapas realizadas foram:

1. Carregamento das imagens
2. Redimensionamento
3. Normalização dos pixels
4. Organização das classes
5. Separação entre treino, validação e teste
6. Preparação dos lotes para treinamento

---

# Modelo CNN

Foi implementada uma Rede Neural Convolucional para classificação das imagens médicas.

Etapas:

- Camadas convolucionais
- Pooling
- Flatten
- Camadas densas
- Função Softmax
- Treinamento supervisionado

---

# Métricas Avaliadas

Foram utilizadas métricas estudadas durante a disciplina:

- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de Confusão

---

# Resultados

O modelo apresentou capacidade de identificar padrões nas imagens processadas, demonstrando a aplicação prática de técnicas de Visão Computacional no contexto da saúde.

Os resultados detalhados podem ser visualizados diretamente no notebook:

```
CardioIA_Fase4_Preprocessamento_FINAL.ipynb
```

---

# Protótipo

O notebook atua como protótipo funcional para demonstração do processo de classificação das imagens.

Funcionalidades:

- Pré-processamento
- Treinamento
- Avaliação
- Predição

---

# Tecnologias Utilizadas

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib
- Google Colab

---

# Repositório GitHub

GitHub:

https://github.com/Maison-ux/FIAP-TIAO-2026-CardioIA

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na FIAP.
