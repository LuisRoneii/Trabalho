# Estrutura de Dados — Fila de Espera (FIFO)

Este repositório apresenta a implementação manual de uma **Fila (First In, First Out)** em Python,
sem uso de bibliotecas externas. O arquivo principal já inclui uma suíte de testes integrada que
cobre tanto o fluxo normal de uso quanto situações de erro controladas.

## Como Executar

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.  
Para verificar, rode no terminal:

```bash
python --version
```

### Executando o Programa

Navegue até a pasta do projeto e execute:

```bash
python fila_espera.py
```

A saída exibirá quatro blocos de teste numerados, confirmando o comportamento esperado
da estrutura em cada cenário.

---

## Estrutura da Classe `FilaEspera`

| Método | Descrição |
|---|---|
| `__init__(capacidade)` | Inicializa a fila. `capacidade=None` significa sem limite. |
| `inserir(elemento)` | Adiciona um elemento ao final da fila. |
| `remover()` | Remove e retorna o elemento da frente (ordem FIFO). |
| `frente()` | Consulta o próximo elemento sem removê-lo. |
| `esta_vazia()` | Retorna `True` se não houver elementos na fila. |
| `esta_cheia()` | Retorna `True` se a capacidade máxima foi atingida. |
| `total()` | Retorna a quantidade atual de elementos. |
| `esvaziar()` | Remove todos os elementos de uma vez. |

---

## Cenários de Teste

O bloco `if __name__ == "__main__"` cobre os seguintes casos:

- **Teste 1** — Inserção, consulta e remoção em fila sem limite de capacidade.
- **Teste 2** — Esvaziamento completo da fila via `esvaziar()`.
- **Teste 3** — Tentativa de `remover()` e `frente()` em fila vazia → captura de `IndexError`.
- **Teste 4** — Tentativa de inserção em fila com capacidade esgotada → captura de `OverflowError`.

---

## Tratamento de Erros

| Situação | Exceção Lançada |
|---|---|
| Remover ou consultar elemento de fila vazia | `IndexError` |
| Inserir elemento em fila já no limite | `OverflowError` |

---

## Princípio de Funcionamento

A fila segue o princípio **FIFO**: o primeiro elemento inserido é sempre o primeiro a ser removido.
Isso garante ordem justa de processamento, amplamente utilizada em sistemas de atendimento,
filas de impressão e escalonamento de processos.