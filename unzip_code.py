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

def gzip_from_UCI(UCI_url, dest=''):
    response = requests.get(UCI_url)
    compressed_file = io.BytesIO(response.content)
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    filename = UCI_url.split('/')[-1][:3]
    with open(os.getcwd()+'\\'+filename, 'wb') as outfile:
        outfile.write(decompressed_file.read())
        print('file %s decompressed % filename')

def targzip_from_UCI(UCI_url, dest=''):
    response = urllib.request.urlopen(UCI_url)
    compressed_file = io.StringIO(response.read())
    tar = tarfile.open(mode="r:gz", fileobj=compressed_file)
    tar.extract(path=dest)
    datasets = tar.getnames()
    for dataset in datasets:
        size = os.path.getsize(dest+'\\'+dataset)
        print('file %s is %i byte' % (dataset, size))

def load_matrix(UCI_url):
    #uci의 데이터세트를 행렬 포맷으로 다운로드하고 압축을 푼다.
    return np.loadtxt(urllib.request.urlopen(UCI_url))