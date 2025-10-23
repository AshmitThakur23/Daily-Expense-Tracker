from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        note = request.form['note']

        new_expense = {
            'amount': amount,
            'category': category,
            'date': date,
            'note': note
        }

        expenses = load_expenses()
        expenses.append(new_expense)
        save_expenses(expenses)

        return redirect(url_for('index'))

    expenses = load_expenses()
    summary = {}

    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    categories = list(summary.keys())
    amounts = list(summary.values())

    return render_template(
        'index.html',
        expenses=expenses,
        categories=categories,
        amounts=amounts,
        today=datetime.now().strftime('%Y-%m-%d')
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

