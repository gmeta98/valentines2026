import streamlit as st
from pathlib import Path
import os
import base64

st.set_page_config(page_title="Our Love Story", layout="wide", initial_sidebar_state="collapsed")

# Load and encode the music file
try:
    with open("music/Music.mp3", "rb") as f:
        music_data = base64.b64encode(f.read()).decode()
except:
    music_data = ""

# Background styling
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fff5f7 0%, #ffe7f0 100%) !important;
    }
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #ffe7f0 100%) !important;
    }
    body, html {
        background: linear-gradient(135deg, #fff5f7 0%, #ffe7f0 100%) !important;
    }
    
    .love-message {
        font-family: 'Georgia', serif;
        text-align: center;
        color: #ff0000;
        margin: 10px 0;
        line-height: 1.8;
    }
    
    .title {
        text-align: center;
        color: #ff0000;
        font-size: 3em;
        margin-bottom: 30px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .photo-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    .photo-card {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(255, 46, 122, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .photo-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 28px rgba(255, 46, 122, 0.3);
    }
    
    .photo-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    
    .back-button {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
    }
    
    .star-rating {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 10px 0;
        font-size: 40px;
    }
    
    .star {
        cursor: pointer;
        transition: all 0.2s;
        filter: grayscale(100%);
        opacity: 0.5;
    }
    
    .star:hover {
        transform: scale(1.2);
        filter: grayscale(0%);
        opacity: 1;
    }
    
    .star.active {
        filter: grayscale(0%);
        opacity: 1;
        animation: heartPulse 0.6s ease-out;
    }
    
    @keyframes heartPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1.2); }
    }
    
    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    
    .title {
        text-align: center;
        color: #ff0000;
        font-size: 3em;
        margin-bottom: 30px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: fadeIn 1s ease-in;
    }
    
    .love-message {
        font-family: 'Georgia', serif;
        text-align: center;
        color: #ff0000;
        margin: 10px 0;
        line-height: 1.8;
        animation: fadeIn 1.2s ease-in;
    }
    
    .star-rating {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 10px 0;
        font-size: 40px;
        animation: fadeIn 1.4s ease-in;
    }
    
    .rating-message {
        text-align: center;
        font-size: 18px;
        color: #ff2e7a;
        font-weight: bold;
        margin-top: 15px;
        min-height: 30px;
        animation: fadeIn 1.4s ease-in;
    }
    
    .audio-control {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 999;
        background: #ff2e7a;
        border: none;
        color: white;
        padding: 12px 16px;
        border-radius: 50%;
        cursor: pointer;
        font-size: 20px;
        box-shadow: 0 4px 12px rgba(255, 46, 122, 0.3);
        transition: all 0.3s ease;
    }
    
    .audio-control:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 16px rgba(255, 46, 122, 0.4);
    }
</style>

<div class="star-rating" id="starRating">
    <span class="star" data-value="1">❤️</span>
    <span class="star" data-value="2">❤️</span>
    <span class="star" data-value="3">❤️</span>
    <span class="star" data-value="4">❤️</span>
    <span class="star" data-value="5">❤️</span>
</div>
<div class="rating-message" id="ratingMessage"></div>

<script>
    const messages = {
        1: "Okay... 😅",
        2: "You're warming up! 🔥",
        3: "That's fair 💕",
        4: "Getting there! 😏",
        5: "YESSS BABY!!! 🎉💖"
    };
    
    const stars = document.querySelectorAll('.star');
    const ratingMessage = document.getElementById('ratingMessage');
    
    stars.forEach(star => {
        star.addEventListener('click', function() {
            const value = this.dataset.value;
            
            // Clear previous active stars
            stars.forEach(s => s.classList.remove('active'));
            
            // Activate clicked star and all before it
            for (let i = 0; i < value; i++) {
                stars[i].classList.add('active');
            }
            
            ratingMessage.textContent = messages[value];
        });
        
        star.addEventListener('mouseenter', function() {
            const value = this.dataset.value;
            stars.forEach((s, idx) => {
                s.style.opacity = idx < value ? '1' : '0.5';
            });
        });
    });
    
    document.getElementById('starRating').addEventListener('mouseleave', function() {
        stars.forEach(s => {
            s.style.opacity = s.classList.contains('active') ? '1' : '0.5';
        });
    });
</script>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title"></div>', unsafe_allow_html=True)

# Love Message
st.markdown("""
<div class="love-message">
    <h2 style="font-size: 2em; margin-bottom: 20px; color: #333333;">For My Juju-Bear ❤️</h2></p>
    <p style="font-size: 1.3em; max-width: 800px; margin: 0 auto;">
    Roses are red, violets are blue,<br>
    I'm so-so at planning, but good at loving you.<br>
    Your smile makes me happy, your laugh makes my day,<br>
    So thank you for saying yes, in every possible way.
    </p>
</div>
""", unsafe_allow_html=True)
# Star Rating Section

# Add audio player with base64 encoded music
if music_data:
    audio_html = f'''
    <audio id="bgMusic" autoplay loop style="display:none;">
        <source src="data:audio/mpeg;base64,{music_data}" type="audio/mpeg">
    </audio>
    <button id="bgAudioToggle" style="position: fixed; bottom: 30px; right: 30px; z-index: 999; background: #ff2e7a; border: none; color: white; padding: 12px 16px; border-radius: 50%; cursor: pointer; font-size: 20px; box-shadow: 0 4px 12px rgba(255, 46, 122, 0.3); transition: all 0.3s ease;">🔊</button>
    <script>
        const audio = document.getElementById('bgMusic');
        const btn = document.getElementById('bgAudioToggle');
        audio.play().catch(err => {{
            audio.muted = true;
            audio.play();
        }});
        btn.onclick = function() {{
            if (audio.paused) {{
                audio.play();
                btn.textContent = '🔊';
            }} else {{
                audio.pause();
                btn.textContent = '🔇';
            }}
        }};
    </script>
    '''
    st.markdown(audio_html, unsafe_allow_html=True)

# Load photos from photos_main folder
photos_dir = Path("photos_main")
photos = sorted([f for f in photos_dir.glob("*") if f.suffix.lower() in [".jpg", ".jpeg", ".png"]])

if photos:
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: #ff0000;'>Memories We Share</h2>", unsafe_allow_html=True)
    
    # Create photo grid
    cols = st.columns(2)
    for idx, photo in enumerate(photos):
        with cols[idx % 2]:
            st.image(str(photo), use_column_width=True)
else:
    st.warning("No photos found in photos_main folder")

# Back button
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("💕 Back to You", use_container_width=True, key="back_button"):
        st.switch_page("app.py")
