import os
import csv
local_path = os.getcwd()
source = 'bikesharing\\hour.csv'
SEP = ' ' #파일에 명시된 구분자로 쉽게 변경할 수 있도록 정의한다.
# with open(local_path+'\\'+source, 'rt') as R:
#     iterators = csv.reader(R, delimiter=SEP)
#     for n, row in enumerate(iterators):
#         if n == 0:
#             header = row
#         else:
#             pass
#     print('total rows : %i' % (n+1))
#     print('header: %s' % ','.join(header))
#     print('Sample values: %s' % '%'.join(row))

with open(local_path+'\\'+source, 'r') as R:
    iterator = csv.DictReader(R)
    a = ""
    b = ""
    for n, row in enumerate(iterator):
        pass

    for key in row.keys():
        if key != "instant":
            a = a + ','
            b = b + ','
        a = a + row[key]
        b = b + key

    print(a)
    print(b)
    print('{0}'.format(n+1))
    print('{0}'.format(row))
    print('{0}'.format(row['instant']))
