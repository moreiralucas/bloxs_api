from app import app
@app.post('/account/<int:account_id>/block')
def block_account():
    return {}
