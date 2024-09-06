from flask import Flask, render_template, redirect, request
from models import add_time, get_times

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['campo1']
        pais = request.form['campo2']
        campeonatos_nacionais = request.form['campo3']
        campeonatos_internacionais = request.form['campo4']
        
        add_time(nome, pais, campeonatos_nacionais, campeonatos_internacionais)
        
        return redirect('/')
    
    times = get_times()
    return render_template('index.html', times=times)

if __name__ == '__main__':
    app.run(debug=True)
