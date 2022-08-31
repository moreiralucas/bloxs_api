"""Account Module"""
from app import app


@app.post('/account')
def create_account():
    """Create account"""
    return {'message': 'created'}, 201
