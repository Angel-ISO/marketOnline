from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://uw7kpqjvtwjgjvlp:96kgABFFa3NVHT6BHYsG@bubjqyt0xq0ugmdptvos-mysql.services.clever-cloud.com/bubjqyt0xq0ugmdptvos")

meta = MetaData()

conn = engine.connect()