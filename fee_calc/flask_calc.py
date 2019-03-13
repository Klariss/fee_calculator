from flask import Flask, render_template, request
from calculator import FeeCalc, Term
from calculator import LoanData

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """A simple page, where parameters can be given."""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
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

    loan = int(loan_str)

    fee = fee_calculator.calculate(LoanData(loan, term))

    return render_template('calculate.html', number=loan, terms=term_field, calculated_fee=fee)


if __name__ == '__main__':
    app.run(debug=True)
