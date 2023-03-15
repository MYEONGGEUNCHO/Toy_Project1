from kafka import KafkaProducer

from core.config import settings
from common.kafka import utils

base_hci_dict_producer = KafkaProducer(
    acks=-1, 
    compression_type='gzip',
    bootstrap_servers=settings.KAFKA_HCI_BOOTSTRAP_SERVER,
    value_serializer=utils.producer_value_serializer
)

base_hci_value_producer = KafkaProducer(
    acks=-1, 
    compression_type='gzip',
    bootstrap_servers=settings.KAFKA_HCI_BOOTSTRAP_SERVER,
    value_serializer=utils.producer_original_value_serializer
)