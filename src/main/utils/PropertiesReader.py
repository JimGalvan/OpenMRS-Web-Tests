from pathlib import Path

from jproperties import Properties


class PropertiesReader:
    ROOT_PROJECT_FOLDER_INDEX = 3

    def __init__(self, properties_path):
        self.properties_path = properties_path

    def get_project_root(self):
        return Path(__file__).absolute().parents[self.ROOT_PROJECT_FOLDER_INDEX]

    def get_value(self, key):
        configs = Properties()
        config_file_path = str(self.get_project_root()) + self.properties_path

        with open(config_file_path, 'rb') as read_prop:
            configs.load(read_prop)

        return str(configs.get(key).data).strip().lower()
