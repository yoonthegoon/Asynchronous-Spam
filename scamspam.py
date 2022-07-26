import concurrent.futures
import json
import time
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.request import Request


HEADERS = json.load(open('headers.json'))
PAYLOAD = json.load(open('payload.json'))


def send_request(request, infinite):
    while True:
        with urlopen(request) as f:
            print(f'{datetime.now()}\t\t{f.status}')

        if not infinite:
            break


def send_all(url, threads, method='GET', infinite=False):
    t = time.time()
    print(datetime.now())

    data = urlencode(PAYLOAD).encode()
    r = Request(url, data=data, headers=HEADERS, method=method)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(send_request, r, infinite) for _ in range(threads)]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

    print(f'{time.time() - t:.3f}s')
