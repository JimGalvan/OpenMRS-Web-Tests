from pathlib import Path

ROOT_PROJECT_FOLDER_INDEX = 3
CONFIG_FILE_PATH = '\\src\\resources\\config.properties'


def get_project_root() -> Path:
    return Path(__file__).absolute().parents[ROOT_PROJECT_FOLDER_INDEX]


def get_config_path():
    return str(get_project_root()) + CONFIG_FILE_PATH
