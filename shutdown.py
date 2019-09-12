import threading
import sys

a = 0
b = 0
valor = 10

def transfer():
    global a, b, valor
    if (a >= valor):
        a -= valor
        b += valor
        print("Transferencia com sucesso [" + a.__str__() + "] [" + b.__str__() +"]")

if __name__ == "__main__":
    a = 100
    b = 100
    valor = 10
    pid = 0
    cur_thread = []
    for pid in range(10):
        process = threading.Thread(target=transfer())
        process.start()
        cur_thread.append(process)
        process.join()
