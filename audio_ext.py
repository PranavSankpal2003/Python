#pip install moviepy -- It is used to extract audio from video files. And aslo it is used for video editing and multimedia manipulating.

import moviepy.editor as mpe

cvt_video = mpe.VideoFileClip("Test.mkv")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("test1.mp3")