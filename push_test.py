import urllib.request
import requests, io, os
import numpy as np
import tarfile, zipfile, gzip

def unzip_from_UCI(UCI_url, dest=''):
    #ucl의 데이터 세트를 zip 포맷으로 다운로드하고 압축을 푼다.
    response = requests.get(UCI_url)
    compressed_file = io.BytesIO(response.content)
    z = zipfile.ZipFile(compressed_file)
    print('extracting in %s' % os.getcwd()+'\\'+dest)
    for name in z.namelist():
        if '.csv' in name:
            print('tunxipping %s' %name)
            z.extract(name, path=os.getcwd()+'\\'+dest)


def load_matrix(UCI_url):
    #uci의 데이터세트를 행렬 포맷으로 다운로드하고 압축을 푼다.
    return np.loadtxt(urllib.request.urlopen(UCI_url))




#what the hack?