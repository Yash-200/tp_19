## Sentiment_Analyser_App
**This is a Streamlit application that uses the OpenAI's Model to create a chat interface similar to Chatbot. The application also uses the NLTK library to perform sentiment analysis on the assistant's responses.**

### Getting Started
To run this application, you will need to have Python and Streamlit installed on your machine. You will also need to sign up for an OpenAI API key and set it as a Streamlit secret.

### Standard Install
### Requirements
**Python 3.7+**
**OpenAI API key**

### Installation

#### System install with a virtual-environment of choice(DO NOT INSTALL IT WITHOUT A VIRTUAL ENVIRONMENT)
**Clone this repository**
**Install the required Python packages with**
```
pip install -r req.txt
```

### Usage
Run the application with streamlit run app.py
Enter a prompt in the chat input box
The assistant will generate a response and display it in the chat message container
The sentiment of the assistant's response will be displayed in a bar chart
Application Overview
The application uses the OpenAI API to generate responses to user prompts. The NLTK library is used to perform sentiment analysis on the assistant's responses. The application also uses Streamlit to create a user-friendly chat interface.


### Docker Install

#### **Clone and cd into the repository**

```
git clone https://github.com/Yash-200/tp_19.git
cd tp_19
```

### ! Do not forget to setup your openAI api key or else you will have to rebuild the container
#### **To build the container run**

```
bash build.sh
```

#### **To start the application run (First time only)**
```
bash tp.sh
```
#### **To run it again**
```
docker start tp_19_docker
```
### **To Stop it run**
```
docker stop tp_19_docker
```

### Key Features
Chat interface similar to ChatGPT
Sentiment analysis of assistant's responses
Customizable OpenAI API model
Built With
Python
Docker
Streamlit
OpenAI API
NLTK
