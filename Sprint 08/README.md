# 📌 Análise de Risco de Inadimplência e Crédito

## 📖 Descrição do Projeto

Este projeto tem como objetivo analisar o risco de inadimplência e prever a capacidade de pagamento de clientes da Home Credit. Utilizamos técnicas de Ciência de Dados e Machine Learning para criar um modelo preditivo, garantindo que clientes elegíveis não sejam injustamente recusados.

---

## 🔍 Fluxo do Projeto

1. **Exploração de Dados**: Análise inicial dos datasets fornecidos.
2. **Pré-processamento**: Tratamento de dados, remoção de colunas irrelevantes e normalização.
3. **Treinamento do Modelo**: Implementação de um RandomForestClassifier com validação cruzada.
4. **Avaliação**: Uso de métricas como AUC-ROC, Matriz de Confusão e SHAP para interpretação do modelo.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - Pandas, NumPy (Manipulação de Dados)
  - Scikit-learn (Modelagem e Avaliação)
  - Seaborn, Matplotlib (Visualização de Dados)
  - XGBoost (Modelo de Machine Learning)

---

## 📊 Principais Métricas e Resultados

### Regressão Logística

| Classe | Precision | Recall | F1-score | Suporte |
|--------|------------|--------|----------|---------|
| 0 (Pagantes) | 0.90 | 1.00 | 0.95 | 469845 |
| 1 (Inadimplentes) | 0.50 | 0.00 | 0.00 | 50070 |
| **Acurácia** | **0.90** |
| **AUC ROC** | **0.5006** |

### Decision Tree

| Classe | Precision | Recall | F1-score | Suporte |
|--------|------------|--------|----------|---------|
| 0 (Pagantes) | 0.91 | 1.00 | 0.95 | 469845 |
| 1 (Inadimplentes) | 0.81 | 0.02 | 0.03 | 50070 |
| **Acurácia** | **0.90** |
| **AUC ROC** | **0.5085** |

### XGBoost

| Classe | Precision | Recall | F1-score | Suporte |
|--------|------------|--------|----------|---------|
| 0 (Pagantes) | 0.92 | 1.00 | 0.96 | 469845 |
| 1 (Inadimplentes) | 0.94 | 0.18 | 0.30 | 50070 |
| **Acurácia** | **0.92** |
| **AUC ROC** | **0.5897** |

![image](https://github.com/user-attachments/assets/5ec23084-f20f-4e56-9edd-9780edc7add9)


---

## 📂 Arquivos do Projeto

- **Desafio.ipynb**: Notebook Jupyter contendo todas as etapas do projeto, desde a exploração dos dados até a avaliação dos modelos.

---

## 🎥 Apresentação

Um vídeo explicativo do projeto foi gravado para detalhar todo o processo. [Assista aqui](#) (inserir link caso disponível).

---

## 📩 Dúvidas ou Sugestões?

Fique à vontade para entrar em contato! 🚀

