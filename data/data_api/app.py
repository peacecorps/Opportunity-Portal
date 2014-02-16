from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('index.html')



# @app.route('/')
# def search_job():
#     # content = request.json
#     return 'search_job'

@app.route('/foo')
def foo():
    return "hi"



if __name__ == '__main__':
    app.run(debug=True)