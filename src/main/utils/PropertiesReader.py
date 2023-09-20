from pathlib import Path
from src.main.utils.logger import logger
from jproperties import Properties


def get_config_properties():
    return PropertiesReader("\\src\\resources\\config.properties")


class PropertiesReader:
    ROOT_PROJECT_FOLDER_INDEX = 3

    def __init__(self, properties_path):
        """
        Initialize the PropertiesReader instance.

        Args:
            properties_path (str): Path to the properties file.
        """
        self.properties_path = properties_path

    def get_project_root(self):
        """
        Get the root folder of the project.

        Returns:
            Path: The absolute path to the root folder of the project.
        """
        return Path(__file__).absolute().parents[self.ROOT_PROJECT_FOLDER_INDEX]

    def get_value(self, key):
        """
        Get the value associated with the given key from the properties file.

        Args:
            key (str): The key for which to retrieve the value.

        Returns:
            str: The value associated with the key, converted to lowercase and stripped of whitespace.
        """
        configs = Properties()
        config_file_path = str(self.get_project_root()) + self.properties_path

        with open(config_file_path, 'rb') as read_prop:
            configs.load(read_prop)

        value = str(configs.get(key).data).strip().lower()
        # Log the key and corresponding value
        logger.info(f"Key: {key}, Value: {value}")
        return value
