
if __name__ == '__main__':
    from sqlalchemy import create_engine, text

    engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())

    with engine.connect() as conn:
        conn.execute(text('create table some_table (x int, y int)'))
        conn.execute(
            text('insert into some_table (x,y) values (:x, :y)'),
            [{'x': 1, 'y': 1}, {'x': 2, 'y': 4}]
        )
        conn.commit()

    with engine.begin() as conn:
        conn.execute(
            text('insert into some_table (x,y) values (:x, :y)'),
            [{'x': 6, 'y': 8}, {'x': 9, 'y': 10}]
        )

    with engine.connect() as conn:
        result = conn.execute(text('select x, y from some_table'))
        for row in result:
            print(f'x: {row.x} y: {row.y}')

    with engine.connect() as conn:
        result = conn.execute(text('select x, y from some_table'))
        for x, y in result:
            print(f'x: {x} y: {y}')

    with engine.connect() as conn:
        result = conn.execute(text('select x, y from some_table'))
        for row in result:
            print(f'x: {row[0]} y: {row[1]}')

    with engine.connect() as conn:
        result = conn.execute(text('select x, y from some_table'))
        for dict_row in result.mappings():
            print(f'{dict_row}')

    with engine.connect() as conn:
        result = conn.execute(text('SELECT x, y FROM some_table WHERE y > :y'), {'y': 2})
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

    from sqlalchemy.orm import Session

    stmt = text('select x, y from some_table where y > :y order by x, y')
    with Session(engine) as session:
        result = session.execute(stmt, {'y': 6})
        for row in result:
            print(f'x: {row.x} y: {row.y}')

    with Session(engine) as session:
        result = session.execute(
            text('update some_table set y=:y where x=:x'),
            [{'x': 9, 'y': 11}, {'x': 13, 'y': 15}]
        )
        session.commit()
