from app.database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT version();")
        )

        print("CONNECTED SUCCESSFULLY")
        print(result.fetchone())

except Exception as e:
    print("ERROR:")
    print(e)