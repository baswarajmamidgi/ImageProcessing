import urllib2
file=open('videofilesurl.txt','r')

lines=file.readlines()
for line in lines:
    data=line.split(",")
    #print(data[0]+':'+data[1]) data[0] file name  and data[1] video file url

    response = urllib2.urlopen(data[1])
    print (data[1])
    with open(data[0]+'.webm', 'wb') as f:
        f.write(response.read())
