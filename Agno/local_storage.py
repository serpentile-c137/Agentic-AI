# Agno/local_storage.py
from pathlib import Path
from agno.db.sqlite import SqliteDb  # current DB handle [web:51][web:15]

DB_PATH = Path("tmp/agno.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def load_social_media_storage():
    # Return a DB object for the Agent; name kept for compatibility. [web:51]
    return SqliteDb(db_file=str(DB_PATH))  # single-file SQLite database [web:51]




# from agno.storage.agent.sqlite import SQLiteAgentStorage

# def load_social_media_storage() -> SQLiteAgentStorage:
#     storage = SQLiteAgentStorage(
#         table_name="social_media_session",
#         db_file="./storage/social_media_session.db"
#     )
#     return storage


