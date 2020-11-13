from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, Numeric
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlite-latest.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class InvTypes(Base):
    __tablename__ = 'invTypes'
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


class RamActivities(Base):
    __tablename__ = "ramActivities"
    activityID = Column(Integer, primary_key=True)
    activityName = Column(String(100))
    IconNo = Column(String(5))
    description = Column(String(1000))
    published = Column(Boolean)


class InvCategories(Base):
    __tablename__ = "invCategories"
    categoryID = Column(Integer, primary_key=True)
    categoryName = Column(String(100))
    iconID = Column(Integer)
    published = Column(Boolean)


class InvGroups(Base):
    __tablename__ = "invGroups"
    groupID = Column(Integer, primary_key=True)
    categoryID = Column(Integer, ForeignKey("invCategories.categoryID"))
    groupName = Column(String(100))
    iconID = Column(Integer)
    useBasePrice = Column(Boolean)


class IndustryActivityProducts(Base):
    __tablename__ = "industryActivityProducts"
    typeID = Column(Integer, ForeignKey("invTypes.typeID"), primary_key=True)
    activityID = Column(Integer, ForeignKey("ramActivities.activityID"),
                        primary_key=True)
    productTypeID = Column(Integer, ForeignKey("invTypes.typeID"),
                           primary_key=True)
    quantity = Column(Integer)


class IndustryActivityMaterials(Base):
    __tablename__ = "industryActivityMaterials"
    typeID = Column(Integer, ForeignKey("invTypes.typeID"), primary_key=True)
    activityID = Column(Integer, ForeignKey("ramActivities.activityID"),
                        primary_key=True)
    materialTypeID = Column(Integer, ForeignKey("invTypes.typeID"),
                            primary_key=True)
    quantity = Column(Integer)

    invTypes = relationship("InvTypes",
                            back_populates="industryActivityMaterials")


class IndustryActivityTime(Base):
    __tablename__ = "industryActivity"
    typeID = Column(Integer, ForeignKey("invTypes.typeID"), primary_key=True)
    activityID = Column(Integer, ForeignKey("ramActivities.activityID"),
                        primary_key=True)
    time = Column(Integer)


class IndustryActivityProbabilities(Base):
    __tablename__ = "industryActivityProbabilities"
    typeID = Column(Integer, ForeignKey("invTypes.typeID"),
                    primary_key=True)
    activityID = Column(Integer, ForeignKey("ramActivities.activityID"),
                        primary_key=True)
    productTypeID = Column(Integer, ForeignKey("invTypes.typeID"),
                           primary_key=True)
    probability = Column(Numeric)


session = Session()
for name in session.query(InvTypes.typeName).filter(InvTypes.typeID == 34):
    print(name)
