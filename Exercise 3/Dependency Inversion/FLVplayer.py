class App:

    def __init__(self, videoPlayer : VideoPlayer):
        self.videoPlayer = videoPlayer

    def begin(self):
        self.videoPlayer.play()
