from ismi import download_data
from pathlib import Path
import shutil

file_name = Path("/tmp/dummy.zip")
link = "https://getsamplefiles.com/download/zip/sample-3.zip"
extract_dir = Path("/tmp/dummy_zip")
download_data(file_name, link, extract_dir)

file_name.unlink()
shutil.rmtree(extract_dir)
