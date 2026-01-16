from random import *
import os, sys, shutil, time, subprocess

MAIN_SOL="sol"
NUM_TEST=10
TIME_LIMIT=1
PROBLEM_ID=2
def create(i):
    lim=0
    if i<=NUM_TEST*0.3: lim=20
    else: lim=1e5
    n=randint(1,lim)
    print(n)
    for i in range(n): print(randint(1,int(1e9)),end=' ')
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
    run(MAIN_SOL)
    shutil.copy(f"{MAIN_SOL}.INP",f"Problems/{pid}/{tid}.INP")
    shutil.copy(f"{MAIN_SOL}.OUT",f"Problems/{pid}/{tid}.OUT")

print("Compiling")
os.system(f"g++ {MAIN_SOL}.cpp -o {MAIN_SOL}.exe")
print("Done")
def cleanup():
    print("Cleaning Up")
    time.sleep(1)
    os.remove(f"{MAIN_SOL}.INP")
    os.remove(f"{MAIN_SOL}.OUT")
    os.remove(f"{MAIN_SOL}.exe")
    print("Finished")
try:
    tests=0
    for i in range(1,NUM_TEST+1):
        test(PROBLEM_ID, i)
    cleanup()
except Exception as e:
    print(e)