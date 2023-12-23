from api.v1 import create_app
from api.v1.config import CURRENT_CONFIG

app = create_app()

if __name__ == "__main__":
    app.run(debug=CURRENT_CONFIG.DEBUG, port=8080)

