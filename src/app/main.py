import click

@click.group()
def main():
    pass

@main.command()
@click.option('-g', '--group', default='nggroup1')
@click.option('-d', '--debug', default=False, is_flag=True)
def koscom_realtime_producer(
    group: str
    , debug: bool
):
    """KOSCOM 실시간 UDP KAFKA Producer

    Args:
        group (str): 멀티캐스트 그룹
        debug (bool): flag
    """
    from domain.realtime.koscom.udp.udp_producer import koscom_udp_producer
    
    koscom_udp_producer(
        group_name=group
        , debug=debug
    )

@main.command()
@click.option('-l', '--limit', help='수신 데이터 수', default=2000, type=int)
@click.option('-d', '--debug', default=False, is_flag=True)
def koscom_realtime_consumer(
        limit: int
        , debug: bool
) -> None:
    """KOSCOM 실시간 UDP 데이터 저장 컨슈머

    Args:
        limit (int): message limit
        debug (bool): flag
    """
    from domain.realtime.koscom.udp.udp_consumer import koscom_udp_consumer
    
    koscom_udp_consumer(
        limit=limit
        , debug=debug
    )

@main.command()
@click.option('-d', '--data_path', help='파일 경로', default='C:\\Users\\202201006\\Desktop\\project\\mgcho\\Toy_Project1_io\\res\\batch\\ftp\\koscom\\20230307')
@click.option('-t', '--target_date', help='날짜', default='')
@click.option('-e', '--exe_tm', help='처리시간', default=3)
@click.option('-d', '--debug', help='flag', default=False, is_flag=True)
def koscom_ftp(
    data_path: str
    , target_date: str
    , exe_tm: str
    , debug: bool
) -> None:
    
    from domain.batch.tasks.koscom.ftp import extract_data
    
    extract_data(
        data_path=data_path
        , target_date=target_date
        , exe_tm=exe_tm
        , debug=debug
    )

    

if __name__ == "__main__":
    main()