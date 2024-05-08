import streamlit as st
from openai import OpenAI
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd


st.title("Sentiment_Analysis_App")

#Open_AI_API_Key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#Sentiment_Analyzer
sentiment_analyser = SentimentIntensityAnalyzer()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []


chat_used = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def plot_chart(Sentence):
    sentiment = sentiment_analyser.polarity_scores(Sentence)
    df = pd.DataFrame(sentiment,index=["Sentiment"])
    df.rename(columns = {'pos':'Positive_Score','neg' :"Negative_Score", 'neu':"Neutral_Score","compound": "Compound_Score"}, inplace = True)
    st.bar_chart(data=df,y=list(df.columns))
    return sentiment




if prompt := st.chat_input("What is up?"):
    chat_used = True  

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)     
    #User_Messages
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    sentiment =  plot_chart(response)
    #Assistant_Responses
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                
                {"role": "assistant","content":f"<Summarize this({[response]}) content> and <include its polarity_scores ({[sentiment]})>"},

            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


#Generating_Responses
generate_report = st.button("Generate Report", disabled=not chat_used)
if generate_report:
    #Filltering_Messages
    assistant_messages = [message for message in st.session_state.messages if message["role"] == "assistant"]

    #Sentiment_Analysis_on_Each_Message
    message_sentiment = []
    for message in assistant_messages:
        sentiment = sentiment_analyser.polarity_scores(message["content"])
        message_sentiment.append(sentiment)

    #Creating_DataFrame
    df_sentiment = pd.DataFrame(message_sentiment)
    sentiment_scores = df_sentiment

    #bar_chart_plot
    st.bar_chart(sentiment_scores)

    #Combining_Messages_and_Sentences
    message_and_sentiment = []
    for i, message in enumerate(assistant_messages):
        sentiment = sentiment_analyser.polarity_scores(message["content"])
        message_and_sentiment.append({"message": message["content"], "sentiment": sentiment})


    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                
                {"role": "assistant","content":f"<Summarize this({[message_and_sentiment]}) content> and <include its polarity_scores in the summarization> <don't metion the specific scores in the response"},

            ],
            stream=True,
        )
        response = st.write_stream(stream)

