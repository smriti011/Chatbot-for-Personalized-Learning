
import streamlit as st
import requests
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title="Chatbot For Personalized Learning",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS wrapped in proper string format
css = '''
<style>
/* Global styles */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

.stApp {
    background-color: #ffffff; /* Background color */
}

.main .block-container {
    background-color: #ffffff;
    max-width: 1200px;
    margin: 0 auto;
    margin-left: 300px;
    padding: 2.5rem;
}

 # Custom design of the new chat button
 
# /* New Chat button styles */
# .new-chat-button {
#     background: linear-gradient(90deg, #1e90ff, #00bfff); /* Blue gradient */
#     border: none;
#     border-radius: 5px;
#     color: white;
#     padding: 10px 20px;
#     font-size: 16px;
#     font-weight: bold;
#     text-transform: uppercase;
#     cursor: pointer;
#     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     transition: transform 0.2s, box-shadow 0.2s;
# }
# .new-chat-button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
# }



/* App header */
.app-header {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 1.5rem;
    background: #112D4E;
    border-radius: 12px;
    margin-bottom: 2rem;
    border: 1px solid #e9ecef;
}

.app-logo {
    font-size: 28px;
}

.app-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #ffffff; /* Text color */
}

/* Chat history sidebar */
[data-testid="stSidebar"] {
    background-color: #112E4D; /* Sidebar background color */
    color: #ffffff; /* Sidebar text color */
}

.chat-history-sidebar {
    background-color: #1E3E62; /* Sidebar background color */
    padding: 1.5rem;
    color: #ffffff; /* Sidebar text color */
}

.sidebar-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #3c6aff50;
    color: #ffffff; /* Sidebar header text color */
}

.chat-history-item {
    padding: 0.875rem 1rem;
    margin: 0.5rem 0;
    border-radius: 8px;
    background-color: #ffffff;
    color: #4b5563;
    transition: all 0.2s ease;
    cursor: pointer;
    border: 1px solid #e9ecef;
}

.chat-history-item:hover {
    background-color: #f1f5f9;
    transform: translateX(2px);
}

.chat-history-item.active {
    background-color: #e5edff;
    color: #1e40af;
    border-color: #93c5fd;
}

/* Message containers and bubbles */
.message-container {
    display: flex;
    margin: 1.5rem 0;
    gap: 1rem;
    align-items: flex-start;
}

.user-bubble, .bot-bubble {
    padding: 1rem 1.5rem 1rem 3rem;
    border-radius: 12px;
    max-width: 80%;
    line-height: 1.6;
    font-size: 0.95rem;
    position: relative;
    background-color: #3c6aff50; /* Bubble background color */
    color: #000000; /* Bubble text color */
}

.user-bubble {
    margin-left: auto;
    border-bottom-right-radius: 4px;
}

.bot-bubble {
    border-bottom-left-radius: 4px;
    border: 1px solid #e9ecef;
}

/* Input field styling */
.stTextInput > div > div > input {
    border-radius: 12px;
    padding: 0.875rem 1rem 0.875rem 3rem;
    font-size: 0.95rem;
    border: 1px solid #000000; /* Input border color */
    background-color: #1E3E62;
    color: #ffffff; /* Input text color */
}

/* Sidebar info boxes */
.sidebar-info {
    padding: 1rem;
    background: #ffffff;
    border-radius: 8px;
    margin: 1rem 0;
    border: 1px solid #e9ecef;
    color: #1E3E62; /* Sidebar info text color */
}

.sidebar-info h3 {
    font-size: 0.9rem;
    color: #1E3E62; /* Sidebar info header text color */
    margin-bottom: 0.5rem;
}

.sidebar-info p {
    font-size: 0.8rem;
    color: #4b5563;
    margin: 0;
}

/* Hide default Streamlit elements */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* Grey text for "Thinking" */
.grey-text {
    color: grey;
}

</style>
'''

# Apply the CSS
st.markdown(css, unsafe_allow_html=True)

# Initialize session states
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'chat_sessions' not in st.session_state:
    st.session_state.chat_sessions = [{'id': 0, 'title': 'New Chat', 'messages': []}]
if 'current_chat_id' not in st.session_state:
    st.session_state.current_chat_id = 0
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'last_message' not in st.session_state:
    st.session_state.last_message = ""
if 'last_message_time' not in st.session_state:
    st.session_state.last_message_time = 0

# Add sidebar content
sidebar_container = st.sidebar.container()
with sidebar_container:
    st.markdown("""
    <div class="sidebar-info" role="complementary" aria-label="Interactive Learning Section">
        <h3>🎯 Interactive Learning</h3>
        <p>Get personalized explanations for challenging topics and concepts</p>
    </div>

    <div class="sidebar-info" aria-label="Resource Recommendations Section">
        <h3>📚 Resource Recommendations</h3>
        <p>Discover curated YouTube videos for better understanding </p>
    </div>
    """, unsafe_allow_html=True)

#  # Add sidebar content
# sidebar_container = st.sidebar.container()
# with sidebar_container:
#     st.markdown("""
#     <button class="new-chat-button" onclick="handleNewChat()">New Chat</button>
#     """, unsafe_allow_html=True)   

st.markdown("""
<style>
    .animated-logo {
        display: inline-block;
        animation: updown 1s infinite;
    }

    @keyframes updown {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
</style>

<div class="app-header">
    <span class="app-logo animated-logo">🤖</span>
    <h1 class="app-title">Chatbot For Personalized Learning</h1>
</div>
""", unsafe_allow_html=True)

# JavaScript for handling chat interactions
# st.markdown("""
# <script>
# function handleNewChat() { window.parent.postMessage({type:'newChat'}, '*'); }
# function handleChatSelect(id) { window.parent.postMessage({type:'selectChat', chatId:id}, '*'); }
# </script>
# """, unsafe_allow_html=True)

def create_new_chat():
   new_id = len(st.session_state.chat_sessions)
   st.session_state.chat_sessions.append({
       'id': new_id,
       'title': f'New Chat {new_id + 1}',
       'messages': []
   })
   st.session_state.current_chat_id = new_id

def get_current_chat():
   return next((chat for chat in st.session_state.chat_sessions if chat['id'] == st.session_state.current_chat_id), st.session_state.chat_sessions[0])

# Chat container
chat_container = st.container()

def clear_input():
   st.session_state.last_message = st.session_state.user_input
   st.session_state.user_input = ""

# Display current chat messages with timestamps
chat_container = st.container()
current_chat = get_current_chat()
with chat_container:
    for message in current_chat['messages']:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="message-container">
                <div class="user-bubble">
                    <span class="message-icon">👤</span>
                    {message["content"]}
                    <span class="timestamp">{message["timestamp"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="message-container">
                <div class="bot-bubble">
                    <span class="message-icon">🤖</span>
                    {message["content"]}
                    <span class="timestamp">{message["timestamp"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Add this right before your text input line:
st.markdown('<div class="input-container"><span class="input-emoji">👤</span></div>', unsafe_allow_html=True)

# Input area (without header)
user_input = st.text_input("", placeholder="Type your message here...", key="user_input", on_change=clear_input)


# Message processing
if st.session_state.last_message and not st.session_state.processing:
    current_time = time.time()
    
    if current_time - st.session_state.last_message_time < 1:
        st.warning("⚡ Please wait a moment before sending another message")
        st.stop()
    
    st.session_state.processing = True
    st.session_state.last_message_time = current_time
    timestamp = datetime.now().strftime("%H:%M")
    
    # Add user message to current chat
    current_chat['messages'].append({
        "role": "user",
        "content": st.session_state.last_message,
        "timestamp": timestamp
    })

    # Update chat title if it's the first message
    if len(current_chat['messages']) == 1:
        current_chat['title'] = st.session_state.last_message[:30] + "..."

    try:
        with st.spinner('Thinking'):
            rasa_url = "http://localhost:5005/webhooks/rest/webhook"
            payload = {"sender": "user", "message": st.session_state.last_message}
            response = requests.post(rasa_url, json=payload)
            
            if response.status_code == 200:
                bot_responses = response.json()
                if bot_responses:
                    # Combine all bot responses into a single message
                    combined_response = "\n\n".join([res.get("text", "") for res in bot_responses])
                    current_chat['messages'].append({
                        "role": "bot",
                        "content": combined_response,
                        "timestamp": datetime.now().strftime("%H:%M")
                    })
                else:
                    st.error("📝 No response received. Let's try rephrasing the question.")
            else:
                st.error(f"❌ Connection error: {response.status_code}")
                
    except requests.exceptions.RequestException as e:
        st.error(f"🔌 Connection issue: {str(e)}")
        
    finally:
        st.session_state.processing = False
        st.session_state.last_message = ""
        st.rerun()

# Handle new chat button in sidebar               #remove this for deleting default new chat button
if st.sidebar.button("+ New Chat"):
    create_new_chat()
    st.rerun()
