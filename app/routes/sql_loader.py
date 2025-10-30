import os

SQL_FILE = os.path.join(os.path.dirname(__file__), "../queries/queries.sql")

def get_query(name: str) -> str | None:
    """
    Lê queries do arquivo queries.sql no formato:
    
    --QUERY nome_da_query
    SELECT * FROM tabela LIMIT :limit;
    """
    with open(SQL_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    queries = {}
    blocks = content.split("--QUERY ")
    for block in blocks[1:]:
        try:
            header, body = block.split("\n", 1)
            queries[header.strip()] = body.strip()
        except ValueError:
            pass

    return queries.get(name)
