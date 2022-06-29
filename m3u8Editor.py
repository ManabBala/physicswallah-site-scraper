import requests


def editLinkFile(baseUrl, policyData):
    url = baseUrl[0:-11]+"/hls/480/"+"main.m3u8"+policyData
    r = requests.get(url)

    open('main.m3u8', 'wb').write(r.content)
    mainLink = open('main.m3u8', 'r')

    with open('Final_Link.m3u8', 'w') as finalLink:

        for line in mainLink:
            if line.startswith('#'):
                finalLink.write(line)
            else:
                newLine = baseUrl[0:-11] + \
                    "/hls/480/"+line[0:-1]+policyData+'\n'
                print(newLine)
                finalLink.write(newLine)
        print(finalLink)
