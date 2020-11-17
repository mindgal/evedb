from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("sqlite:///sqlite-latest.sqlite")

Base.prepare(engine, reflect=True)

InvTypes = Base.classes.invTypes
RamActivities = Base.classes.ramActivities
InvCategories = Base.classes.invCategories
InvGroups = Base.classes.invGroups
IndustryActivityTime = Base.classes.industryActivity0


session = Session(engine)

for name in session.query(InvTypes.typeName).filter(InvTypes.typeID == 34):
    print(name)
