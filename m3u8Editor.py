import os
import requests


def editLinkFile(tempName, baseUrl, policyData, resolution='720'):
    url = baseUrl[0:-11]+"/hls/"+resolution+"/main.m3u8"+policyData
    r = requests.get(url)

    open('temp'+tempName+'.m3u8', 'wb').write(r.content)
    mainLink = open('temp'+tempName+'.m3u8', 'r')

    with open(tempName+'.m3u8', 'w') as finalLink:
        for line in mainLink:
            if line.startswith('#'):
                finalLink.write(line)
            else:
                newLine = baseUrl[0:-11] + \
                    "/hls/"+resolution+"/"+line[0:-1]+policyData+'\n'
                finalLink.write(newLine)
        mainLink.close()
        os.remove('temp'+tempName+'.m3u8')
