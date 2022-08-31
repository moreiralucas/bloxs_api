"""Extract Module"""
from app import app
@app.get('/account/<int:account_id>/extract')
def extract_account(account_id):
    return {}
