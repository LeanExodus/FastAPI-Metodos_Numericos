from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:////opt/application/test.db")

#sqlite:////opt/application/test.db
#mysql+pymysql://root:@localhost:3306/db_metodos
meta = MetaData()

conn = engine.connect()

