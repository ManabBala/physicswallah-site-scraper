import os
import m3u8Editor
import manageVideos


def downloadVideo(videoName, chapter, baseUrl, policyData):

    m3u8Editor.editLinkFile(baseUrl, policyData)

    link = 'ffmpeg -protocol_whitelist file,https,tcp,tls,crypto -i Final_Link.m3u8 -c copy -bsf:a aac_adtstoasc new_video.mp4'

    os.system(link)
    print("\033[1;32m"+str("#"*20))
    manageVideos.manageVideo(videoName, chapter)
