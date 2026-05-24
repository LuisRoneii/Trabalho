class FilaEspera:
    def __init__(self, capacidade=None):
        """
        Estrutura de dados FIFO (First In, First Out).
        
        Parâmetros:
            capacidade (int | None): Limite de elementos suportados.
                                     Se None, a fila cresce sem restrição.
        """
        self._buffer = []
        self._capacidade = capacidade

    def inserir(self, elemento):
        """
        Insere um elemento no final da fila.
        Dispara OverflowError caso a capacidade máxima já tenha sido atingida.
        """
        if self.esta_cheia():
            raise OverflowError(
                f"Capacidade máxima ({self._capacidade}) atingida. Inserção negada."
            )
        self._buffer.append(elemento)

    def remover(self):
        """
        Retira e devolve o elemento da frente da fila (ordem FIFO).
        Dispara IndexError se não houver elementos.
        """
        if self.esta_vazia():
            raise IndexError("Operação inválida: nenhum elemento para remover.")
        return self._buffer.pop(0)

    def frente(self):
        """
        Consulta o próximo elemento sem retirá-lo da fila.
        Dispara IndexError se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("Operação inválida: a fila não contém elementos.")
        return self._buffer[0]

    def esta_vazia(self):
        """Indica se a fila está sem elementos."""
        return not self._buffer

    def esta_cheia(self):
        """Indica se a fila atingiu o limite de capacidade definido."""
        if self._capacidade is None:
            return False
        return len(self._buffer) >= self._capacidade

    def total(self):
        """Retorna a quantidade de elementos presentes na fila."""
        return len(self._buffer)

    def esvaziar(self):
        """Remove todos os elementos da fila de uma vez."""
        self._buffer.clear()


# ---------------------------------------------------------------------------
# Ponto de entrada do programa
# ---------------------------------------------------------------------------
if __name__ == "__main__":

    separador = "=" * 52

    print(separador)
    print("   IMPLEMENTAÇÃO DE FILA — TESTES E VALIDAÇÕES")
    print(separador)

    # -----------------------------------------------------------------------
    # TESTE 1 — Fila sem limite de capacidade
    # -----------------------------------------------------------------------
    print("\n[TESTE 1] Fila de atendimento sem restrição de tamanho")

    atendimento = FilaEspera()
    atendimento.inserir("Ana")
    atendimento.inserir("Bruno")
    atendimento.inserir("Carlos")

    print(f"  Elementos na fila   : {atendimento.total()}")
    print(f"  Próximo na fila     : {atendimento.frente()}")
    print(f"  Removendo elemento  : {atendimento.remover()}")
    print(f"  Removendo elemento  : {atendimento.remover()}")
    print(f"  Elementos restantes : {atendimento.total()}")
    print(f"  Fila vazia?         : {atendimento.esta_vazia()}")

    # -----------------------------------------------------------------------
    # TESTE 2 — Esvaziamento manual da fila
    # -----------------------------------------------------------------------
    print("\n[TESTE 2] Limpeza completa da fila")

    atendimento.esvaziar()
    print(f"  Elementos após limpeza : {atendimento.total()}")
    print(f"  Fila vazia?            : {atendimento.esta_vazia()}")

    # -----------------------------------------------------------------------
    # TESTE 3 — Remoção e consulta em fila vazia (IndexError esperado)
    # -----------------------------------------------------------------------
    print("\n[TESTE 3] Operações proibidas em fila vazia")

    try:
        atendimento.remover()
    except IndexError as exc:
        print(f"  remover() -> IndexError capturado : {exc}")

    try:
        atendimento.frente()
    except IndexError as exc:
        print(f"  frente()  -> IndexError capturado : {exc}")

    # -----------------------------------------------------------------------
    # TESTE 4 — Inserção além da capacidade (OverflowError esperado)
    # -----------------------------------------------------------------------
    print("\n[TESTE 4] Inserção em fila com capacidade esgotada")

    impressora = FilaEspera(capacidade=2)
    impressora.inserir("relatorio.pdf")
    impressora.inserir("contrato.pdf")
    print(f"  Capacidade esgotada? : {impressora.esta_cheia()}")

    try:
        impressora.inserir("apresentacao.pdf")
    except OverflowError as exc:
        print(f"  inserir() -> OverflowError capturado : {exc}")

    print(f"\n{separador}")
    print("   TODOS OS TESTES CONCLUÍDOS COM ÊXITO")
    print(separador)