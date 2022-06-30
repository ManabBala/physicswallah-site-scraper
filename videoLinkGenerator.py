import json
import videoLinkApi
import policyParamApi
import time


topicDataJson = open(
    'F:\\Manab World Backup\\Manab Workspace\\GITHUB\\physicswallah-site-scraper\\topicLink.json')
topicData = json.load(topicDataJson)

videoLinkObj = []

i = 0
for topic in topicData:
    topicName = topic['name']
    topicId = topic['_id']
    print(str(i)+")"+topicName)

    videoLinkData = videoLinkApi.getVideoLink(topicId)

    for videoLink in videoLinkData:
        videoDetails = videoLink['videoDetails']
        videoName = videoDetails['name']
        videoId = videoDetails['id']
        videoUrl = videoDetails['videoUrl']
        videoDuration = videoDetails['duration']
        print(videoName)

        policyParam = policyParamApi.get_policy(videoUrl)

        VideoLinkDic = {
            "topicName": topicName,
            "topicId": topicId,
            "videoId": videoId,
            "baseUrl": videoUrl,
            "videoName": videoName,
            "videoDuration": videoDuration,
            "policyParam": policyParam,
            "downloaded": False
        }
        videoLinkObj.append(VideoLinkDic)
        time.sleep(.2)

    i = i+1
    time.sleep(.2)

print(videoLinkObj)

with open('videoLink.json', 'w') as f:
    json.dump(videoLinkObj, f)
