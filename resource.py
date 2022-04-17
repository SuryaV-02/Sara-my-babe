class resource(object):
    def __init__(self):
        self.q_current_activity = ['doing', 'free', 'bored', 'boring','help']
        self.q_play_song = ['play','song','boring']
        self.q_wiki =  ['what','where','who','know','define']
        self.bad_personality = ['may','fuck','ass','kick']
        self.romantic = ['darling', 'babe', 'baby', 'love']
        self.dt = ['today','date','time','now']

        # self.r_my_activities = ['watching Movie', 'reading book', 'dancing at my Pi Party hall','learning to paint','mastering a new language','learning how to play an instrument',
        #                         'trying some magic tricks','flying Kite', 'Scuba diving','Riding roller coasters','windsurfing','Study the Titanic','Making gingerbread houses']
        self.r_my_activities = ['curing swine flu','fighting crime','trying to imagine you with a personality','curing cancer','Taking a mental hiatus','trying some magic tricks','flying Kite', 'Scuba diving',
                                'Riding roller coasters','windsurfing','Study the Titanic','Making gingerbread houses']
        self.r_post_fillers = ['what can I do for you?','let me know maybe I can see what I can do','may I join my hands with you?',
                          'what best help can I do for you?','need some help?',
                          'find your patience before I lose mine']
        self.r_harsh_response = ['I think you should mind your own business','Are you always such an idiot, or do you just show off when I’m around?',
                                 'Umm...pardon me, I wasn’t listening. Can you repeat what you just said?','Sorry, I don’t understand what you’re saying. I don’t speak bullshit',
                                 'Were you born on the highway? That is where most accidents happen','I believed in evolution until I met you']



        self.r_romantic = ['I love you, mi amour!','Who, me? Are you serious? This crazy, neurotic me? Well, you like weird stuff!','Our forever is going to be beautiful',
                           'I am gonna faint!','With that, it’s now time for action','You are my baby, and you know that','There is no need for words. Your smile says it all',
                           'I would like to record your voice saying these words so I can listen to them again and again','Awww! I love you too!']
        self.queries=[self.q_current_activity,self.q_play_song, self.q_wiki, self.bad_personality,self.romantic,self.dt]
        self.r_pre_fillers = ['I was']

        self._q_genere = {
            0 : 'activity',
            1 : 'song',
            2 : 'wiki',
            3 : 'badperson',
            4 : 'love',
            5: 'dt'
        }