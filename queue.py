class Queue:
    def __init__(self, max_size=None):
        """
        Fila baseada em princípio FIFO (First In, First Out).

        Parâmetros:
            max_size (int | None): Número máximo de elementos aceitos.
                                   Quando None, a fila não possui limite.
        """
        self._dados = []
        self._max_size = max_size

    def enqueue(self, item):
        """
        Insere um novo item ao final da fila.

        Lança:
            OverflowError: se max_size foi definido e a fila já está cheia.
        """
        if self.is_full():
            raise OverflowError(
                f"Limite de {self._max_size} elemento(s) atingido. "
                "Remova um item antes de inserir outro."
            )
        self._dados.append(item)

    def dequeue(self):
        """
        Remove e retorna o elemento do início da fila (ordem FIFO).

        Lança:
            IndexError: se chamado em uma fila vazia.
        """
        if self.is_empty():
            raise IndexError("dequeue() não permitido: a fila está vazia.")
        return self._dados.pop(0)

    def peek(self):
        """
        Retorna o elemento do início da fila sem removê-lo.

        Lança:
            IndexError: se chamado em uma fila vazia.
        """
        if self.is_empty():
            raise IndexError("peek() não permitido: a fila está vazia.")
        return self._dados[0]

    def is_empty(self):
        """Retorna True se não houver elementos na fila; False caso contrário."""
        return not self._dados

    def is_full(self):
        """
        Retorna True se a fila atingiu max_size; False caso contrário.
        Sempre False quando max_size não foi definido.
        """
        if self._max_size is None:
            return False
        return len(self._dados) >= self._max_size

    def size(self):
        """Retorna o número de elementos atualmente armazenados."""
        return len(self._dados)

    def clear(self):
        """Descarta todos os elementos, deixando a fila vazia."""
        self._dados.clear()


# ---------------------------------------------------------------------------
# Testes — executados apenas quando o arquivo é chamado diretamente
# ---------------------------------------------------------------------------
if __name__ == "__main__":

    linha = "-" * 48

    print("TESTE 1 — Enfileiramento e consulta básica")
    print(linha)
    fila = Queue()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    print(f"Elementos na fila : {fila.size()}")       # esperado: 3
    print(f"Primeiro elemento : {fila.peek()}")        # esperado: 10
    print(f"Fila vazia?       : {fila.is_empty()}")    # esperado: False

    print(f"\nTESTE 2 — Remoção em ordem FIFO")
    print(linha)
    print(f"dequeue() -> {fila.dequeue()}")            # esperado: 10
    print(f"dequeue() -> {fila.dequeue()}")            # esperado: 20
    print(f"Restam {fila.size()} elemento(s) na fila") # esperado: 1

    print(f"\nTESTE 3 — Limpeza com clear()")
    print(linha)
    fila.clear()
    print(f"Tamanho após clear() : {fila.size()}")     # esperado: 0
    print(f"Fila vazia?          : {fila.is_empty()}") # esperado: True

    print(f"\nTESTE 4 — IndexError ao operar fila vazia")
    print(linha)
    try:
        fila.dequeue()
    except IndexError as erro:
        print(f"dequeue() -> IndexError : {erro}")

    try:
        fila.peek()
    except IndexError as erro:
        print(f"peek()    -> IndexError : {erro}")

    print(f"\nTESTE 5 — OverflowError ao exceder capacidade")
    print(linha)
    fila_limitada = Queue(max_size=2)
    fila_limitada.enqueue("req_1")
    fila_limitada.enqueue("req_2")
    print(f"is_full() com 2/2 elementos : {fila_limitada.is_full()}")  # esperado: True

    try:
        fila_limitada.enqueue("req_3")
    except OverflowError as erro:
        print(f"enqueue() -> OverflowError : {erro}")

    print(f"\n{'=' * 48}")
    print("  Todos os 5 testes executados com sucesso.")
    print(f"{'=' * 48}")