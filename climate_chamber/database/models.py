from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Model = declarative_base(metadata=metadata)


class Tempa(Model):

    tablename = 'Temperatura_tablica'

    id = Column(Integer, primary_key=True)
    key = Column(String)
    value = Column(String)
    tempa = Column(Float)

    def repr(self):
        return f"<Tempa(key='{self.key}',value='{self.value}',tempa='{self.temperature}')>"
