from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/story2')
def story2():
    return render_template('story2.html')

@app.route('/story3')
def story3():
    return render_template('story3.html')

@app.route('/story4')
def story4():
    return render_template('story4.html')




# @app.route("/mars", methods=["POST"])
# def mars_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg':'POST 연결 완료!'})

# @app.route("/mars", methods=["GET"])
# def mars_get():
#     return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)