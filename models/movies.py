class Movie:
    def __init__(self,args):
        self._background = 'https://image.tmdb.org/t/p/original'+args['backdrop_path']
        self._id = args['id']
        self._poster = 'https://image.tmdb.org/t/p/original'+args['poster_path']
        self._overview = args['overview']
        self._title = args['title']
        self._vote = args['vote_average']
    
    @property
    def background(self):
        return self._background
    
    @property
    def id(self):
        return self._id
    
    @property
    def poster(self):
        return self._poster
    
    @property
    def overview(self):
        return self._overview
    
    @property
    def title(self):
        return self._title
    
    @property
    def vote(self):
        return self._vote
    
    def to_dict(self):
        return {
            'background': self.background,
            'id': self.id,
            'poster': self.poster,
            'overview': self.overview,
            'title': self.title,
            'vote': self.vote,
        }