# 📊 Dataset - CardioIA Fase 4

## Descrição

Este projeto utiliza um conjunto de imagens de eletrocardiogramas (ECG) para classificação automática de arritmias cardíacas utilizando Redes Neurais Convolucionais (CNN).

---

## Fonte dos Dados

Dataset obtido através da plataforma Kaggle:

ECG Heartbeat Categorization Dataset

https://www.kaggle.com/datasets/shayanfazeli/heartbeat

---

## Base Científica

O dataset é derivado da base:

MIT-BIH Arrhythmia Database

https://physionet.org/content/mitdb/

A MIT-BIH é uma das bases mais utilizadas mundialmente em pesquisas relacionadas à análise de sinais cardíacos e detecção de arritmias.

---

## Classes Utilizadas

| Classe | Descrição |
|---------|------------|
| N | Normal Beat |
| S | Supraventricular Beat |
| V | Ventricular Beat |
| F | Fusion Beat |
| Q | Unknown Beat |
| M | Myocardial Infarction |

---

## Estrutura Utilizada

```text
data/
├── train/
│   ├── F
│   ├── M
│   ├── N
│   ├── Q
│   ├── S
│   └── V
│
└── test/
    ├── F
    ├── M
    ├── N
    ├── Q
    ├── S
    └── V
```

---

## Quantidade de Imagens

### Treino

| Classe | Quantidade |
|---------|-----------:|
| F | 642 |
| M | 8.405 |
| N | 75.709 |
| Q | 6.431 |
| S | 2.223 |
| V | 5.789 |

Total: **79.362 imagens**

---

### Teste

Total: **24.791 imagens**

---

## Observação

O dataset completo não foi incluído neste repositório devido ao tamanho elevado dos arquivos.

Para reproduzir os resultados apresentados neste projeto, é necessário realizar o download do dataset original através do Kaggle e manter a estrutura de diretórios apresentada acima.
