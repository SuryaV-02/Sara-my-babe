class resource(object):
    def __init__(self):
        self.q_current_activity = ['doing', 'free', 'now', 'bored', 'boring']
        self.q_play_song = ['play','song','boring']
        self.q_wiki =  ['what','where','who','know','define']


        self.r_my_activities = ['watching Movie', 'reading book', 'dancing at my Pi Party hall']
        self.r_post_fillers = ['what can I do for you?','let me know maybe I can see what I can do','may I join my hands with you?',
                          'what best help can I do for you?','tell me what I can do.','need some help?',
                          'let me make things better for you']

        self.queries=[self.q_current_activity,self.q_play_song, self.q_wiki]
        self.r_pre_fillers = ['I was']

        self._q_genere = {
            0 : 'activity',
            1 : 'song',
            2 : 'wiki'
        }