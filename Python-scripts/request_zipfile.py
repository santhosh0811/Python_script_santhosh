import zipfile, urllib.request, shutil

url = 'https://www2.census.gov/geo/tiger/GENZ2017/shp/cb_2017_02_tract_500k.zip'
file_name = 'cb_2017_02_tract_500k.Zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()
