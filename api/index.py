import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_mysql import app, init_db
from flask import jsonify

@app.route('/setup-db')
def setup_db():
    try:
        init_db()
        return jsonify({"status": "ok", "message": "Tables created successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
