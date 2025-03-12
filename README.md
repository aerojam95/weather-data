# Weather data API

A web-application that generates a REST API for weather data of European locations. The API allows users to fetch weather data for specific locations, for a specific location over all the available records, and weather data for a year at a given location using different REST API endpoints.

## Table of Contents

- [API](#api)
- [Data](#data)
- [Code](#code)
    - [Python virtual environment](#python-venv)
    - [Programme execution](#execution)
    - [Using API endpoints](#using-api-endpoints)

## REST API

The Weather Data API exposes three endpoints to retrieve weather data.

## Data

The weather data is sourced from various publicly available weather APIs, for locations around Europe. The data includes temperature, location, date, and time. There are plenty of historic data available for those needing siginificant data for long term trends, as well as a high frequency of measurements for volume. 

## Code

### Python virtual environment

Before using the programme it is best to setup and start a Python virtual environment in order to avoid potential package clashes using the [requirements](requirements.txt) file:

```BASH
# Navigate into the project directory

# Create a virtual environment
python3 -m venv email-daily-news

# Activate virtual environment
source email-daily-news/bin/activate

# Install dependencies for code
pip3 install -r requirements.txt

# When finished with virtual environment
deactivate
```

### Programme Execution

To get the website running on the localhost (set the port in the routes.py file)

```Bash
# Navigate into the root of the project directory
python3 app.py
```

### Using API endpoints

The webpage should be able to be reached at `localhost:<PORT>` or online based environments `https://127.0.0.1:<PORT>`.

Endpoints that can be accessed are:

1. `localhost:<PORT>/`: to get to the home page of website and documentation for the endpoints of the REST API
2. `localhost:<PORT>/api/v1/<station>/<date>`: to get the data for a given measurement station on a given day
3. `localhost:<PORT>/api/v1/<station>`: to get all the data for a given measurement station
4. `localhost:<PORT>/api/v1/yearly/<station>/<year>`: to get the data for a given measurement station for a given year
