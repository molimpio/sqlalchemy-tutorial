
if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
    print(f'engine {engine}')
