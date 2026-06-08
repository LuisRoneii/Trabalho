# ============================================================
# Implementação de Deque (Fila Dupla — Double-Ended Queue)
# ============================================================


class EmptyDequeError(Exception):
    """Exceção personalizada lançada ao operar sobre um Deque vazio."""
    pass


class Deque:
    """
    Implementação de Deque (Fila Dupla) utilizando uma lista Python.
    Suporta inserção e remoção tanto no início quanto no fim da estrutura.
    """

    def __init__(self):
        # Lista interna que armazena os elementos do deque.
        # O índice 0 representa o INÍCIO; o índice -1 representa o FIM.
        self._data = []

    # ----------------------------------------------------------
    # Métodos de inserção
    # ----------------------------------------------------------

    def insert_first(self, value):
        """Insere um elemento no INÍCIO (frente) do deque."""
        self._data.insert(0, value)  # Desloca todos os elementos uma posição à direita
        print(f"[insert_first] '{value}' inserido no início → {self._data}")

    def insert_last(self, value):
        """Insere um elemento no FIM (traseira) do deque."""
        self._data.append(value)     # Adiciona ao final — custo amortizado O(1)
        print(f"[insert_last]  '{value}' inserido no fim    → {self._data}")

    # ----------------------------------------------------------
    # Métodos de remoção
    # ----------------------------------------------------------

    def remove_first(self):
        """
        Remove e retorna o elemento do INÍCIO do deque.
        Lança EmptyDequeError se o deque estiver vazio.
        """
        if self.is_empty():
            raise EmptyDequeError("Não é possível remover do início: o deque está vazio.")
        removed = self._data.pop(0)   # Remove o índice 0 e desloca os demais para a esquerda
        print(f"[remove_first] '{removed}' removido do início → {self._data}")
        return removed

    def remove_last(self):
        """
        Remove e retorna o elemento do FIM do deque.
        Lança EmptyDequeError se o deque estiver vazio.
        """
        if self.is_empty():
            raise EmptyDequeError("Não é possível remover do fim: o deque está vazio.")
        removed = self._data.pop()    # Remove o último elemento — O(1)
        print(f"[remove_last]  '{removed}' removido do fim    → {self._data}")
        return removed

    # ----------------------------------------------------------
    # Métodos de consulta (sem remoção)
    # ----------------------------------------------------------

    def first(self):
        """
        Retorna (sem remover) o elemento do INÍCIO do deque.
        Lança EmptyDequeError se o deque estiver vazio.
        """
        if self.is_empty():
            raise EmptyDequeError("Não é possível consultar o início: o deque está vazio.")
        return self._data[0]

    def last(self):
        """
        Retorna (sem remover) o elemento do FIM do deque.
        Lança EmptyDequeError se o deque estiver vazio.
        """
        if self.is_empty():
            raise EmptyDequeError("Não é possível consultar o fim: o deque está vazio.")
        return self._data[-1]

    # ----------------------------------------------------------
    # Métodos utilitários
    # ----------------------------------------------------------

    def is_empty(self):
        """Retorna True se o deque não contém elementos, False caso contrário."""
        return len(self._data) == 0

    def size(self):
        """Retorna a quantidade de elementos presentes no deque."""
        return len(self._data)

    def __repr__(self):
        """Representação textual exibindo a ordem do início ao fim."""
        return f"Deque(início → fim): {self._data}"


# ==============================================================
# Bloco de testes — mínimo de 10 operações
# ==============================================================

def run_tests():
    print("=" * 60)
    print("       DEQUE — BATERIA DE TESTES (≥ 10 operações)")
    print("=" * 60)

    dq = Deque()

    # 1. Verifica que um deque recém-criado começa vazio
    print(f"\n[TESTE  1] is_empty()  → {dq.is_empty()}")   # Esperado: True

    # 2. Insere no fim
    dq.insert_last(10)                                       # [10]

    # 3. Insere no fim novamente
    dq.insert_last(20)                                       # [10, 20]

    # 4. Insere no início
    dq.insert_first(5)                                       # [5, 10, 20]

    # 5. Insere no início novamente
    dq.insert_first(1)                                       # [1, 5, 10, 20]

    # 6. Consulta o início sem remover
    print(f"\n[TESTE  6] first()     → {dq.first()}")       # Esperado: 1

    # 7. Consulta o fim sem remover
    print(f"[TESTE  7] last()      → {dq.last()}")          # Esperado: 20

    # 8. Verifica o tamanho atual
    print(f"[TESTE  8] size()      → {dq.size()}")          # Esperado: 4

    # 9. Remove do início
    print()
    dq.remove_first()                                        # Remove 1  → [5, 10, 20]

    # 10. Remove do fim
    dq.remove_last()                                         # Remove 20 → [5, 10]

    # 11. Insere mais elementos e verifica o estado atual
    dq.insert_last(30)                                       # [5, 10, 30]
    dq.insert_first(0)                                       # [0, 5, 10, 30]
    print(f"\n[TESTE 11] Estado atual → {dq}")

    # 12. Remove todos os elementos um a um
    print("\n[TESTE 12] Esvaziando o deque:")
    while not dq.is_empty():
        dq.remove_first()

    print(f"\n[TESTE 12] is_empty() após esvaziar → {dq.is_empty()}")   # Esperado: True

    # 13. Tenta remover do início com deque vazio — tratamento de erro
    print("\n[TESTE 13] Tentando remove_first() com deque vazio:")
    try:
        dq.remove_first()
    except EmptyDequeError as e:
        print(f"  ✔ EmptyDequeError capturada → {e}")

    # 14. Tenta remover do fim com deque vazio — tratamento de erro
    print("\n[TESTE 14] Tentando remove_last() com deque vazio:")
    try:
        dq.remove_last()
    except EmptyDequeError as e:
        print(f"  ✔ EmptyDequeError capturada → {e}")

    # 15. Verifica que first() também lança erro com deque vazio
    print("\n[TESTE 15] Tentando first() com deque vazio:")
    try:
        dq.first()
    except EmptyDequeError as e:
        print(f"  ✔ EmptyDequeError capturada → {e}")

    print("\n" + "=" * 60)
    print("         TODOS OS TESTES CONCLUÍDOS COM SUCESSO")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()



## Breve Explicação do Projeto:A classe Deque foi implementada utilizando os conceitos de Orientação a Objetos em Python,
## tendo como estrutura interna de armazenamento uma lista padrão (list), cumprindo a restrição de não utilizar o módulo collections
## Início do Deque: Representado pelo índice 0 da lista. Operações aqui deslocam os elementos,
## possuindo complexidade de tempo $O(n)$.Fim do Deque: Representado pelo último índice da lista (-1).
## Operações aqui ocorrem no final da estrutura, possuindo complexidade amortizada $O(1)$.Tratamento de Erros:
## Foi criada a classe customizada EmptyDequeError que herda de Exception. Ela é lançada preventivamente sempre que o usuário tenta ler ou remover elementos de um Deque vazio (is_empty() == True).##