from enum import Enum
from pydantic import BaseModel, Field

class EnumBase(Enum):
    def __init__(self, idx, data) -> None:
        self.idx = idx
        self.data = data

    def __str__(self) -> str:
        """직렬화 상황에서 열거형 이름이 아닌 값 반환"""
        return self.data

class UdpMulticastGroup(EnumBase):
    NGGROUP1= (1, {'host': '233.38.231.172', 'port': 10422, 'name': 'nggroup2', 'ttl': 512, 'buff_size': 10240})
    NGGROUP2 = (2, {'host': '233.38.231.151', 'port': 10401, 'name': 'nggroup3', 'ttl': 512, 'buff_size': 10240})
    NGGROUP3 = (3, {'host': '233.38.231.167', 'port': 10451, 'name': 'nggroup4', 'ttl': 512, 'buff_size': 10240})
    NGGROUP4 = (4, {'host': '233.38.231.169', 'port': 10452, 'name': 'nggroup5', 'ttl': 512, 'buff_size': 10240})    

    @classmethod
    def get_by_name(cls, name: str):
        target_name = name.lower()
        result = {}
        for e in cls:
            if e.data['name'] == target_name:
                result.update(e.data)
                break
        return result


