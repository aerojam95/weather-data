# =============================================================================
# Modules
# =============================================================================

# Python
import argparse

# Third-party
from flask import Flask, render_template
import pandas as pd

# Custom
from custom_logger import get_custom_logger

# =============================================================================
# Variables
# =============================================================================

# Logging
logger = get_custom_logger("configurations/logger.yaml")

app = Flask(__name__)


# =============================================================================
# Functions
# =============================================================================
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    #temperature = df.station(date)
    temperature = "23"
    return {"station": station, "date": date, "temperature": temperature}

# =============================================================================
# Programme exectuion
# =============================================================================

if __name__ == "__main__":
    
    # Parsed values
    parser = argparse.ArgumentParser(description="")
    
    app.run(debug=True, port=5000)