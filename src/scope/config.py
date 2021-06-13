import os

def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'example')
    user, db_name = 'postgres', 'postgres'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"