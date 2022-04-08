class resource(object):
    def __init__(self):
        self.q_current_activity = ['doing', 'free', 'now', 'bored', 'boring']
        self.q_play_song = ['play','song','boring']
        self.q_wiki =  ['what','where','who','know','define']



        # self.r_my_activities = ['watching Movie', 'reading book', 'dancing at my Pi Party hall','learning to paint','mastering a new language','learning how to play an instrument',
        #                         'trying some magic tricks','flying Kite', 'Scuba diving','Riding roller coasters','windsurfing','Study the Titanic','Making gingerbread houses']
        self.r_my_activities = ['curing swine flu','fighting crime','trying to imagine you with a personality','curing cancer','Taking a mental hiatus','trying some magic tricks','flying Kite', 'Scuba diving',
                                'Riding roller coasters','windsurfing','Study the Titanic','Making gingerbread houses']
        self.r_post_fillers = ['what can I do for you?','let me know maybe I can see what I can do','may I join my hands with you?',
                          'what best help can I do for you?','need some help?',
                          'find your patience before I lose mine']

        self.queries=[self.q_current_activity,self.q_play_song, self.q_wiki]
        self.r_pre_fillers = ['I was']

        self._q_genere = {
            0 : 'activity',
            1 : 'song',
            2 : 'wiki'
        }