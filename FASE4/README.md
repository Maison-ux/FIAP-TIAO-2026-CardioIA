# ❤️ CardioIA – Fase 4

## Assistente Cardiológico Virtual com Visão Computacional

<div align="center">

# FIAP

## Faculdade de Informática e Administração Paulista

### FASE 4 – Superando Limites: Era da Mobilidade e Visão Inteligente

</div>

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

# 📌 Descrição do Projeto

O CardioIA é uma iniciativa acadêmica desenvolvida ao longo das fases do projeto FIAP com o objetivo de aplicar Inteligência Artificial em cenários relacionados à saúde cardiovascular.

Nesta Fase 4, o foco está na utilização de técnicas de Visão Computacional para realizar o processamento e a classificação de imagens médicas simuladas, permitindo a identificação automatizada de padrões relevantes para apoio à tomada de decisão clínica.

O projeto demonstra na prática a aplicação de Redes Neurais Convolucionais (CNNs), técnicas de pré-processamento de imagens e análise de métricas de desempenho amplamente utilizadas em projetos de Inteligência Artificial voltados para a área da saúde.

---

# 🎯 Objetivos da Fase 4

* Realizar o pré-processamento das imagens utilizadas no treinamento.
* Construir e treinar uma Rede Neural Convolucional (CNN).
* Avaliar o desempenho do modelo utilizando métricas apropriadas.
* Demonstrar a classificação das imagens por meio de um protótipo funcional.
* Aplicar conceitos de Visão Computacional estudados durante a disciplina.

---

# 📂 Estrutura do Projeto

```text
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

# 🔍 Pipeline de Pré-processamento

As imagens passaram pelas seguintes etapas:

1. Carregamento do dataset.
2. Redimensionamento das imagens.
3. Normalização dos pixels.
4. Organização das classes.
5. Separação em conjuntos de treino, validação e teste.
6. Preparação dos dados para treinamento da CNN.

---

# 🧠 Rede Neural Convolucional (CNN)

O modelo desenvolvido utiliza conceitos de Deep Learning aplicados à Visão Computacional.

Etapas principais:

* Camadas convolucionais.
* Funções de ativação.
* Pooling.
* Flatten.
* Camadas densas.
* Classificação supervisionada.

O treinamento foi realizado utilizando Python e TensorFlow/Keras no ambiente Google Colab.

---

# 📊 Avaliação do Modelo

As métricas utilizadas para avaliação foram:

* Accuracy (Acurácia)
* Precision (Precisão)
* Recall
* F1-Score
* Matriz de Confusão

Os resultados completos podem ser consultados diretamente no notebook disponibilizado no repositório.

---

# 💻 Tecnologias Utilizadas

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* Google Colab
* GitHub

---

# 📁 Dataset

O dataset utilizado para treinamento e testes não foi incluído neste repositório devido às limitações de armazenamento do GitHub.

As informações referentes ao conjunto de dados encontram-se em:

```text
FASE4/data/README_DATASET.md
```

---

# 🚀 Execução

1. Abrir o notebook:

```text
FASE4/src/CardioIA_Fase4_Preprocessamento_FINAL.ipynb
```

2. Executar as células na sequência.

3. Acompanhar:

* Pré-processamento
* Treinamento
* Avaliação
* Predições

---

# 📷 Evidências

Adicionar nesta seção:

* Prints do pré-processamento.
* Prints do treinamento.
* Prints das métricas.
* Prints da matriz de confusão.
* Prints das classificações realizadas.

---

# 🎥 Vídeo de Demonstração

Inserir o link do vídeo após a gravação:

```text
[LINK DO VÍDEO]
```

---

# 📄 Relatório

Inserir o link para o relatório PDF:

```text
https://doc-0s-b0-docstext.googleusercontent.com/export/mvsmsl4i9lhdsiepml8p5ru288/fu8esd437jhsf0paeucjudf5oo/1781643895000/107627523405490861081/107627523405490861081/1M24W0JnpYygNAkZ1Za0_qErEbxdMmL4AOeUCErrKEBg?format=pdf&id=1M24W0JnpYygNAkZ1Za0_qErEbxdMmL4AOeUCErrKEBg&token=ABg6iWQo8L8exODhdt77RATbZDpd:1781643708578&ouid=107627523405490861081&includes_info_params=true&usp=docs_home&cros_files=false&nded=false&tab=t.0&inspectorResult=%7B%22pc%22:3,%22lplc%22:13%7D&dat=AP8AcFpwjJs0mNozNnS5jrLTU_pzfb_-3kpdSyE5uGfjbvXi_7vFAIuzYZ28_yVNughLwIC1M-xm_DpefUTS-XMS3EdVaP3YtcOElwXfNqevzOvFRAS-TO4tb-NPi1mneHFXN7R1x93zsHS9SPRan9AjQ3ZfT_ebYXmq_wGOqh1ccQswsDEAlsdt9uN4DaUm-42fl8rCBPNKetd8MmdDgoyfktjHq0bRckTHWznVXjEj12-lY5-CwsrlhMjDX7ajRSPv4SA7q8K6ayaE_e2YiO1SvmWDMeTYyVdoc3q-tlAVgBG4pwmB9xrgNBZyf0bqwsHhRe2YcEMurVX2DSCKAb-mxq-GgSuIWTGuQ8uocLw2HhvVBPz2OcTdMvCrxzjwFKyGdJ3WzxcKahCIOk2VdLbiIJlX7ip_gggh6NqQ66_yhxMhrmxZgxQbRXq9Ac8OwoDqVWrijt7KITb9DpXilhWsUNISWigTRGvbyDYAeKchg0OBb4x6LBl4EsbeOYpaL-XxvGLOaTp1APN7b-40WrHuYpdYaPCnIUh7O6Q6cn657_JcCy5r-e_aZXr6ooia-DU6447cMNzgLtMwUbJG3FVmKgIRl9lvR1Zhtm5-gPDDiEOC3M0QuuIN4VZSM37LEPk3A4fKztJl7XaNFj4AIkRnP9bPsPfjWa273tvm0FR-PUO8UvZg3TH02-Z-E5QeTMYlw55avfBwA7ZlaPUxhNbI9ZRXH66J2XN1Ol4OjYnpIM8nx5ICthnbarEjl5lxLXUc8lA00bB9ZzxJOgn844TTKN8QA_c27F_qOyaQ10kFw2PY9hXMbBMYiXUSTpmWT6UGMlsxBH4d-NwgaSzxOGmGrR1prLHLg7X4ZfU6vPDqMSyKBmhqD1Gka4Vk-p2FuGDJgih2vN3-el9r80t51QRqYW5wbRt8Fe3Xe2FrCK7E6eIZ
```

---

# 🔗 Repositório GitHub

https://github.com/Maison-ux/FIAP-TIAO-2026-CardioIA

---

# 📜 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos como atividade da FIAP.

Não destinado para utilização clínica ou comercial.
