from typing import Optional, Tuple, Callable

from core.config import settings

from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, MetaData, Table
from sqlalchemy.engine import Engine
from sqlalchemy.ext.automap import AutomapBase
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import declarative_base




# TARGET_TABLE = {
#     'MARIADB': {
#         'only': [
#             'H_DATA'
#         ]
#     },
#     'POSTGRESDB': {
#         'only': [
#             'h_data'
#         ]
#     }
# }

# def get_base(
#     engine: Engine
#     , target: str
# ) -> Optional[AutomapBase]:
#     Base = None
#     public_schema_metadata = None
    
#     if target == 'POSTGRESDB':
#         public_schema_metadata = MetaData(schema='public')
        
#         public_schema_metadata.reflect(
#             engine, **TARGET_TABLE[target]
#         )
        
#         Base = automap_base(metadata=public_schema_metadata)
#         Base.prepare()
    
#     # if target == 'MARIADB':
        
    
#     return Base

engine_maria = create_engine(
    settings.get_db_uri(
        'MARIADB'
        , **settings.DB_CONNECTION_INFO['MARIADB']
    )
    , echo=True
)

SessionLocal_Maria = sessionmaker(
    autocommit=False
    , autoflush=False
    , bind=engine_maria
)

Base = declarative_base()

# engine_postgre = create_engine(
#     settings.get_db_uri(
#         'POSTGRESDB'
#         , **settings.DB_CONNECTION_INFO['POSTGRESDB']
#     )
#     , echo=True
# )

# SessionLocal_Postgre = sessionmaker(
#     autocommit=False
#     , autoflush=False
#     , bind=engine_postgre
# )

def make_session(db_type: str) -> Tuple[Engine, Callable]:
    """엔진 객체와 세션 팩토리 반환"""

    engine = create_engine(
        settings.get_db_uri(db_type,
                **settings.DB_CONNECTION_INFO[db_type]),
        echo=False)

    session_factory = sessionmaker(autocommit=False, 
            autoflush=False, bind=engine)
    
    return engine, session_factory