import webbrowser

class Movie():

    VALID_RATINGS = ['R','PG','PG13','NR']
    def __init__(self,title, story_line, poster_image, trailer):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
