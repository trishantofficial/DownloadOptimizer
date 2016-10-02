from urllib2 import Request, urlopen
from multiprocessing import Process
from urllib import unquote
from psutil import pid_exists
from os import remove


def download(url, part, x, fileName):
    threadNumber = x
    fileName = str(fileName) + '.' + str(threadNumber)
    headers = 'Content-Length: ' + str(part)
    request = Request(url)
    request.add_header('Range', 'bytes=' + str(part))
    #print request.headers
    result = urlopen(request)
    data = result.read()
    with open(fileName, "wb") as code:
        code.write(data)
    print 'Thread' + str(threadNumber) + ' stopped.'
    #return fileName

def main():
    url = raw_input('Enter URL: ')
    response = urlopen(url)
    acceptRanges = response.info().getheader('Accept-Ranges')
    fileSize = response.info().getheader('Content-Length')
    fileType = response.info().getheader('Content-Type')
    fileName = str(unquote(str(url).split('/').pop()).decode('utf8'))
    print '[*] File type: ' + fileType
    print '[*] File size: ' + fileSize
    print '[*] Accepts ranges: ' + acceptRanges
    if str(acceptRanges) != None or str(acceptRanges) != '':
        multiDownload = True
        print '\n\tThis file can be downloaded in parts.'
    partitions = raw_input('Enter number of partitions: ')
    if multiDownload is True:
        parts = []
        partitionSize = int(fileSize) / int(partitions)
        print '\t\t' + str(partitionSize) + ' bytes per part.'
        print '\t\t' + str(partitionSize/1024) + ' kb per part'
        x = 0
        for partition in range(int(partitions)):
            parts.append(str(x) + '-' + str(x + partitionSize))
            x = x + partitionSize
        x = 0
        processList = []
        for part in parts:
            process = Process(target=download, args=(url, part, str(x), fileName))
            process.start()
            processList.append(process)
            print 'Thread' + str(x+1) + ' started'
            x = x + 1
        while len(processList) != 0:
            for processes in processList:
                if not pid_exists(processes.pid):
                    print 'Process with pid=' + str(processes.pid) + ' ended'
                    processes.join()
                    processList.remove(processes)
        print 'Download complete! :)'
        print 'Compiling now.....'
        to_file = open(fileName, 'wb')
        for chunk in range(int(partitions)):
            tmp = fileName + '.' + str(chunk)
            from_file = open(tmp, 'rb')
            to_file.write(from_file.read())
            from_file.close()
            remove(tmp)
        to_file.close()
        print 'Compiled!!'