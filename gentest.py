from random import *
import os, sys, shutil, time, subprocess

MAIN_SOL="sol"
NUM_TEST=20
TIME_LIMIT=1
PROBLEM_ID=1
def create():
    a=randint(1,10000)
    b=randint(1,100000)
    print(a,b)

def check(a,b):
    return a==b

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
    create()
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