import json
from typing import Any, Dict

def producer_value_serializer(value: Any) -> str:
    """카프카 전송 메시지 직렬화 문자열 변환

    Args:
        value (Any): 직렬화 대상 객체

    Returns:
        str: 직렬화 문자열
    """
    return json.dumps(value).encode('utf-8')

def consumer_value_deserializer(value: bytes) -> Dict[str, Any]:
    """카프카 전송 메시지 역직렬화 후 객체(딕셔너리) 변환

    Args:
        value (bytes): _description_

    Returns:
        Dict[str, Any]: _description_
    """
    return json.loads(value.decode('utf-8'))

def producer_original_value_serializer(value: str) -> str:
    return value.encode('utf-8')

def consumer_original_value_serializer(value: str) -> str:
    return value.decode('utf-8')