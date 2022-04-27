from app import create_app
from manage import alembic_upgrade, seed

app = create_app()
alembic_upgrade(app)
seed(app)
