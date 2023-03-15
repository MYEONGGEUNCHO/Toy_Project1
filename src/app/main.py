import click

@click.group()
def main():
    pass

@main.command()
@click.option('-g', '--group', default='nggroup1')
@click.option('-d', '--debug', default=False, is_flag=True)
def koscom_realtime_producer(
    group: str
    , debug: bool = False
):
    from domain.realtime.koscom.udp.udp_producer import koscom_udp_producer
    
    koscom_udp_producer(
        group_name=group
        , debug=debug
    )
    

if __name__ == "__main__":
    main()