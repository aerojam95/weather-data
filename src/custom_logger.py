# =============================================================================
# Modules
# =============================================================================

# Python modules
import logging
import logging.config

# Third-party modules
import yaml

# =============================================================================
# Variables
# =============================================================================

# Set up a temporary logger before loading the YAML configuration
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
setup_logger = logging.getLogger("setup_logger")

# =============================================================================
# Functions
# =============================================================================


def get_custom_logger(yaml_config_file_path: str):
    """Set up logger based on configuration from a YAML file

    Args:
        yaml_config_file_path (str): 
            The path to the YAML file containing the logging configuration

    Returns:
        logging.Logger: Configured logger instance

    Raises:
        FileNotFoundError: If the file does not exist
        yaml.YAMLError: If there's an error parsing the YAML file
    """
    # Log function entry
    setup_logger.debug(f"Generating logger from {yaml_config_file_path} ...")

    try:
        # Load logging configuration from YAML file
        with open(yaml_config_file_path, "r") as file:
            config = yaml.safe_load(file)
        setup_logger.debug(f"Configuration data: {config}")
        
        # Apply the logging configuration
        logging.config.dictConfig(config["logging"])

        # Dynamically get the logger's name from YAML configuration
        logger_name = next(
            iter(config["logging"]["loggers"]),"default_logger"
        )
        setup_logger.debug(f"Logger name: {logger_name}")
        
        # Use the logger name dynamically
        logger = logging.getLogger(logger_name)
        setup_logger.debug(
            f"Generated {logger_name} from {yaml_config_file_path}"
        )
        return logger

    except FileNotFoundError as fe:
        setup_logger.critical(
            f"FileNotFoundError: {fe}"
        )
        raise

    except yaml.YAMLError as ye:
        setup_logger.critical(
            f"YAMLError: {ye}"
        )
        raise

    except Exception as e:
        setup_logger.error(
            f"Error: {e}"
        )
        raise