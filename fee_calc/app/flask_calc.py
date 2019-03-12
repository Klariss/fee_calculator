from flask import Flask, render_template, request
from app.calculator import FeeCalc, Term
from app.calculator import Data

app2 = Flask(__name__)


@app2.route('/', methods=['GET'])
def index():
    """A simple page, where parameters can be given."""
    return render_template('index.html')


@app2.route('/Error', methods=['GET'])
def error():
    """A simple page, where parameters can be given."""
    return render_template('Error.html')


@app2.route('/calculate', methods=['POST'])
def calculate():
    """Recieve the given parameters and the calculation."""
    fee_calculator = FeeCalc()

    term_field = int(request.form['terms'])
    term = None
    if term_field == 12:
        term = Term.TERM_12
    elif term_field == 24:
        term = Term.TERM_24

    loan_str = request.form['amount']
    if not loan_str:
        return render_template('Error.html')

    loan = int(loan_str)
#    if 1000 > loan or loan > 20000:
#        return render_template('Error.html')

    fee = fee_calculator.calculate(Data(loan, term))

    return render_template('calculate.html', number=loan, terms=term_field, calculated_fee=fee)


if __name__ == '__main__':
    app2.run(debug=True)
