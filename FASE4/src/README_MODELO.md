# 🧠 CardioIA – Modelo Treinado

## Fase 4 – Assistente Cardiológico Virtual com Visão Computacional

---

# 📌 Sobre o Modelo

Este documento descreve o modelo de Inteligência Artificial desenvolvido durante a Fase 4 do projeto CardioIA.

O objetivo do modelo é realizar a classificação automática de imagens de eletrocardiogramas (ECG), identificando diferentes tipos de batimentos cardíacos por meio de técnicas de Visão Computacional e Deep Learning.

O treinamento foi realizado utilizando Redes Neurais Convolucionais (CNN), uma das arquiteturas mais utilizadas para tarefas de classificação de imagens.

---

# 📁 Arquivo do Modelo

Nome original do modelo treinado:

```text
modelo_cardioia_fase4.h5
```

---

# ⚠️ Observação Importante

O arquivo do modelo não foi disponibilizado neste repositório.

Motivo:

O GitHub possui limite máximo de 100 MB por arquivo em repositórios convencionais.

O arquivo gerado durante o treinamento possui aproximadamente:

```text
128 MB
```

Por esse motivo, apenas o notebook responsável pelo treinamento e geração do modelo foi disponibilizado.

---

# 🏗️ Arquitetura da Rede Neural

O modelo foi desenvolvido utilizando uma Rede Neural Convolucional (CNN) composta pelas seguintes camadas:

### Bloco Convolucional 1

```text
Conv2D (32 filtros)
MaxPooling2D
```

### Bloco Convolucional 2

```text
Conv2D (64 filtros)
MaxPooling2D
```

### Bloco Convolucional 3

```text
Conv2D (128 filtros)
MaxPooling2D
```

### Classificador

```text
Flatten
Dense (128 neurônios)
Dropout (0.5)
Dense (6 neurônios - Softmax)
```

---

# 📊 Configurações do Treinamento

| Parâmetro           | Valor                    |
| ------------------- | ------------------------ |
| Tamanho das imagens | 224 x 224                |
| Batch Size          | 32                       |
| Épocas              | 10                       |
| Classes             | 6                        |
| Otimizador          | Adam                     |
| Função de Perda     | Categorical Crossentropy |

---

# 🧪 Classes Classificadas

O modelo foi treinado para reconhecer seis categorias de batimentos cardíacos:

| Classe | Descrição             |
| ------ | --------------------- |
| F      | Fusion Beat           |
| M      | Myocardial Infarction |
| N      | Normal Beat           |
| Q      | Unknown Beat          |
| S      | Supraventricular Beat |
| V      | Ventricular Beat      |

---

# 📈 Resultados Obtidos

Avaliação realizada sobre o conjunto de teste.

### Accuracy

```text
1.0000
```

### Loss

```text
2.64e-10
```

### Métricas por Classe

| Classe | Precision | Recall | F1-Score |
| ------ | --------- | ------ | -------- |
| F      | 1.00      | 1.00   | 1.00     |
| M      | 1.00      | 1.00   | 1.00     |
| N      | 1.00      | 1.00   | 1.00     |
| Q      | 1.00      | 1.00   | 1.00     |
| S      | 1.00      | 1.00   | 1.00     |
| V      | 1.00      | 1.00   | 1.00     |

Accuracy Geral:

```text
100%
```

---

# 🔄 Como Reproduzir o Modelo

1. Abrir o notebook:

```text
CardioIA_Fase4_Preprocessamento_FINAL.ipynb
```

2. Executar todas as células na sequência.

3. Realizar:

* carregamento do dataset;
* pré-processamento das imagens;
* treinamento da CNN;
* avaliação do modelo;
* geração do arquivo `.h5`.

Ao final da execução será criado novamente o arquivo:

```text
modelo_cardioia_fase4.h5
```

---

# 💻 Ambiente Utilizado

* Google Colab
* Python 3
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn

---

# 👥 Integrantes

* Maison Wendrel Bezerra Ramos – RM 565616
* Italo Domingues – RM 561787

---

# 👨‍🏫 Professores

## Tutor(a)

* Caique Nonato da Silva Bezerra

## Coordenador(a)

* André Godoi Chiovato

---

# 📚 Considerações Finais

O modelo desenvolvido demonstrou excelente desempenho na classificação das imagens de ECG utilizadas durante os experimentos.

Os resultados obtidos evidenciam o potencial das Redes Neurais Convolucionais para auxiliar na identificação automática de padrões cardíacos, reforçando a importância da Inteligência Artificial como ferramenta de apoio à área da saúde.

---

## FIAP – Inteligência Artificial

Projeto acadêmico desenvolvido para a disciplina de Visão Computacional.

**CardioIA – Fase 4 – Assistente Cardiológico Virtual com Visão Computacional**
