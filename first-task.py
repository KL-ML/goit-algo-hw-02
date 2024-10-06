from queue import Queue
from uuid import uuid4
import time
import random

def loading(message):
    symbols = [f'{message}...  ', f'{message}...  ', f'{message} ... ', f'{message}  ...', f'{message}.  ..', f'{message}..  .', f'{message}...  ']
    i = 0
    times = random.randrange(1, len(symbols)*4, len(symbols))

    while times > 0:
        i = (i + 1) % len(symbols)
        print('\r\033[K%s' % symbols[i], flush=True, end='')
        time.sleep(0.25)
        times -= 1
    print('ready!')

class Request:
    def __init__(self, data):
        self.data = data
        self.id = uuid4()

class RequestQueue:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self, data=None):
        loading(message="Generating request")
        request: Request = Request(data)
        print(f"Request generated: {request.id}")
        self.queue.put(request)

    def process_request(self):
        time.sleep(random.randint(0, 2))
        request: Request = self.queue.get()
        if request:
            loading(message="Processing request")
            print(f"Request processed: {request.id}")
        else:
            print("No requests to process.")


if __name__ == "__main__":
    request_queue: RequestQueue = RequestQueue()
    while True:
        try:
            request_queue.generate_request()
            request_queue.process_request()
            time.sleep(random.randrange(0, 3))
        except KeyboardInterrupt:
            break
