import wikipedia
import nltk
from PyDictionary import PyDictionary
from nltk.corpus import stopwords


def search_wiki(tokens, summary_length):
    tokens = nltk.pos_tag(tokens)
    stop_words = set(stopwords.words('english'))
    question_tags = ['WDT','WP','WRB']
    clean_tokens = [token for token in tokens if token[0].lower() not in stop_words and token[1] not in question_tags]
    # clean_tokens=[]
    # print(tokens)
    # for token in tokens:
    #     print(token)
    #     if (token[0] not in stop_words) and token[1] not in question_tags:
    #         print('adding it')
    #         clean_tokens.append(token)
    required_l = ['NN', 'NNP', 'JJ', 'JJR', 'JJS']
    results = []
    for query, _type in tokens:
        if _type in required_l:
            try:
                results.append((query, wikipedia.summary(query, summary_length)))
            except:
                pass

    # print('clean_tokens',(clean_tokens))
    if len(results) == 0:
        if(len(clean_tokens)==0):
            results.append(('null', "Sorry about that. I can't get that at this moment."))
            return results
        query = clean_tokens[0][0]
        dict_meaning = search_local_dictionary(query)
        if dict_meaning == 'null':
            query = 'null'
            results.append((query, "Sorry about that. I can't get that at this moment."))
            return results
        else:
            results.append((query, dict_meaning))
            return results
    else:
        # print('results',results)
        return results
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
