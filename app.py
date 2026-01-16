from flask import *
import time,judge,threading

app = Flask(__name__)

sub_id=0
subs={}
subs_pid={}

def refresh_problems():
    global problem_set,problem_name
    problem_set=[]
    problem_name={}
    with open("problemset.txt",'r') as file:
        data=file.readlines()
    for i in range(0,len(data),2):
        problem_set.append(data[i].replace("\n",''))
        problem_name[problem_set[i//2]]=data[i+1].replace("\n",'')

@app.route('/')
def home():
    return render_template(
        "home.html",
    )

@app.route('/api/problems')
def problems():
    res=[]
    refresh_problems()
    for i in range(0,len(problem_set)):
        res.append({"title":problem_name[problem_set[i]], "id":problem_set[i]})

    return res

@app.route('/api/submit',methods=['POST'])
def submit():
    global sub_id
    sub_id+=1
    data=request.get_json()
    inp=f"SUBMISSION_{sub_id}"
    subs_pid[sub_id]=data['problemId']
    def a():
        judge.write(f"{inp}.cpp",data['code'])
        subs[sub_id]=judge.main(data['problemId'],1,inp,'a')
    threading.Thread(target=a).start()
    return str(sub_id)

refresh_problems()

@app.route("/problem-<pid>")
def problem(pid):
    if pid not in problem_set:
        return "Invalid problem", 404
    return render_template(
        "problem.html",
        id=pid,
        name=problem_name[pid]
    )

@app.route("/submissions/<int:id>")
def submissions(id):
    if id>sub_id:
        return "Invalid submission", 404
    return render_template(
        "submissions.html",
        id=id,
        pid=subs_pid[id]
    )

@app.route("/api/submissions/<int:id>")
def submissions_api(id):
    if id>sub_id:
        return "Invalid submission", 404
    while id not in subs: pass
    return subs[id]

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)