from typing import Any, List

class Stack:


    ## Construtor
    def __init__(self) -> None:
        self.__data: List[Any] = []

    def push(self, elemento: Any) -> None:
        self.__data.append(elemento)

    def pop(self) -> Any:
        if len(self.__data) > 0:
            valor = self.__data.pop()
            return valor
        else:
            print("Não pode dar pop em lista vazia")

    def __repr__(self) -> str:
        return str(self.__data)

    def peek(self) -> Any:
        return self.__data[-1]

    def size(self) -> int:
        return len(self.__data)

    def invert(self):
        invertida = Stack()
        copia = self.__data.copy()

        for i in range(self.size()):
            invertida.push(self.__data.pop())
        self.__data = copia

        return invertida


## Main
if __name__ == "__main__":
    pilha = Stack()

    pilha.push("111")
    pilha.push("222")
    pilha.push("333")
    pilha.push("444")
    pilha.push("555")

    print(pilha)

    print(pilha.pop())

    print(pilha)

    pilha.pop()

    print(pilha)

    print(pilha.peek())

    print(pilha.size())

    pilhaInvertida = pilha.invert()
    print(pilhaInvertida)

    print(pilha)