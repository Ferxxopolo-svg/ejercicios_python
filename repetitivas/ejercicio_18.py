import time
import os

for hora in range(0, 24):
    for minuto in range(0, 60):
        for segundo in range(0, 60):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"{hora}:{minuto}:{segundo}")
            
            time.sleep(1)