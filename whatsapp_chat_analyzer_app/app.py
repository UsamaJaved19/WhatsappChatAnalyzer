import streamlit as st
import chat_preprocessing
# import analysis
import analysis
import matplotlib.pyplot as plt
st.sidebar.title('Whatsapp Chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    file = bytes_data.decode("utf-8")
    df = chat_preprocessing.chat_preprocessing(file)
    st.dataframe(df)

    user_list = df['user'].unique().tolist()

    user_list.remove('Notification')
    user_list.insert(0, 'Complete Analysis')
    option = st.selectbox('select user', user_list)

    if st.button('Show Analysis'):
        # num_msg, words, num_media, num_deleted_msg,x = analysis.analysis(
        #     option, df)
        num_msg, words, num_media, num_deleted_msg, x = analysis.analysis(
            option, df)
        no_links, links = analysis.links(option, df)

        wordcloud = analysis.wordcloud(option, df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_msg)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media)
        with col4:
            st.header("Total Deleted Messages")
            st.title(num_deleted_msg)
        col5, col6 = st.columns(2)
        with col5:
            st.header("Total Links in Messages")
            st.title(no_links)
        col7, col8 = st.columns(2)
        with col7:
            st.header("Links in Messages")
            st.dataframe(links)

        col7, col8 = st.columns(2)
        if option == 'Complete Analysis':
            with col7:
                st.title("Most Busy user")
                names = x.index
                messages = x.values
                fig, ax = plt.subplots()
                ax.bar(names, messages)
                ax.set_xlabel = 'user'
                ax.set_ylabel = 'messages'
                ax.set_xticklabels(x.index, rotation='vertical')
                st.pyplot(fig)
        with col8:
            st.title('Most Frequent word used')
            fig, ax = plt.subplots()
            ax.imshow(wordcloud)
            st.pyplot(fig)
