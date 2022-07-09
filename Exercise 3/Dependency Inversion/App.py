from VideoPlayer import VideoPlayer

class App:

    def __init__(self, videoPlayer : VideoPlayer):
        self.videoPlayer = videoPlayer

    def begin(self):
        print("Ready to play video.")
        print(f"Registered video player is {self.videoPlayer.__class__.__name__}.")
        self.videoPlayer.play()