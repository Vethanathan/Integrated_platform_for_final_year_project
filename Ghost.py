import requests
import zipfile
from io import BytesIO


def gimme_string(url):
    response = requests.get(url)
    print(response.status_code)
    d={}
    zip_file = BytesIO(response.content)
    with zipfile.ZipFile(zip_file) as z:
        for i in range(len(z.namelist())):
            file_name = z.namelist()[i]
            try:
                file_content = z.read(file_name)
                file_content_str = file_content.decode("utf-8")
                d[file_name]=file_content_str
            except:
                pass

    return d
