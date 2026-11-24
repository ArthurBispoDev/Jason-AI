from database.connection import engine
from database.models import Base

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")

# python -m database.create_tables -> Para executar o script