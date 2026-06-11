from random import *
import os, sys, shutil, time, subprocess

MAIN_SOL="a"
NUM_TEST=20
TIME_LIMIT=1
PROBLEM_ID="test"
OUTPUT=True
def create(i):
    if i<=NUM_TEST*.3:lim1=20;lim2=10;lim3=50
    else: lim1=5000;lim2=1000;lim3=1e9
    n=randint(1,lim1)
    print(n)
    for _ in range(n):print(randint(1,lim2),end=' ')
    print()
    for _ in range(n):print(randint(1,lim3),end=' ')
    print()
def run(filename):
    start = time.time()
    try:
        subprocess.run(
            [f"{filename}.exe"],
            timeout=TIME_LIMIT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return time.time() - start
    except subprocess.TimeoutExpired:
        return -1
def write(filename):
    sys.stdout=open(filename,"w")
def read(filename):
    with open(filename,"r") as file: return file.read()
def test(pid,tid):
    write(f"{MAIN_SOL}.INP")
    create(tid)
    sys.stdout.close()
    sys.stdout=sys.__stdout__
    if OUTPUT:run(MAIN_SOL)
    shutil.copy(f"{MAIN_SOL}.INP",f"Problems/{pid}/{tid}.INP")
    if OUTPUT:shutil.copy(f"{MAIN_SOL}.OUT",f"Problems/{pid}/{tid}.OUT")
    else:
        with open(f"Problems/{pid}/{tid}.OUT","w") as file:file.write("")
create(1)
if input()!='':exit()
if OUTPUT:
    print("Compiling")
    os.system(f"g++ {MAIN_SOL}.cpp -o {MAIN_SOL}.exe")
    print("Done Compiling")
def cleanup():
    print("Cleaning Up")
    time.sleep(1)
    os.remove(f"{MAIN_SOL}.INP")
    if OUTPUT:
        os.remove(f"{MAIN_SOL}.OUT")
        os.remove(f"{MAIN_SOL}.exe")
    print("Finished")
print("Generating Tests")
try:
    tests=0
    for i in range(1,NUM_TEST+1):
        test(PROBLEM_ID, i)
    cleanup()
except Exception as e:
    print(e)