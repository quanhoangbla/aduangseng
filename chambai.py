from subprocess import *
import time

log=''
with open(f'inp','r') as file:
    with open(f'out','r') as file1:
        inp=f'{file.read()}\n'
        out=file1.read()
        start=time.time()
        p = Popen(['python',f'a.py'], shell=True, stdin=PIPE, stdout=PIPE)
        output, err = p.communicate(inp.encode())
        speed=time.time()-start
        log=f'''Thời gian chạy : {speed}s
Kết quả : {output.decode()}
Đáp án : {out}'''
print(log)