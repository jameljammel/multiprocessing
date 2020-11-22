import time
from multiprocessing import Lock, Process
import random
import sys


def task(lock, mot):
    lock.acquire()
    try:
     i = 0
     while i < 1:
        for lettre in mot:
            sys.stdout.write(lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
        i += 1
    finally: #partie pour relacher le verrou sino il part en infinie
        lock.release()

def main():
    lock = Lock()
    colors = ['red', 'green', 'blue', 'black']
    processes = []
    for color in colors:
        proc = Process(target= task, args=(lock, color))
        processes.append(proc)
        proc.start()

    for proc in processes :
        proc.join()

if __name__ == '__main__':
    main()

