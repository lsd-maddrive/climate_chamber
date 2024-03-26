from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Model = declarative_base(metadata=metadata)


class Temperature(Model):
    __tablename__ = 'temperature_table'

    id = Column(Integer, primary_key=True)
    key = Column(String)
    value = Column(String)
    temperature = Column(Float)

    def __repr__(self):
        return f"<Tempa(key='{self.key}',value='{self.value}',tempa='{self.temperature}')>"
