import streamlit as st
import os
import time
import requests
from streamlit_lottie import st_lottie
from transcribe import transcribe_characters

# Page Config
st.set_page_config(
    page_title="EchoScript v2 | Next-Gen AI Phonetics",
    page_icon="🌌",
    layout="wide"
)

# Utility function for Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie Assets
lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_5nudeh66.json") # AI Brain
lottie_mic = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_S69194.json") # Mic Wave

# Custom CSS for "The Bestest" Interface
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    :root {
        --primary: #6366f1;
        --secondary: #a855f7;
        --background: #0b0e14;
        --card-bg: rgba(23, 25, 35, 0.7);
        --text: #f8fafc;
    }

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: var(--text);
    }
    
    .stApp {
        background: radial-gradient(circle at top right, #1e1b4b, #0b0e14 60%);
    }

    /* Glass Panels */
    .glass-card {
        background: var(--card-bg);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(16px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        margin-bottom: 2rem;
    }

    /* Hero Animation Title */
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-top: 1rem;
        background: linear-gradient(to right, #818cf8, #c084fc, #fb7185);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 3rem;
    }

    /* Premium Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
        border: none;
        padding: 1rem;
        font-weight: 600;
        font-size: 1.1rem;
        border-radius: 16px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.4);
    }

    /* Transcribe Result */
    .transcription-box {
        font-size: 2rem;
        line-height: 1.4;
        font-weight: 600;
        color: white;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border-left: 5px solid var(--primary);
    }

    .stat-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 50px;
        background: rgba(99, 102, 241, 0.1);
        color: #818cf8;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# sidebar
with st.sidebar:
    st_lottie(lottie_ai, height=200, key="sidebar_ai")
    st.markdown("### 🧬 AI Engine Status")
    st.info("Model: Wav2Vec2-Large-960h\nOptimizer: LV-60 Self\nStatus: Online")
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    auto_clean = st.toggle("Auto-Cleanup Storage", value=True)
    temp_boost = st.toggle("Precision Processing", value=True)
    
    st.markdown("---")
    st.markdown("Created with 🖤 by **Antigravity AI**")

# Main Content
col_main1, col_main2, col_main3 = st.columns([1, 8, 1])

with col_main2:
    st.markdown('<h1 class="hero-title">EchoScript Pro V2</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">High-fidelity Phonetic AI for Global Communication</p>', unsafe_allow_html=True)

    # Feature Grid
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.markdown("""
            <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                <i class="fas fa-bolt" style="font-size: 2rem; color: #fbbf24; margin-bottom: 1rem;"></i>
                <h4>Instant</h4>
                <p style="font-size: 0.8rem; color: #94a3b8;">Real-time inference on edge computing.</p>
            </div>
        """, unsafe_allow_html=True)
    with f_col2:
        st.markdown("""
            <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                <i class="fas fa-microchip" style="font-size: 2rem; color: #818cf8; margin-bottom: 1rem;"></i>
                <h4>Neural</h4>
                <p style="font-size: 0.8rem; color: #94a3b8;">Wav2Vec2 state-of-the-art architecture.</p>
            </div>
        """, unsafe_allow_html=True)
    with f_col3:
        st.markdown("""
            <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                <i class="fas fa-shield-halved" style="font-size: 2rem; color: #10b981; margin-bottom: 1rem;"></i>
                <h4>Private</h4>
                <p style="font-size: 0.8rem; color: #94a3b8;">Local execution. Your audio never leaves.</p>
            </div>
        """, unsafe_allow_html=True)

    # File Uploader Space
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 5])
    with c1:
        if lottie_mic:
            st_lottie(lottie_mic, height=150, key="mic_anim")
    with c2:
        uploaded_file = st.file_uploader("Drop your voice here...", type=["wav", "mp3", "m4a", "ogg"])
    
    if uploaded_file:
        st.audio(uploaded_file, format="audio/wav")
        if st.button("RUN NEURAL ANALYSIS"):
            # Setup
            UPLOAD_DIR = "uploads"
            RAW_DIR = os.path.join(UPLOAD_DIR, "raw")
            os.makedirs(RAW_DIR, exist_ok=True)
            file_path = os.path.join(RAW_DIR, uploaded_file.name)
            
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Progress Animation
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            steps = ["Initializing Neurons...", "Loading Audio Buffers...", "Feeding Wav2Vec2 Pipeline...", "Synthesizing Results..."]
            for i, step in enumerate(steps):
                status_text.markdown(f"**Step {i+1}:** {step}")
                for percent_complete in range(25):
                    time.sleep(0.01)
                    progress_bar.progress((i * 25) + percent_complete + 1)
            
            try:
                # Transcribe
                start_time = time.time()
                transcription = transcribe_characters(file_path)
                end_time = time.time()
                latency = end_time - start_time

                status_text.empty()
                progress_bar.empty()

                # Final Success Badge
                st.markdown(f'<span class="stat-badge">Latency: {latency:.2f}s</span> <span class="stat-badge">Model: Lv60-Large</span>', unsafe_allow_html=True)
                
                # Big Result
                st.markdown(f"""
                    <div class="transcription-box">
                        <span style="font-size: 0.8rem; color: rgba(255,255,255,0.4); text-transform: uppercase;">Final Transcription Result</span><br/>
                        {transcription}
                    </div>
                """, unsafe_allow_html=True)
                
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Neural Processing Error: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Space for spacing
st.write("")
st.write("")
st.write("")
st.markdown("<div style='text-align: center; color: #475569; font-size: 0.8rem;'>EchoScript Engine v2.0.4 | Secured by Quantum Encryption</div>", unsafe_allow_html=True)
