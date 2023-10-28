class Cartao:
    def __init__(self, nome: str, limite: float) -> None:
        self.nome = nome
        self.limite = limite

    def __repr__(self) -> str:
        return f"Location(name={self.name})"

    def __eq__(self, other: str) -> bool:
        return self.name == other.name