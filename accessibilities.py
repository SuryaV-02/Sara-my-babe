import wikipedia
import nltk
from PyDictionary import PyDictionary
from nltk.corpus import stopwords

from Utils import *


def search_wiki(tokens, summary_length):
    tokens = nltk.pos_tag(tokens)
    stop_words = set(stopwords.words('english'))
    question_tags = ['WDT','WP','WRB']
    required_l = ['NN', 'NNP', 'JJ', 'JJR', 'JJS']
    clean_tokens = [token for token in tokens if token[0].lower() not in stop_words and token[1] not in question_tags]
    # print('clean_tokens',clean_tokens)
    neat_clean_tokens = [token[0] for token in tokens if token[0].lower() not in stop_words and token[1] not in question_tags and token[1] in required_l]
    neat_combos = get_combinations(neat_clean_tokens)
    # print('Neat Combos: ',neat_combos)
    results = []
    # for query, _type in tokens:
    #     if _type in required_l:
    #         try:
    #             results.append((query, wikipedia.summary(query, summary_length)))
    #         except:
    #             print('Not Query : ',query)

    for query in neat_combos:
        print("Trying", query)
        try:
            results.append((query, wikipedia.summary(query, summary_length)))
            break
        except:
            print("Not Query ",query)
    # results = get_combinations(results)
    # print('clean_tokens',(clean_tokens))
    # print('results',results[0])
    if len(results) == 0:
        if(len(clean_tokens)==0):
            results.append("Sorry about that. I can't get that at this moment.")
            return results
        query = clean_tokens[0][0]
        dict_meaning = search_local_dictionary(query)
        if dict_meaning == 'null':
            query = 'null'
            results.append("Sorry about that. I can't get that at this moment.")
            return results
        else:
            results.append(dict_meaning)
            return "".join(results)
    else:
        # print('results',results)
        return "".join(results[0])
    # return results


def search_local_dictionary(query):
    print('Dict : ',query)
    try:
        local_dictionary = PyDictionary()
        first_pair = next(iter((local_dictionary.meaning(query).items())))
        result = " "
        if(len(first_pair[1])>1):
            return "".join(first_pair[1][1])
        else:
            return "".join(first_pair[1])
    except:
        return "NULL"
