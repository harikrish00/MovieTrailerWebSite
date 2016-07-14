import webbrowser
"""Movie class to hold information about any movie with the following attributes

    Attributes:
        title (str): Movie original title
        story_line (str): Long string explaining the storyline of the movie
        poster_image_url(str): url string linking to an actual image on the internet
        trailer_youtube_url(str): youtube url pointing to trailer of the movie
    """
class Movie():

    VALID_RATINGS = ['R','PG','PG13','NR']
    def __init__(self, title, story_line, poster_image, trailer):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    # this function opens a browser and play thr trailer using trailer_youtube_url variable
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
