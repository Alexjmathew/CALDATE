from flask import Flask, render_template, request
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route to display the form and the calculated result.
    """
    result = None
    from_date_str = ''
    to_date_str = ''

    if request.method == 'POST':
        # Get date strings from the form
        from_date_str = request.form['from_date']
        to_date_str = request.form['to_date']

        # Ensure both dates are provided
        if from_date_str and to_date_str:
            # Convert string dates to datetime objects
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

            # Calculate the difference using relativedelta for accurate results
            difference = relativedelta(to_date, from_date)

            result = {
                'years': difference.years,
                'months': difference.months,
                'days': difference.days
            }

    # Render the HTML page, passing the result and submitted dates
    return render_template('index.html', result=result, from_date=from_date_str, to_date=to_date_str)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.102', port=80)