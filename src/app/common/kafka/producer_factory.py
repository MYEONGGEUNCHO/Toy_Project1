from kafka import KafkaProducer

from core.config import settings
from common.kafka import utils

def generate_producer(
    ptype: str = 'dict'
) -> KafkaProducer:
    
    if ptype == 'dict':
        return KafkaProducer(
            acks=-1
            , compression_type='gzip'
            , bootstrap_servers=settings.KAFKA_HCI_BOOTSTRAP_SERVER
            , value_serializer=utils.producer_value_serializer
        )
    elif ptype == 'value':
        return KafkaProducer(
            acks=-1
            , compression_type='gzip'
            , bootstrap_servers=settings.KAFKA_HCI_BOOTSTRAP_SERVER
            , value_serializer=utils.producer_original_value_serializer
        )
    else:
        return None