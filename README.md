# Chatbot-for-Personalized-Learning 

## Project Description

The Chatbot for Personalized Learning is an AI-powered assistant designed to enhance the learning experience. Using advanced machine learning models and APIs, the chatbot:

Generates content based on user queries
Recommends YouTube videos relevant to the topic
This chatbot aims to make learning interactive, engaging, and tailored to the user's needs.

## Features 

* Content Generation: Utilizes Hugging Face's google/flan-t5-large model for generating detailed and accurate responses to user queries
* Video Recommendations: Integrates YouTube API to provide curated video recommendations based on the user's query
* Personalized Learning: Delivers customized educational resources and guidance tailored to individual users' needs
* Seamless LMS Integration: Interacts with external educational repositories to provide topic-specific content
* NLU-Driven Interactions: Uses advanced Natural Language Understanding techniques for intelligent conversations

## Tech Stack

* Language: Python
* Framework: RASA for building Chatbot
* Machine Learning: Hugging Face Transformers (google/flan-t5-large)
* APIs: YouTube Data API v3
* Frontend: Streamlit
* IDE: Visual Studio Code

## Modules Implemented

* Intent Recognition: Advanced NLU for understanding user queries
* Dialogue Management: Context-aware conversation handling
* LMS Integration: Seamless connection with educational repositories
* Content Generation: AI-powered response generation
* Video Recommendation: Smart YouTube content curation

## Setup Instruction

### Prerequisites
- Python 3.8+
- Virtual Environment(recommended)
- API Keys: YouTube Data API key


### Installation Steps

#### 1. Clone the repository

        https://github.com/smriti011/Chatbot-for-Personalized-Learning

#### 2. Create and activate virtual environment

        python -m venv venv

* For Windows
  
        venv\Scripts\activate

* For Unix/MacOS
  
        source venv/bin/activate

#### 3. Install dependencies

        pip install -r requirements.txt

#### 4. Configure API keys: Create a ".env" file in the root directory:

        YOUTUBE_API_KEY=your_key_here

#### 5. Train RASA model:

        rasa train


## Deployment

### Local Deployment with Streamlit

#### 1. Install Streamlit

        pip install streamlit
#### 2. Run the Streamlit app:

                # Start RASA server
                rasa run --enable-api --cors "*" --port 5005

                # In a new terminal, start RASA actions
                rasa run actions

                # In another terminal, run Streamlit
                streamlit run app.py

The application will be available at         

## Deployment options

- Local: Run using Streamlit for development
- Cloud: Deploy to Streamlit Cloud for production
- Docker: Containerization available for scalable deployment

## Usage Guide

#### 1. Starting a Conversation:

* Launch the Streamlit interface
* Type your question in the chat input
* Press Enter or click Send

#### 2. Getting Responses:

* View AI-generated content
* Explore recommended YouTube videos
* Follow up with related questions

#### 3. Examples Interactions

                User: "Explain Artificial Intelligence"
                Bot: *Generates detailed explanation about the topic*
                Bot: "Would you like to see some video resources?"
                User: "Yes"
                Bot: *Provides YouTube links related to the topic*
  




