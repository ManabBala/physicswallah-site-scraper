import json
import time
import videoLinkApi
import policyParamApi
import videoDownloader
import manageVideos

topicDataJson = open(
    'F:\\Manab World Backup\\Manab Workspace\\GITHUB\\physicswallah-site-scraper\\topicLink.json')
topicData = json.load(topicDataJson)

print(len(topicData))

i = 0
while i < len(topicData):
    topicName = topicData[i]['name']
    topicTag = topicData[i]['_id']
    print(str(i)+")"+topicName+"\nTopic Tag:" + topicTag)
    videoLinkData = videoLinkApi.getVideoLink(topicTag)
    # print(len(videoLinkData))
    j = 0
    while j < len(videoLinkData):
        videoDetails = videoLinkData[j]['videoDetails']
        videoName = videoDetails['name']
        videoUrl = videoDetails['videoUrl']
        policyData = policyParamApi.get_policy(videoUrl)
        time.sleep(.3)
        # print(videoName)
        # print(videoUrl)
        # print(policyData)
        # manageVideos.manageVideo(videoName, topicName)
        videoDownloader.downloadVideo(
            videoName, topicName, videoUrl, policyData)
        # time.sleep(86400)
        j = j + 1

    i = i + 1
