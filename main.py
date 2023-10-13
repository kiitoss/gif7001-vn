import uvicorn
from app.api import app

if __name__ == '__main__':
    # Run the application
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

    # Uvicorn will be runnning on http://localhost:8000 (Press CTRL+C to quit)
