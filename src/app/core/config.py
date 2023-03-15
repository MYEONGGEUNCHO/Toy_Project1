import os
from urllib.parse import quote
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseSettings


# PROJECT ROOT 상대경로
PROJECT_ROOT: str = os.path.dirname(
    os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
LOG_DIR = os.path.join(PROJECT_ROOT, 'src', 'logs')
APP_DIR = os.path.join(PROJECT_ROOT, 'src', 'app')

class Settings(BaseSettings):
    
    # DB INFO Settings
    DB_URI_TEMPLATE: Dict[str, str] = {
        'SQLITE': "sqlite:///{}{}{}{}{}./myapi.db" # main.py 동일 경로에 myapi.db 위치
        , 'MARIADB': "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4"
        , 'progresDB': "postgresql://{}:{}@{}:{}/{}"
    }
    DB_CONNECTION_INFO: Dict[str, Dict[str, str]] = {
        'SQLITE': {
            'user': ''
            ,'pwd': ''
            ,'host': ''
            ,'port': ''            
            ,'database': ''
        },
        'MARIADB': {
            'user': 'root'
            ,'pwd': '1234'
            ,'host': 'localhost'
            ,'port': '3306'            
            ,'database': 'mydb'
        },
        'POSTGRESDB': {
            'user': 'root'
            ,'pwd': '1234'
            ,'host': 'localhost'
            ,'port': '5432'            
            ,'database': 'mydb'
        }
    }
    
    def get_db_uri(
        self
        , uri_type: str
        , user: str
        , pwd: str
        , host: str
        , port: str
        , database: str
    ) -> str:
        """
        DB URI by DB TYPE

        Args:
            uri_type (str): DB TYPE
            user (str): user
            pwd (str): pwd
            host (str): host
            port (str): port
            database (str): database

        Returns:
            str: DB URI
        """
        return self.DB_URI_TEMPLATE[uri_type].format(
            user
            , quote(pwd)
            , host
            , port
            , database
        )    

    
    # KAFKA_BOOTSTRAP_SERVER: str = '192.168.200.22:9092'
    KAFKA_BOOTSTRAP_SERVER: str = '172.25.1.42:9092'

    # HCI KAFKA 
    KAFKA_HCI_BOOTSTRAP_SERVER: List[str] = [
        'kafka1.egap.co.kr:9092',
        'kafka1.egap.co.kr:9093',
        'kafka2.egap.co.kr:9092',
        'kafka2.egap.co.kr:9093',
        'kafka3.egap.co.kr:9092',
        'kafka3.egap.co.kr:9093'
    ]
    
    
    
settings = Settings()

# print(settings.get_db_uri('MARIADB', **settings.DB_CONNECTION_INFO['MARIADB']))