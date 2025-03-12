# =============================================================================
# Modules
# =============================================================================

# Third-party
from flask import Flask
from routes import init_routes

# Custom
from custom_logger import get_custom_logger

# =============================================================================
# Variables
# =============================================================================

PORT = 5000
DEBUG = True

# =============================================================================
# Initialise
# =============================================================================

logger = get_custom_logger("configurations/logger.yaml")
app = Flask(__name__)
init_routes(app)

# =============================================================================
# Application exectuion
# =============================================================================

if __name__ == "__main__":
    
    logger.info(f"Running web application {app}...")
    app.run(debug=DEBUG, port=PORT)