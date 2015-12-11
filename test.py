
import urllib, socket, time, re

def open_file():
    fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
    counts = dict()
    for line in fhand:
        line.rstrip()
        words = line.split()
        # count words
        for word in words:
            counts[word] = counts.get(word,0) + 1
    print counts

def retr_image():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.py4inf.com', 80))
    mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n' )

    print "Debug: ", type(mysock)
    count = 0
    picture = ""

    while True:
        data = mysock.recv(5120)
        if (len(data) < 1) :
            break
        count = count + len(data)
        print "Debug: ", count, len(data)
        picture = picture + data
    mysock.close()

    # look for the end of the header
    pos = picture.find("\r\n\r\n")
    print "Header length: ", pos
    print picture[:pos]

    # Skip past the header and save the picture data
    picture = picture[pos+4:]
    fhand = open("stuff,jpg", "wb")
    fhand.write(picture)
    fhand.close()

#parsing Html using regex
def regex_html():
    url = raw_input("Enter a url - ")
    html = urllib.urlopen(url).read()
    found_links = re.findall('href="(http://.*?)"', html)

    for link in found_links:
        website_links = link.split()
        print link


#start and handle program flow
def start():
    print "Choose one of the following actions:"
    print "Open a file"
    print "Retrieve an image"

    action = raw_input("> ")
    if "file" in action:
        open_file()
    elif "image" in action:
        retr_image()
    elif "reg" in action:
        regex_html()

start()
