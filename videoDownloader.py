import json
import os
import time
import m3u8Editor
import shutil
import policyParamApi
import concurrent.futures


current_downloading = 0
concurrent_download = 3


def downloadVideo(videoName, chapter, baseUrl):
    policyData = policyParamApi.get_policy(baseUrl)

    i = 0
    tempName = "main0"
    while os.path.exists(tempName[0:-1]+str(i)+'.m3u8'):
        i = i+1
        tempName = tempName[0:-1]+str(i)
        time.sleep(4)

    m3u8Editor.editLinkFile(tempName, baseUrl, policyData, '720')

    link = 'ffmpeg -protocol_whitelist file,https,tcp,tls,crypto -i ' + \
        tempName+'.m3u8'+' -c copy -bsf:a aac_adtstoasc '+tempName+'.mp4'

    try:
        global current_downloading
        current_downloading += 1
        print("current downloading: "+str(current_downloading))
        os.system(link)
        if os.path.exists(tempName+'.mp4'):
            manageVideo(tempName, videoName, chapter)
        os.remove(tempName+'.m3u8')
        current_downloading -= 1
        print("current downloading: "+str(current_downloading))
    except OSError as e:
        print(e)
        current_downloading -= 1
        print("current downloading: "+str(current_downloading))
        os.remove(tempName+'.m3u8')


def manageVideo(tempName, finalName, chapter):
    # f = open('new_video.txt', 'w')
    # f.close()
    modifiedFileName = finalName.replace(
        ':', '-').replace('||', '&').replace('|', '&') + '.mp4'
    modifiedChapter = chapter.replace(
        ':', '-').replace('||', '&').replace('|', '&')
    os.rename(tempName+'.mp4', modifiedFileName)
    try:
        os.mkdir('Biology')

    except OSError as error:
        print(error)
    try:
        os.mkdir('Biology\\'+modifiedChapter)

    except OSError as error:
        print(error)
    shutil.move(modifiedFileName, 'Biology\\' + modifiedChapter)


def initiate_download():
    videoDataJson = open(
        'F:\\Manab World Backup\\Manab Workspace\\GITHUB\\physicswallah-site-scraper\\videoLink.json')
    videoData = json.load(videoDataJson)

    for video in videoData:
        # print(video)
        if video['downloaded'] == False:
            downloadVideo(video['videoName'],
                          video['topicId'],
                          video['baseUrl'])


initiate_download()


# def downloader_thread(vidDetails):
#     print(vidDetails['videoName'])
#     downloadVideo(vidDetails['videoName'],
#                   vidDetails['topicName'],
#                   vidDetails['baseUrl'])


# with concurrent.futures.ThreadPoolExecutor(4) as executor:
#     executor.map(downloader_thread, videoData)
