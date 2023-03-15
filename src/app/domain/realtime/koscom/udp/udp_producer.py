import socket
import struct
import traceback

from typing import List, Dict, Optional, Any

from domain.realtime.koscom.udp import udp_schema
from common.kafka.producer import base_hci_value_producer as base_producer

def koscom_udp_producer(
    group_name: str
    , debug: bool
) -> None:
    """koscom udp multicast 수집 서비스

    Args:
        group_name (str): multicast group 구분
        debug (bool): test flag
    """
    # group 정보 로드
    group = udp_schema.UdpMulticastGroup.get_by_name(group_name)
    print(group)
    if debug:
        topic = 'realtime_test1'
    else:
        topic = 'realtime_test2'
        
    if 'host' not in group or 'port' not in group:
        raise Exception('잘못된 멀티캐스트 그룹명입니다.')
        
    
    # 소캣 설정
    ## 설정값 설명
    sock = socket.socket(
        socket.AF_INET
        , socket.SOCK_DGRAM
        , socket.IPPROTO_UDP
    )
    
    # setsockopt
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind
    sock.bind(("", group['port']))
    # mreq
    mreq = struct.pack(
        "4sl"
        , socket.inet_aton(group['host'])
        , socket.INADDR_ANY
    )
    # setsockopt
    sock.setsockopt(
        socket.IPPROTO_IP
        , socket.IP_ADD_MEMBERSHIP
        , mreq
    )
    
    while True:
        try:
            data, addr = sock.recvfrom(group['buff_size'])
            rst = data[:-1].decode("utf-8")
            base_producer.send(topic, value=rst)
            print(f'{group["name"]}||{rst}')
                    
        except KeyboardInterrupt:
            print('stop service ...')
            break
        
        except Exception as exc:
            print(traceback.format_exc())
            print(f'----------{exc}----------')