"""Withdraw Module"""
from app import app

@app.post('/account/<int:account_id>/withdraw/')
def withdraw(account_id):
    return {}
