"""Balance Module"""
from app import app

@app.get('/account/<int:account_id>/balance')
def retrieve_balance():
    return {}
