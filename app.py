from flask import Flask, render_template, request, redirect, url_for  

app = Flask(__name__)  

tasks = []  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        task = request.form['task']  
        tasks.append(task)  
    return render_template('index.html', tasks=tasks)  

@app.route('/delete/<int:task_num>')  
def delete(task_num):  
    if 0 < task_num <= len(tasks):  
        del tasks[task_num-1]  
    return redirect(url_for('index'))  

@app.route('/edit/<int:task_num>', methods=['GET', 'POST'])  
def edit(task_num):  
    if 0 < task_num <= len(tasks):  
        if request.method == 'POST':  
            tasks[task_num-1] = request.form['updated_task']  
            return redirect(url_for('index'))  
        return render_template('edit.html', task=tasks[task_num-1], task_num=task_num)  
    return redirect(url_for('index'))  

if __name__ == '__main__':  
    app.run(debug=True)  