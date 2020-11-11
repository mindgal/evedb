from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlite-latest.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class InvTypes(Base):
    __tablename__ = 'invtypes'

    typeID = Column(Integer, primary_key=True)
    groupID = Column(Integer)
    typeName = Column(String)
    description = Column(String)
    mass = Column(Float)
    volume = Column(Float)
    capacity = Column(Float)
    portionSize = Column(Integer)
    raceID = Column(Integer)
    basePrice = Column(Float)
    published = Column(Boolean)
    marketGroupID = Column(Integer)
    iconID = Column(Integer)
    soundID = Column(Integer)
    graphicID = Column(Integer)

    industryactivitymaterials = relationship("IndustryActivityMaterials")


class IndustryActivityMaterials(Base):
    __tablename__ = 'industryactivitymaterials'
    typeID = Column(Integer, ForeignKey("invtypes.typeID"))
    activityID = Column(Integer)
    materialTypeID = Column(Integer)
    quantity = Column(Integer)

    invtypes = relationship("InvTypes", back_populates="industryactivitymaterials")


session = Session()
for name in session.query(InvTypes.typeName).filter(InvTypes.typeID == 34):
    print(name)
