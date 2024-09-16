from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve form data
    literature = float(request.form['literature'])
    mathematics = float(request.form['mathematics'])
    elective = float(request.form['elective'])

    exemption = request.form['exemption']

    if exemption == 'yes':
            foreign_language = 0  # No score needed for exemption
    else:
        foreign_language = float(request.form['foreign_language'])
    
    incentive = float(request.form.get('incentive', 0))
    avg_10 = float(request.form['avg_10'])
    avg_11 = float(request.form['avg_11'])
    avg_12 = float(request.form['avg_12'])
    priority = float(request.form.get('priority', 0))
    
    # Calculate average score
    avg_score = (avg_10 * 1 + avg_11 * 2 + avg_12 * 3) / 6
    
    # Calculate total score
    total_score = round(((literature + mathematics + elective + foreign_language + incentive) / 4 
                   + avg_score)/2 + priority, 2);


    
    return render_template('index.html', total_score=total_score)

if __name__ == '__main__':
    app.run(debug=True)