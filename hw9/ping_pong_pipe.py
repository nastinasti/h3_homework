from multiprocessing import Process, Pipe
from time import sleep
from os import getpid
from log_orm import logger


def ponger(receiver, sender, response):
  while True:
    receiver.send(response)
    logger.info(f"Process {getpid()} got message: {response}")
    sleep(2)
    sender.send(response)


if __name__ == "__main__":
  receiver, sender = Pipe()
  receiver_process = Process(target=ponger, args=(receiver, sender, 'Pong'))
  sender_process = Process(target=ponger, args=(sender, receiver, 'Ping'))

  receiver_process.start()
  sender_process.start()
  print(receiver.recv())
  print(sender.recv())
  receiver_process.join()
  sender_process.join()
  receiver_process.close()
  sender_process.close()
