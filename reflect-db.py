from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

engine = create_engine("sqlite:///sqlite-latest.sqlite")

metadata = MetaData()

metadata.reflect(engine, only=['invTypes', 'ramActivities', 'invCategories', 'invGroups', 'invTypeMaterials',
                               'industryBlueprints', 'invMetaTypes'])

Table('industryActivityMaterials', metadata,
      Column('typeID', Integer, primary_key=True),
      Column('activityID', Integer, primary_key=True),
      Column('materialTypeID', Integer, primary_key=True),
      Column('quantity', Integer)
      )

Base = automap_base(metadata=metadata)

Base.prepare()

InvTypes = Base.classes.invTypes
RamActivities = Base.classes.ramActivities
InvCategories = Base.classes.invCategories
InvGroups = Base.classes.invGroups
InvTypeMaterials = Base.classes.invTypeMaterials
IndustryBlueprints = Base.classes.industryBlueprints
InvMetaTypes = Base.classes.invMetaTypes

IndustryActivityMaterials = Base.classes.industryActivityMaterials


session = Session(engine)

for _id, name in session.query(InvTypes.typeID, InvTypes.typeName).filter(InvTypes.typeName.like('%multispectrum shield%blueprint%')):
    print('id = ', _id, 'name = ', name)

for name in session.query(InvTypes.typeName).filter(InvTypes.typeID == 165):
    print(name)

for name, quantity in session.query(InvTypes.typeName, InvTypeMaterials.quantity)\
        .join(InvTypeMaterials, InvTypeMaterials.materialTypeID == InvTypes.typeID)\
        .filter(InvTypeMaterials.typeID == 165):
    print(name, quantity)
