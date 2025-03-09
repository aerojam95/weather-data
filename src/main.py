# =============================================================================
# Modules
# =============================================================================

# Python
import argparse

# Custom
from custom_logger import get_custom_logger

# =============================================================================
# Variables
# =============================================================================

# Logging
logger = get_custom_logger("data/configurations/logger.yaml")

# =============================================================================
# Programme exectuion
# =============================================================================

if __name__ == "__main__":
    
    # Parsed values
    parser = argparse.ArgumentParser(description="endpoint from which to request API data")