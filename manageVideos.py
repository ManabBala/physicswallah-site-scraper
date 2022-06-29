import os
import shutil


def manageVideo(finalName, chapter):
    # f = open('new_video.txt', 'w')
    # f.close()
    modifiedFileName = finalName.replace(
        ':', '-').replace('||', '&').replace('|', '&') + '.mp4'
    modifiedChapter = chapter.replace(
        ':', '-').replace('||', '&').replace('|', '&')
    os.rename("new_video.mp4", modifiedFileName)
    try:
        os.mkdir('Biology')

    except OSError as error:
        print(error)
    try:
        os.mkdir('Biology\\'+modifiedChapter)

    except OSError as error:
        print(error)
    shutil.move(modifiedFileName, 'Biology\\'+modifiedChapter)


# manageVideo("final_video.mp4", 'Genetics')
