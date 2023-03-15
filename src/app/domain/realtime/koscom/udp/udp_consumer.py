import logging
from datetime import datetime

from kafka import KafkaConsumer

from core.config import settings
from common.kafka.utils import  consumer_original_value_serializer


def koscom_udp_consumer(
    limit: int = 2000
    , debug: bool = True
) -> None:
    consumer = KafkaConsumer(
        auto_offset_reset='earliest'
        , enable_auto_commit=False
        , value_deserializer=consumer_original_value_serializer
        , bootstrap_servers=settings.KAFKA_HCI_BOOTSTRAP_SERVER
        , group_id='realtime-group-0'
        , max_poll_records=limit
    )
    
    topics = list()
    
    if debug:
        topics.append('realtime_test1')
    else:
        topics.append('realtime_test2')
        
    try:
        consumer.subscribe(topics=topics)
        
        print('start loop-------------')
        
        while True:
            try:
                poll_data = consumer.poll(timeout_ms=20000)
                record_chunk = []
                cnt = 0
                now_stmp = datetime.now()
                now_str = now_stmp.strftime('%Y-%m-%d').encode('cp949')
                
                for partition, messages in poll_data.items():
                    for message in messages:
                        try:
                            msg = message.value
                            
                            dtl_cd = msg[:5]
                            
                            print(msg)
                        
                        except Exception as parse_exc:
                            print(parse_exc)
                consumer.commit()
            except Exception as inner_exc:
                print(inner_exc)
    except Exception as exc:
        print(exc)
    finally:
        consumer.unsubscribe()
    