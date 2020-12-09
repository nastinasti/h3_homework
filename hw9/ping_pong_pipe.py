from multiprocessing import Process, Pipe
from time import sleep
from os import getpid
from logs import logger


def ponger(receiver, sender, response):
  while True:
    receiver.recv()
    logger.info(f"Process {getpid()} got message: {response}")
    sleep(2)
    receiver.send(response)


if __name__ == "__main__":
  receiver, sender = Pipe()
  receiver_process = Process(target=ponger, args=(receiver, sender, 'Ping'))
  sender_process = Process(target=ponger, args=(sender, receiver, 'Pong'))

  sender_process.start()
  receiver_process.start()
  sender.send('Pong')
  receiver_process.join()
  sender_process.join()
  receiver_process.close()
  sender_process.close()
