from random import *
import os, shutil, time, subprocess

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

def write(filename, content):
    with open(filename, "w") as file: 
        return file.write(content)

def read(filename):
    with open(filename, "r") as file: 
        return file.read()

def test(inp_file,out_file, check):
    shutil.copy(inp_file, f"{FILE}.INP")
    r = run(INP)
    run(INP)
    return (check(read(f"{FILE}.OUT"), read(out_file)) if r != -1 else -1, r)

def cleanup():
    time.sleep(1)
    for f in [f"{FILE}.INP", f"{FILE}.OUT", f"{INP}.exe"]:
        if os.path.exists(f):
            os.remove(f)

def main(problem_id, time_limit, inp, file, check):
    global INP, TIME_LIMIT, FILE
    INP = inp
    FILE = file
    TIME_LIMIT = time_limit
    
    print(f"Compiling {INP}.cpp")
    os.system(f"g++ {INP}.cpp -o {INP}.exe")
    
    res = []
    try:
        test_dir = f"Problems/{problem_id}"
        test_count = len([f for f in os.listdir(test_dir) if f.endswith('.INP')])
        for i in range(1, test_count + 1):
            a, r = test(f"{test_dir}/{i}.INP",f"{test_dir}/{i}.OUT", check)
            t = "AC" if a else "WA" if a != -1 else "TLE"
            res.append(t)
        cleanup()
    except Exception as e:
        print(e)
        cleanup()
    return res