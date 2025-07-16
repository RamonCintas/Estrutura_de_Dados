# 🧠 Projeto: Estrutura de Dados com Python e Java

Este repositório contém três programas simples que demonstram o uso de **estruturas de dados** em **Python** e **Java**. São exemplos práticos e interativos.

---

## 📁 Arquivos

### 🐍 `Fila.py`

Simula uma **fila de espera**, utilizando a estrutura `deque` da biblioteca `collections` do Python.

#### 🔧 Funcionalidades:
- Permite adicionar até 100 nomes à fila.
- Valida e ajusta automaticamente se o número ultrapassar o limite.
- Exibe a lista completa de pessoas em ordem de chegada.

#### 🧠 Estrutura usada:
- `collections.deque` com `maxlen=100` (estrutura de **fila**).

---

### 🐍 `Lista.py`

Solicita ao usuário que digite 5 **números inteiros positivos** e os armazena em uma **lista**.

#### 🔧 Funcionalidades:
- Aceita apenas valores inteiros **positivos**.
- Realiza validação e tratamento de exceções.
- Exibe os números válidos ao final.

#### 🧠 Estrutura usada:
- Lista (`list`) do Python.

---

### ☕ `Main.java`

Implementa um **vetor (array unidimensional)** de Strings para armazenar os nomes de 10 cidades.

#### 🔧 Funcionalidades:
- Solicita ao usuário que digite o nome de 10 cidades.
- Armazena os nomes em um vetor.
- Exibe o vetor completo com os nomes cadastrados.

#### 🧠 Estrutura usada:
- `String[]` (vetor unidimensional - **array** em Java).

---

## 📌 Requisitos

- **Python 3.6+** para os scripts `fila.py` e `lista.py`
- **JDK 8+** para compilar e executar `Main.java`

---

## ▶️ Como executar

### Python:
```bash
python fila.py
python lista.py
```

### Java:
```bash
javac Main.java
java Main
```

---

## 📚 Conceitos abordados
- Lista (list)

- Fila (deque)

- Vetor (array unidimensional em Java)

- Validação de entrada do usuário

- Tratamento de exceções (try/except)

- Manipulação de coleções

- Entrada e saída interativa (console)