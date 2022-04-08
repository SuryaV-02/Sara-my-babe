import random
from typing import List

from resource import resource
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from accessibilities import search_wiki


class Model(resource):
    def __init__(self):
        super().__init__()
        # nltk.download('punkt')
        # nltk.download('stopwords')
        # nltk.download('averaged_perceptron_tagger')
        self.my_acts = self.r_my_activities

    def get_current_activity(self):
        return random.choice(self.my_acts)

    def get_tokens(self, sentence):
        tokens = word_tokenize(sentence)
        stop_words = set(stopwords.words('english'))
        clean_tokens = [word for word in tokens if word.lower() not in stop_words]
        return clean_tokens

    def get_raw_tokens(self, sentence):
        tokens = word_tokenize(sentence)
        return tokens

    def get_genre(self,tokens):
        # tokens = [token for token.lower() in token]
        tokens = list((map(lambda x: x.lower(), tokens)))
        global_match_len = 0
        global_genre_index = 0
        for i in range(len(self.queries)):
            match_length = len(set(tokens).intersection(self.queries[i]))
            if match_length > global_match_len:
                global_match_len = match_length
                global_genre_index = i
        genre_resp = self._q_genere.get(global_genre_index)
        return genre_resp

    def process_text(self,text):
        tokens = self.get_raw_tokens(text)
        genre_resp = self.get_genre(tokens)

        if genre_resp == 'activity':
            return random.choice(self.r_pre_fillers) + ' ' + random.choice(self.r_my_activities) + ', ' + \
                   random.choice(self.r_post_fillers)
        elif genre_resp == 'song':
            return 'I will play the song soon.'
        elif genre_resp == 'wiki':
            wiki_resp = search_wiki(tokens,1)
            # print('type wiki : ',type(wiki_resp))
            # print('wiki_resp',wiki_resp)
            return wiki_resp
        elif genre_resp == 'badperson':
            return random.choice(self.r_harsh_response)



