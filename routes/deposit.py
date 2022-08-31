"""Deposit Module"""
from app import app
@app.put('/account/<int:account_id>/deposit')
def deposit_account(account_id):
    return {}
