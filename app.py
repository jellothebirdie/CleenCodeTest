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

@app.route('/main/')
def main():
    return render_template('main.html', page_title='Main Page')

@app.route('/problems/')
def problems():
    return render_template('problems.html', page_title='Problems')

@app.route('/test/', methods=['GET', 'POST'])
def test():
    print(request.method)
    if request.method == 'GET':
        # if GET, send blank form
        return render_template('test.html', page_title='Test')

    else:
        code = request.form.get('code')
        print('code')
        try:
            result = m.get_function(code)
            output = m.execute_function(result)

            # Prioritize returned value, then printed output
            if result is not None:
                flash(str(result))
            elif output:
                flash(output)
            else:
                flash('No output')

            return render_template('test.html', page_title='Test')

        except Exception as e:
            flash(str(e))
            return redirect(url_for('test'))

if __name__ == '__main__':
    app.debug = True
    app.run()