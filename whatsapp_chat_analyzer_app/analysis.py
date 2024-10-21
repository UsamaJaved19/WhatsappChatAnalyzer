
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt


def analysis(option, df):
    if option != 'Complete Analysis':
        df = df[df['user'] == option]
    words_list = []

    # extract total no of messages

    num_messages = df.shape[0]

    # extract no of words

    for messages in df['messages']:
        words = messages.split()
        words_list.extend(words)
        num_words = len(words_list)

    # extract no of media messages

    num_media = df[df['messages'] == '<Media omitted>\n']
    no_media = len(num_media)

    # extract deleted messages

    num_delted_msg = df[df['messages'] == 'This message was deleted\n']
    no_deleted_msg = len(num_delted_msg)

    # busiest user graphs

    x = df['user'].value_counts().head()

    return num_messages, num_words, no_media, no_deleted_msg, x

  # #extract links


def links(option, df):
    links = []
    extracter = URLExtract()
    if option != 'Complete Analysis':
        df = df[df['user'] == option]

    for messages in df['messages']:
        links.extend(extracter.find_urls(messages))
    no_links = len(links)
    links_df = pd.DataFrame({'links': links})
    return no_links, links_df


def wordcloud(option,df):
    if option != 'Complete Analysis':
        df = df[df['user'] == option]

    filter_df = df[df['messages'] != '<Media omitted>\n']
    wc = WordCloud(height=500, width=500, min_font_size=10,
                   background_color='white')
    df_wc = wc.generate(' '.join(filter_df['messages']))
    return df_wc
