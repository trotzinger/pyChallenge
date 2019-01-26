'''challenge 6 channel.html channel.zip
'''

import zipfile

pathtozip = r"channel.zip"

zinfo = zipfile.ZipFile(pathtozip).infolist()
data = {z.filename : z for z in zinfo}
def findnext(filename):
    with zipfile.ZipFile(pathtozip) as myzip:
        with myzip.open(filename) as current:
            #print (current.read())
            return ''.join(filter(lambda x : x.isdigit(), str(current.read())))
nextnum = (findnext("90052.txt"))
comments = []
while True:
    #print(nextnum)
    nextnum = findnext(("{}.txt".format(nextnum)))
    try:
        comments.append(data["{}.txt".format(nextnum)].comment)
    except KeyError as e:
        break
#print(comments)
cleancom = ''.join([x.decode("utf-8") for x in comments])
print(cleancom)
