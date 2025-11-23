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

@app.route('/problem/<problem_slug>', methods=['GET', 'POST'])
def problem(problem_slug):
    print("SESSION AT START:", session.get('complete'))
    slugs_to_names = {
    "two-sum": "Two Sum",
    "palindrome": "Palindrome",
    "rain-water": "Rain Water"
    }
    problem_name = slugs_to_names[problem_slug]
    data = m.problems[problem_name]
    tests = m.problems[problem_name]['tests']

    if request.method == 'GET':
        return render_template('problem.html', data=data, tests=tests, page_title=problem_name)

    # POST request
    else:
        code = request.form.get('code')

        try:
            # Compile user code and extract the function
            func = m.load_user_function(code)

            if func is None:
                return "No function found in submitted code.", 400

            test_results = []
            for test in data["tests"]:
                passed, result = m.run_test(func, test)
                test_results.append({
                    "input": test["input"],
                    "expected": test["output"],
                    "actual": result,
                    "passed": passed
            })
                
            num_passed = sum(1 for r in test_results if r["passed"])
            if num_passed == len(test_results):
                complete = session.get('complete', {})
                complete[problem_name] = True
                session['complete'] = complete

            print(session['complete'])


            # print(test_results)
            return render_template('problem.html', data=data, tests=test_results, page_title=problem_name)

        
        except Exception as e:
            return f"Error: {str(e)}", 500, {'Content-Type': 'text/plain'}


@app.before_request
def init_complete_counter():
    if 'complete' not in session:
        session['complete'] = {'Two Sum': False, 
                               'Palindrome': False,
                               'Rain Water': False}

if __name__ == '__main__':
    app.debug = True
    app.run()