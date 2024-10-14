import os
from flask import Flask
from flask_migrate import Migrate
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)

@app.cli.command('run')
def run():
    """Run the Flask app."""
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
