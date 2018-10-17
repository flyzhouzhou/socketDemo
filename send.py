# -*- coding:UTF-8 -*-
import time
import socket
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host','-ht',
                        required=True,
                        dest='host',
                        help='destination host addr needed')
    parser.add_argument('--port','-pt',
                        required=True,
                        dest='port',
                        help='deatination port needed')
    parser.add_argument('--data','-d',
                        default='test data',
                        dest='data',
                        help='send data')
    return parser.parse_args()

args = parse_args()

def main():
    host = args.host
    port = int(args.port)
    send_data = args.data
    try:
        soc = socket.socket()
        print('connecting remote server host:{} port:{}'.format(host,port))
        soc.connect((host,port))
        print('sending data')
        soc.sendall(send_data)
        time.sleep(1)
    except Exception as e:
        print('some error occurred:',e)
    finally:
        soc.close()



if __name__ == "__main__":
    main()
    print('over')