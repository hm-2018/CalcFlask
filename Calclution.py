from flask import Flask, request, render_template , url_for
# ================================================================================================
app = Flask(__name__)
# ================================================================================================
@app.route('/')  # like index
def home():
    return render_template('calc.html')
# ================================================================================================
@app.route('/Calc', methods=['get', 'post'])
def Calc():
    #if request.method == 'POST':
    Number1 = int(request.form['num1'])
    opreation = request.form['opreation']
    Number2 = int(request.form['num2'])
    try:
     if opreation=='plus':
        num3 = Number1 + Number2
     elif opreation=='mins':
        num3 = Number1 - Number2
     elif opreation=='power':
        num3 = Number1 * Number2
     elif opreation=='division':
        num3 = Number1 / Number2
    
     else:
      return render_template('calc.html', Calc=0)
    except Exception as ex:
        Calc = ex
    return render_template('calc.html', Calc = num3 )
# ================================================================================================
if __name__ == '__main__':
    app.run(debug=False , host = '0.0.0.0')

