import argparse
import logging

from moneybook.util import Timer

logger = logging.getLogger('MONEYBOOK')


def run():
    t = Timer()
    t.start()
    option = get_option()
    setup_logger(option.log_level)
    logger.info('Moneybook start at {}'.format(t.start_time))
    # TODO RUN MAIN FUNCTION
    t.end()
    logger.info('Moneybook end at {} [{} second(s)]'.format(t.end_time, t.term))


def get_option():
    parser = argparse.ArgumentParser(description='Moneybook data tool')
    parser.add_argument('-b', '--base-url', type=str, help='Base URL of PC Moneybook')
    parser.add_argument('-l', '--log-level', type=str, default='INFO',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Logging level')
    return parser.parse_args()


def setup_logger(log_level):
    logger.setLevel(log_level.upper())
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


if __name__ == '__main__':
    run()
