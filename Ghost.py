import requests
import zipfile
from io import BytesIO


def gimme_string(url):
    # url = "https://hzmzxhzqslaoahheatdf.supabase.co/storage/v1/object/public/vetha/test_dir.zip"
    response = requests.get(url)
    print(response.status_code)
    d={}
    zip_file = BytesIO(response.content)
    with zipfile.ZipFile(zip_file) as z:
        for i in range(len(z.namelist())):
            file_name = z.namelist()[i]
            file_content = z.read(file_name)
            file_content_str = file_content.decode("utf-8")
            d[file_name]=file_content_str

    return d
