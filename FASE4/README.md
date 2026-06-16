# ❤️ CardioIA – Fase 4
## Classificação de Arritmias Cardíacas com Redes Neurais Convolucionais (CNN)

---

## 👨‍💻 Integrantes

- Maison Wendrel Bezerra Ramos – RM: 565616
- Ítalo Domingues – RM: 561787

---

## 👨‍🏫 Professores

### Tutor(a)

- Caique Nonato da Silva Bezerra

### Coordenador(a)

- André Godoi Chiovato

---

# 📌 Descrição do Projeto

O CardioIA é uma solução baseada em Inteligência Artificial voltada para a identificação e classificação automática de arritmias cardíacas através de imagens de eletrocardiogramas (ECG).

Nesta Fase 4 foi desenvolvido um pipeline completo de Visão Computacional utilizando Redes Neurais Convolucionais (CNN), permitindo que imagens de ECG sejam classificadas em seis categorias distintas de batimentos cardíacos.

O objetivo é demonstrar como técnicas modernas de Deep Learning podem auxiliar profissionais da saúde na análise rápida e eficiente de sinais cardíacos.

---

# 🎯 Objetivos

- Aplicar técnicas de Visão Computacional em imagens médicas.
- Construir uma CNN para classificação de arritmias.
- Avaliar o desempenho do modelo utilizando métricas de Machine Learning.
- Identificar possíveis problemas de viés e desbalanceamento do conjunto de dados.
- Demonstrar a aplicação prática da Inteligência Artificial na área da saúde.

---

# 🗂 Estrutura do Projeto

```bash
FASE4/
│
├── data/
│   ├── train/
│   └── test/
│
├── src/
│   └── CardioIA_Fase4_Preprocessamento_FINAL.ipynb
│
└── README.md
```

---

# 📊 Dataset Utilizado

O projeto utiliza imagens de ECG organizadas em seis classes:

| Classe | Descrição |
|----------|------------|
| F | Fusion Beat |
| M | Myocardial Infarction |
| N | Normal Beat |
| Q | Unknown Beat |
| S | Supraventricular Beat |
| V | Ventricular Beat |

---

# 📚 Fonte dos Dados

O conjunto de dados utilizado neste projeto foi obtido através da plataforma Kaggle.

Dataset:
ECG Heartbeat Categorization Dataset

Fonte:
https://www.kaggle.com/datasets/shayanfazeli/heartbeat

O dataset é derivado da base MIT-BIH Arrhythmia Database, amplamente utilizada em pesquisas acadêmicas para detecção e classificação de arritmias cardíacas.

Classes utilizadas:

- N (Normal Beat)
- S (Supraventricular Beat)
- V (Ventricular Beat)
- F (Fusion Beat)
- Q (Unknown Beat)
- M (Myocardial Infarction)

# 📈 Distribuição das Classes (Treino)

| Classe | Quantidade |
|----------|------------:|
| F | 642 |
| M | 8.405 |
| N | 75.709 |
| Q | 6.431 |
| S | 2.223 |
| V | 5.789 |

Observa-se forte desbalanceamento entre as classes, especialmente na classe N (Normal), que representa a maior parte do conjunto de treinamento.

---

# ⚙️ Pré-processamento

As imagens passaram pelas seguintes etapas:

- Redimensionamento para 224x224 pixels
- Normalização dos pixels (0–1)
- Separação automática entre treino e validação
- Organização em batches para treinamento

Configuração utilizada:

```python
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 32
```

---

# 🧠 Arquitetura da CNN

A rede neural foi composta por:

### Bloco 1

```python
Conv2D(32)
MaxPooling2D()
```

### Bloco 2

```python
Conv2D(64)
MaxPooling2D()
```

### Bloco 3

```python
Conv2D(128)
MaxPooling2D()
```

### Classificador

```python
Flatten()
Dense(128, activation='relu')
Dropout(0.5)
Dense(6, activation='softmax')
```

---

# 📋 Resumo do Modelo

| Métrica | Valor |
|----------|--------:|
| Total de parâmetros | 11.169.734 |
| Parâmetros treináveis | 11.169.734 |
| Classes | 6 |
| Batch Size | 32 |
| Épocas | 10 |

---

# 📊 Divisão dos Dados

| Conjunto | Quantidade |
|------------|-----------:|
| Treino | 79.362 |
| Validação | 19.837 |
| Teste | 24.791 |

---

# 🚀 Resultados Obtidos

## Accuracy

```text
Accuracy: 1.0
```

## Loss

```text
Loss: 2.64e-10
```

---

# 📈 Relatório de Classificação

| Classe | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| F | 1.00 | 1.00 | 1.00 |
| M | 1.00 | 1.00 | 1.00 |
| N | 1.00 | 1.00 | 1.00 |
| Q | 1.00 | 1.00 | 1.00 |
| S | 1.00 | 1.00 | 1.00 |
| V | 1.00 | 1.00 | 1.00 |

Accuracy Geral:

```text
100%
```

---

# 📉 Matriz de Confusão

A matriz de confusão apresentou classificação perfeita para todas as categorias analisadas.

Não foram observados falsos positivos ou falsos negativos no conjunto de teste utilizado.

---

# ⚠️ Discussão Ética e Limitações

Apesar dos excelentes resultados obtidos, alguns pontos devem ser considerados:

### Desbalanceamento de Classes

A classe N (Normal) possui quantidade significativamente maior de exemplos quando comparada às demais classes.

Isso pode gerar:

- Tendência do modelo a favorecer a classe majoritária.
- Menor generalização em cenários reais.
- Possíveis vieses em populações diferentes das presentes no dataset.

### Ambiente Controlado

O modelo foi treinado em um conjunto de dados previamente organizado e limpo.

Em ambientes clínicos reais podem existir:

- Ruídos nos sinais.
- Artefatos de captura.
- Equipamentos diferentes.
- Pacientes com características distintas.

Portanto, antes de aplicação clínica real, seriam necessários novos testes, validações externas e aprovação regulatória.

---

# 🛠 Tecnologias Utilizadas

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-Learn
- Google Colab

---

# 📚 Conclusão

O projeto CardioIA Fase 4 demonstrou a viabilidade do uso de Redes Neurais Convolucionais para classificação automática de arritmias cardíacas a partir de imagens de ECG.

Os resultados obtidos evidenciam o potencial da Inteligência Artificial para auxiliar profissionais da saúde em tarefas de apoio diagnóstico, contribuindo para maior rapidez e eficiência na análise de exames cardíacos.

---

## 🔗 Repositório

GitHub:

https://github.com/Maison-ux

---
# 📖 Referências

1. Kaggle - ECG Heartbeat Categorization Dataset
   https://www.kaggle.com/datasets/shayanfazeli/heartbeat

2. MIT-BIH Arrhythmia Database
   https://physionet.org/content/mitdb/

3. TensorFlow Documentation
   https://www.tensorflow.org/

4. Scikit-Learn Documentation
   https://scikit-learn.org/
