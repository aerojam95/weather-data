# =============================================================================
# Modules
# =============================================================================

# Python
import os

# Third-party
from flask import render_template, jsonify
import pandas as pd

# Custom
from custom_logger import get_custom_logger

# =============================================================================
# Initialise
# =============================================================================

logger = get_custom_logger("configurations/logger.yaml")

# =============================================================================
# Variables
# =============================================================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data_small")


# =============================================================================
# Routes
# =============================================================================

def init_routes(app):
    """
    Initializes all the routes for the Flask application

    Args:
        app (Flask): The Flask application instance
    """
    
    # Home page
    @app.route("/")
    def home():
        """
        Serves the home page with a table displaying available stations

        Returns:
            str: Rendered HTML template with station data or an error message
        """
        
        filename = os.path.join(DATA_DIR, "stations.txt")
        logger.debug(f"Lauching web app...")
        
        try:
            stations = pd.read_csv(filename, skiprows=17)
            stations = stations[["STAID", "STANAME                                 "]]
            logger.debug(f"Lauched web app")
            return render_template("home.html", data=stations.to_html())
        
        except Exception as e:
            return jsonify({"error": f"Failed to load stations: {str(e)}"}), 500

    
    # Data for a station at a given date API
    @app.route("/api/v1/<station>/<date>")
    def get_temperature_station_date(station, date):
        """
        Fetches the temperature data for a specific station and date

        Args:
            station (str): The station ID
            date (str): The date in YYYY-MM-DD format

        Returns:
            dict: JSON response containing station ID, date, and temperature
        """
        
        logger.debug(f"Retrieving data for station {station} from {date}...")
        filename = os.path.join(DATA_DIR, f"TG_STAID{str(station).zfill(6)}.txt")

        try:
            df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
            temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
            logger.debug(f"Retrieved data for station {station} from {date}")
            return jsonify({"station": station, "date": date, "temperature": temperature})
        
        except Exception as e:
            return jsonify({"error": f"Data retrieval failed: {str(e)}"}), 500

    # Data for a station API
    @app.route("/api/v1/<station>")
    def get_all_temperature_station(station):
        """
        Retrieves all available temperature data for a specific station

        Args:
            station (str): The station ID

        Returns:
            list: JSON response containing all records as a list of dictionaries
        """
        
        logger.debug(f"Retrieving all data for station {station}...")
        filename = os.path.join(DATA_DIR, f"TG_STAID{str(station).zfill(6)}.txt")

        try:
            df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
            logger.debug(f"Retrieved all data for station {station}")
            return jsonify(df.to_dict(orient="records"))
        
        except Exception as e:
            return jsonify({"error": f"Failed to retrieve station data: {str(e)}"}), 500

    
    # Data for a station for a given year API
    @app.route("/api/v1/yearly/<station>/<year>")
    def get_yearly_temperature_station(station, year):
        """
        Retrieves temperature data for a specific station and year

        Args:
            station (str): The station ID
            year (str): The year in YYYY format

        Returns:
            list: JSON response containing all records for the given year
        """
        
        logger.debug(f"Retrieving all data for station {station} for the year {year}...")
        filename = os.path.join(DATA_DIR, f"TG_STAID{str(station).zfill(6)}.txt")

        try:
            df = pd.read_csv(filename, skiprows=20)
            df["    DATE"] = df["    DATE"].astype(str)
            result = df[df["    DATE"].str.startswith(str(year))]
            logger.debug(f"Retrieved all data for station {station} for the year {year}")
            return jsonify(result.to_dict(orient="records"))
        
        except Exception as e:
            return jsonify({"error": f"Failed to retrieve yearly data: {str(e)}"}), 500