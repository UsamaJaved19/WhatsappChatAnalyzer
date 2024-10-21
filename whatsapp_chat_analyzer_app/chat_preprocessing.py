
import pandas as pd
import re
def chat_preprocessing(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{1,2},\s\d:\d{1,2}\s[APMapm]{2}\s-\s'
    messages = re.split(pattern,data)[1:]
    pattern2 = r'(\d{1,2}/\d{1,2}/\d{1,2},\s\d:\d{1,2}\u202f[APMapm]{2})'
    dates=re.findall(pattern2,data)
    dates_without_unicode = []

    for date in dates:
        dates_without_unicode.append(date.replace('\u202f', ' '))
    df = pd.DataFrame({'dates':dates_without_unicode,'messages':messages})
    df['dates']=pd.to_datetime(df['dates'],format='%m/%d/%y, %I:%M %p')
    msg= []
    user=[]
    for x in df['messages']:
        l = re.split('(\w+\s?\w+):\s', x)
        if l[1:]:
            user.append(l[1])
            msg.append(" ".join(l[2:]))
        else:
            user.append('Notification')
            msg.append(l[0])
    df.drop(columns=['messages'],inplace=True)
    df['user']=user
    df['messages']=msg

    df['year']=df['dates'].dt.year
    df['month_num']=df['dates'].dt.month
    df['month']=df['dates'].dt.month_name()
    df['day']=df['dates'].dt.day
    df['day_name']=df['dates'].dt.day_name()
    df['date']=df['dates'].dt.date
    df['hour']=df['dates'].dt.hour
    df['minutes']=df['dates'].dt.minute

    return df

