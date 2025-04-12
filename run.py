import os
from app import app

if __name__ == "__main__":
    # Get the PORT environment variable for deployment, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # Change `debug=False` in production
