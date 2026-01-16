from flask import *
import time,judge,threading

app = Flask(__name__)

sub_id=0
subs={}

def refresh_problems():
    global problem_set
    with open("problemset.txt",'r') as file:
        problem_set=file.readlines()
    for i in range(0,len(problem_set),2):
        problem_set[i]=problem_set[i].replace("\n",'')
        problem_set[i+1]=problem_set[i+1].replace("\n",'')

@app.route('/')
def home():
    return render_template(
        "home.html",
    )

@app.route('/api/problems')
def problems():
    res=[]
    refresh_problems()
    for i in range(0,len(problem_set),2):
        res.append({"title":problem_set[i+1], "id":problem_set[i]})

    return res

@app.route('/api/submit',methods=['POST'])
def submit():
    global sub_id
    sub_id+=1
    data=request.get_json()
    inp=f"SUBMISSION_{sub_id}"
    def a():
        judge.write(f"{inp}.cpp",data['code'])
        subs[sub_id]=judge.main(data['problemId'],1,inp,'a',lambda a,b:a==b)
    threading.Thread(target=a).start()
    return str(sub_id)

refresh_problems()

@app.route("/problem-<int:pid>")
def problem(pid):
    if str(pid) not in problem_set[::2]:
        return "Invalid problem", 404
    return render_template(
        "problem.html",
        id=pid,
        name=problem_set[pid*2-1]
    )

@app.route("/submissions/<int:id>")
def submissions(id):
    if id>sub_id:
        return "Invalid submission", 404
    return render_template(
        "submissions.html",
        id=id
    )

@app.route("/api/submissions/<int:id>")
def submissions_api(id):
    if id>sub_id:
        return "Invalid submission", 404
    while id not in subs: pass
    return subs[id]

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)