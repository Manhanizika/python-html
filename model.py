from datetime import date, datetime
from sqlalchemy import String, Numeric, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db


class Cartao(db.Model):
    __tablename__ = "cartoes"
    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30))
    cvv: Mapped[str] = mapped_column(String(3))
    limite: Mapped[float] = mapped_column(Numeric(precision=15,
                                                  scale=2))
    validade: Mapped[date] = mapped_column(Date())
    cliente: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(100))

    def __init__(self, **kwargs):
        super().__init__(status='ATIVO', **kwargs)

    def cancela(self):
        self.status = 'CANCELADO'

    def ativa(self):
        self.status = 'ATIVO'

    @property
    def is_ativo(self):
        return self.status == 'ATIVO'

    @property
    def is_cancelado(self):
        return self.status == 'CANCELADO'

    def __str__(self):
        return (f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} '
                f'com limite de {self.limite} valido até {self.validade}')

    def __repr__(self) -> str:
        return (f'Cartao(id={self.id!r}, numero={self.numero!r}, cvv = {self.cvv!r}, validade = {self.validade!r},'
                f' limite={self.limite!r}, cliente={self.cliente!r}, status={self.status!r})')

    def __set__limite(self, limite):
        limite_minimo = 10

        if limite < limite_minimo:
            raise ValueError(f'O limite deve ser de no mínimo {limite_minimo}')

        self.__limite = limite

    def __set_cliente(self, cliente):
        if not isinstance(cliente, str) or len(cliente.split()) != 2:
            raise ValueError("Cliente deve conter exatamente dois nomes separados por espaço.")

        nomes = cliente.split()
        for nome in nomes:
            if len(nome) < 2:
                raise ValueError("Cada nome deve ter pelo menos dois caracteres.")

        self.__cliente = cliente


class Compra(db.Model):
    __tablename__ = "compras"
    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[float] = mapped_column(Numeric(precision=15,
                                                 scale=2))
    data: Mapped[datetime] = mapped_column(DateTime())
    estabelecimento: Mapped[str] = mapped_column(String(1000))
    categoria: Mapped[str] = mapped_column(String(255))
    cartao_id: Mapped[int] = mapped_column(ForeignKey("cartoes.id"))
    cartao: Mapped['Cartao'] = relationship()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f'Compra(id={self.id!r}, valor={self.valor!r}, data = {self.data!r}, estabelecimento = {self.estabelecimento!r}, categoria = {self.categoria!r}, cartao = {self.cartao!r})'

    def __str__(self):
        return f'Compra: {self.__valor} no dia {self.__data} em {self.__estabelecimento} no cartão {self.__cartao.numero}'