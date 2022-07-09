### DEPENDENCY INVERSION PRINCIPLE
# Assuming that we have an App that has many video types available to play.
# Usind the Dependency Inversion Principle, we made an abstract class (VideoPlayer) that will handle the job of playing a video.
# Every video codec class can inherit from VideoPlayer in order to make all codecs available for the App.

from App import App
from MP4player import MP4player
from FLVplayer import FLVplayer

# works for mp4.
mp4_player = MP4player()
app_mp4 = App(mp4_player)
app_mp4.begin()

print("")

#works for flv.
flv_player = FLVplayer()
app_flv = App(flv_player)
app_flv.begin()