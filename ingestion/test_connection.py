import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

url = (
    f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
    f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
    f"?sslmode={os.environ['POSTGRES_SSLMODE']}"
)

engine = create_engine(url)

with engine.connect() as connection:
    result = connection.execute(text("select current_database(), current_user;"))
    print(result.fetchone())