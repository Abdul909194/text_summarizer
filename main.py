import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

src_text = """
It continues to amaze me; actually it is depressing that although our business leaders constantly confirm that innovation is in their top three priorities yet they stay stubbornly disengaged in facilitating this across their organizations, especially the larger ones.
It is our senior leaders within organizations that have the ability to:
link innovation to strategy, and
create focus, engagement and passion for innovation, and
direct funds and resources to good innovation programs, and
speed good ideas to market as new business models, products and services, and
ensure the processes and relevant metrics exist so innovation is sustainable and integrated.
In mid-sized and large companies, leadership and engagement from CEOs and senior executives are vital to innovation success. What’s more, these leaders want innovation to happen, more consistently, more purposefully and with better result.
Of course I am not suggesting this is all business leaders, but I would argue innovation and its ‘make up’ remains a mystery to most leaders. They are more than willing to allocate responsibility down the organization, failing to recognize their pivotal role in managing or orchestrating innovation engagement themselves, or even ensuring the mechanisms are fully in place. Why is this?
Yet the absence of a well-articulated innovation strategy is by far the most important constraint for companies to reach their innovation targets.
"""

s = summarize(src_text,0.5)
print('TEXT: \n',src_text)
print('Summary: \n',s)
