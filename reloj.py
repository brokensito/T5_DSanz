import time

while True:
    reloj = time.localtime()
    formato = time.strftime("%I:%M:%S %p", reloj)
    print(formato)
    time.sleep(1)

