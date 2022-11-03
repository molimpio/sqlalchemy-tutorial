from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    address = relationship('Address', back_populates='user')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f'Address(id={self.id}, email_address={self.email_address})'


if __name__ == '__main__':
    engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
    metadata_obj = MetaData()
    user_table = Table(
        'user_account',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('name', String(30)),
        Column('fullname', String),
    )

    print(f'{user_table.c.name}')
    print(f'{user_table.c.keys()}')
    print(f'{user_table.primary_key}')

    address_table = Table(
        'address',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', ForeignKey('user_account.id'), nullable=False),
        Column('email_address', String, nullable=False)
    )
    metadata_obj.create_all(engine)

    Base.metadata.create_all(engine)



