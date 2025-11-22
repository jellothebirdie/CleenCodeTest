from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
import io
import contextlib
import methods as m

app = Flask(__name__)
app.secret_key = "changethis"

@app.route('/')
def welcome():
    return render_template('welcome.html', page_title='Welcome Page')

@app.route('/problems/')
def problems():
    return render_template('problems.html', page_title='Problems')

@app.route('/problem/<problem_name>', methods=['GET', 'POST'])
def problem(problem_name):
    print(m.problems.keys())
    data = m.problems[problem_name]
    if request.method == 'GET':
        # if GET, send blank form
        return render_template('problem.html', data=data)
    else:
        print('put')
        # need to implement as with test
        return render_template('problem.html', data=data)

@app.route('/test/', methods=['GET', 'POST'])
def test():
    print(request.method)
    if request.method == 'GET':
        # if GET, send blank form
        return render_template('test.html', page_title='Test')

    else:
        code = request.form.get('code')
        print('code:', code)
        try:
            result, output = m.execute_code(code)
            
            # Build response: prioritize returned value, then printed output
            response_text = ""
            if output:
                response_text += output
            if result is not None:
                if response_text:
                    response_text += "\n"
                response_text += str(result)
            
            if not response_text:
                response_text = "Code executed with no output"
            
            # Return plain text response for fetch
            return response_text, 200, {'Content-Type': 'text/plain'}

        except Exception as e:
            # Return error message as plain text
            return f"Error: {str(e)}", 500, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.debug = True
    app.run()