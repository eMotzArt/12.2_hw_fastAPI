import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ABS_FOLDER = os.path.join(ROOT_DIR, 'uploads', 'images')
UPLOAD_FOLDER = os.path.relpath(UPLOAD_ABS_FOLDER, ROOT_DIR)
pass