import os
import traceback

from datetime import datetime
from typing import List, Dict, Optional, Any


def extract_data(
    data_path: str
    , target_date: str
    , debug: bool
) -> None:
    """FTP 수신 파일 데이터 추출 후 저장

    Args:
        data_path (str): FTP 수신 경로
        target_date (str): YYYYMMDD
        debug (bool): test flag
    """
    if target_date == '':
        target_date = datetime.now().strftime('%Y%m%d')
    target_date_hypen = datetime.now().strftime('%Y-%m-%d')
    
    # 벌크 인서트 설정
    bulk_limit = 10000
    
    # 파일명 템플릿 
    ## 파일명.해당날짜
    FILE_NAME_TEMPLATE = '{}.{}'
    
    # 파일 정보 저장
    if debug:
        pass
    else:
        pass
    
    # 파일 정보 로드
    ## 파일명 수집
    
    # 경로 생성
    ## 수신 경로/파일명 템플릿
    
    # 경로 확인
    
    # 파일 읽기
    
    # 파일 저장