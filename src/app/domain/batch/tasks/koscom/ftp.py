import os
import traceback

from datetime import datetime
from typing import List, Dict, Optional, Tuple, Any

def extract_data(
    data_path: str
    , target_date: str
    , exe_tm: str = '3'
    , debug: bool = False
) -> None:
    """FTP 수신 데이터 추출 후 저장

    Args:
        data_path (str): FTP 수신 경로
        target_date (str): YYYYmmdd
        debug (bool): 저장 flag
    """
    
    print(f'koscom file download start---------')
    # 대상 일자 설정
    if target_date == None:
        target_date = datetime.now().strftime('%Y%m%d')
    # bulk insert settings
    bulk_limit = 10000
    
    # 파일명 템플릿
    FILE_NAME_TEMPLATE = '{}.{}'
    
    # 저장 flag
    if debug:
        pass
    else:
        pass
    # 파일 정보 로드 - 파일 스펙 확인
    # ex
    file_schema = [
        ['bofjivst2']
        , ['BONDAV0']
        , ['BONDAVD']
        , ['BONDBOF']
        , ['BONDJ1']
        , ['bondtrad']
        , ['BONDJ0']
        , ['BONDPV0']
    ]
    
    try:
        for file in file_schema:
            # 경로 생성
            file_path = os.path.join(
                data_path
                , FILE_NAME_TEMPLATE.format(file[0], target_date)
            )
            
            # 경로 확인
            if os.path.exists(file_path):
                # 파일 읽기
                with open(file_path, 'r', encoding='utf-8') as input_stream:
                    bulk_list = []
                    for idx, line in enumerate(input_stream):
                        # 인코딩
                        encoded_line = line.encode('utf-8')
                        
                        print(encoded_line[:-1])
                        
                        # bulk_list.append()
                    
                    # if len(bulk_list) > 0:
                    #     pass
            else:
                print(f'{file_path} does not exists-----------')
    
    except Exception as exc:
        print(exc)
    # finally:
    #     sessipn.close()
    