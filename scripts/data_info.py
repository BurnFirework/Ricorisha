from pathlib import Path

DEFAULT_DATA_LOCATION = '../combined'

def get_all_image_files(data_path):
    p = Path(data_path)
    return list(p.glob('*.jpg'))

def get_all_json_files(data_path):
    p = Path(data_path)
    return list(p.glob('*.json'))
