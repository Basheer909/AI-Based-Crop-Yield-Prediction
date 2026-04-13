"""
SmartKisan AI — AI-Powered Crop Yield Prediction & Optimization
Entry point: python run.py
"""

import sys
import os

# Ensure the project root is on the path so 'app' and 'config' import correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == '__main__':
    # use_reloader=False  ← fixes "SystemExit: 3" in VS Code debugger.
    # Flask's reloader spawns a child process that conflicts with debugpy.
    # debug=True is kept so you still get helpful error pages in the browser.
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=False
    )
