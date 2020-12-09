from multiprocessing import Process, Pipe
from time import sleep
from os import getpid
from logs import logger


def ponger(receiver, sender, response):
  while True:
    receiver.recv()
    logger.info(f"Process {getpid()} got message: {response}")
    sleep(2)
    sender.send(response)


if __name__ == "__main__":
  receiver1, sender1 = Pipe()
  receiver2, sender2 = Pipe()
  receiver_process = Process(target=ponger, args=(receiver1, sender2, 'Ping'))
  sender_process = Process(target=ponger, args=(receiver2, sender1, 'Pong'))

  sender_process.start()
  receiver_process.start()
  sender1.send('Ping')
  receiver_process.join()
  sender_process.join()
