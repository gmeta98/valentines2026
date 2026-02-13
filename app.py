import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Will You Be My Valentine?", layout="centered", initial_sidebar_state="collapsed")

# Load and encode the music file
try:
    with open("music/Music.mp3", "rb") as f:
        music_data = base64.b64encode(f.read()).decode()
except:
    music_data = ""

html_code = """
<style>
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        background: #ffb3d9 !important;
    }
    
    * { box-sizing: border-box; }
    
    body {
        margin: 0;
        padding: 0;
        min-height: 100vh;
        width: 100vw;
        height: 100vh;
        display: grid;
        place-items: center;
        background: #ffb3d9 !important;
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
        color: #222;
        overflow: hidden;
    }

    .card {
        width: min(800px, 92vw);
        height: min(550px, 75vh);
        background: #f5f5f5;
        border-radius: 18px;
        box-shadow: 0 12px 35px rgba(0,0,0,.18);
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 28px 22px 30px;
        gap: 16px;
        overflow: hidden;
    }

    h1 {
        margin: -5px 0 5px 0;
        text-align: center;
        font-weight: 800;
        letter-spacing: -0.4px;
        font-size: clamp(22px, 3vw, 34px);
        color: #ff2e7a;
    }

    .actions {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 26px;
        margin-top: 10px;
        position: relative;
        height: 90px;
    }

    button {
        border: 0;
        cursor: pointer;
        font-weight: 800;
        border-radius: 999px;
        transition: transform .12s ease, filter .12s ease, background .12s ease;
        user-select: none;
        -webkit-tap-highlight-color: transparent;
    }

    #yesBtn {
        background: #ff2e7a;
        color: white;
        padding: 18px 44px;
        font-size: 20px;
        box-shadow: 0 14px 26px rgba(255,46,122,.28);
        position: relative;
        z-index: 2;
    }

    #yesBtn:hover {
        background: #ff0f66;
        transform: translateY(-1px) scale(1.02);
    }

    #yesBtn:active {
        transform: translateY(1px) scale(.98);
    }

    #noBtn {
        background: #e63b3b;
        color: white;
        padding: 18px 44px;
        font-size: 20px;
        box-shadow: 0 14px 26px rgba(230,59,59,.18);
        position: absolute;
        left: 0;
        top: 0;
        width: auto;
        white-space: nowrap;
        touch-action: none;
        border-radius: 999px;
        z-index: 3;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }

    .note {
        position: absolute;
        bottom: 14px;
        font-size: 15px;
        color: #666;
        opacity: .9;
    }

    .card-heart {
        position: absolute;
        font-size: 2rem;
        pointer-events: none;
        animation: rise 3s ease-out infinite;
    }

    @keyframes rise {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 0;
        }
        5% {
            opacity: 0.8;
        }
        90% {
            opacity: 0.8;
        }
        100% {
            transform: translateY(-200px) rotate(360deg);
            opacity: 0;
        }
    }

    .card-heart:nth-child(1) { animation-delay: 0s; bottom: -50px; left: 5%; }
    .card-heart:nth-child(2) { animation-delay: 1s; bottom: -50px; left: 15%; }
    .card-heart:nth-child(3) { animation-delay: 2s; bottom: -50px; left: 25%; }
    .card-heart:nth-child(4) { animation-delay: 3s; bottom: -50px; left: 35%; }
    .card-heart:nth-child(5) { animation-delay: 4s; bottom: -50px; left: 45%; }
    .card-heart:nth-child(6) { animation-delay: 5s; bottom: -50px; left: 55%; }
    .card-heart:nth-child(7) { animation-delay: 6s; bottom: -50px; left: 65%; }
    .card-heart:nth-child(8) { animation-delay: 7s; bottom: -50px; left: 75%; }
    .card-heart:nth-child(9) { animation-delay: 8s; bottom: -50px; left: 85%; }
    .card-heart:nth-child(10) { animation-delay: 9s; bottom: -50px; left: 95%; }
    .card-heart:nth-child(11) { animation-delay: 10s; bottom: -50px; left: 10%; }
    .card-heart:nth-child(12) { animation-delay: 11s; bottom: -50px; left: 40%; }
    
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

<div class="card" id="card">
    <p style="font-size: 18px; color: #333; margin: 0 0 5px 0; text-align: center;">Hey Juju-Bear, your Grej has a question for you.</p></p>
    <h1 id="title">Will you be my Valentine?</h1>
    <p style="font-size: 14px; color: #222; margin: 0 0 10px 0; text-align: center; font-style: italic;">good luck saying no wink wink 😉</p>

    <div class="actions" id="actions">
        <button id="yesBtn" type="button">Yes 💘</button>
        <button id="noBtn" type="button">No 😭</button>
    </div>

    <div class="note" id="note">"No" seems a bit shy 😈</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
    <div class="card-heart">❤️</div>
</div>

<script>
    const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
    
    const funnyMessages = [
        '"No" seems a bit shy 😈',
        'Gotta catch that "No" 🏃‍♂️',
        '"No" is playing hard to get 😏',
        'So slippery, this "No" button 🐠',
        '"No" be like: catch me if you can 🏃',
        'The "No" button does parkour 🤸',
        '"No" has trust issues 💔',
        'Speed: "No" button 💨',
        '"No" is training for the Olympics 🏅',
        'Mission impossible: Clicking "No" 🎯',
        '"No" be vibing different 🎵',
        'The "No" button said: Not today 😤',
        '"No" is speedrunning away 🎮',
        'Catch me outside! - "No" button 🌍',
        '"No" has abandonment issues 😅'
    ];

    function setupNoButton() {
        const yesBtn = document.getElementById("yesBtn");
        const noBtn = document.getElementById("noBtn");
        const actions = document.getElementById("actions");
        const note = document.getElementById("note");

        if (!yesBtn || !noBtn || !actions) {
            setTimeout(setupNoButton, 100);
            return;
        }

        function updateMessage() {
            const randomMsg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
            note.textContent = randomMsg;
        }

        function placeNoInitial() {
            const a = actions.getBoundingClientRect();
            const yesRect = yesBtn.getBoundingClientRect();
            const b = noBtn.getBoundingClientRect();
            const pad = 10;

            // Position NO directly on top of YES initially
            const x = yesRect.left - a.left;
            const y = yesRect.top - a.top;

            noBtn.style.left = clamp(x, pad, a.width - b.width - pad) + 'px';
            noBtn.style.top = clamp(y, pad, a.height - b.height - pad) + 'px';

            // Make NO match YES size visually
            noBtn.style.width = `${Math.max(b.width, yesRect.width)}px`;
            noBtn.style.height = `${Math.max(b.height, yesRect.height)}px`;
        }

        function moveNoAway(fromX, fromY) {
            const a = actions.getBoundingClientRect();
            const b = noBtn.getBoundingClientRect();
            const pad = 10;

            const minX = pad;
            const maxX = a.width - b.width - pad;
            const minY = pad;
            const maxY = a.height - b.height - pad;

            const cx = fromX - a.left;
            const cy = fromY - a.top;

            let best = { x: Math.random() * (maxX - minX) + minX, y: Math.random() * (maxY - minY) + minY, d: -1 };

            for (let i = 0; i < 18; i++) {
                const x = Math.random() * (maxX - minX) + minX;
                const y = Math.random() * (maxY - minY) + minY;
                const dx = (x + b.width / 2) - cx;
                const dy = (y + b.height / 2) - cy;
                const d = Math.hypot(dx, dy);
                if (d > best.d) best = { x, y, d };
            }

            noBtn.style.left = clamp(best.x, minX, maxX) + 'px';
            noBtn.style.top = clamp(best.y, minY, maxY) + 'px';
            updateMessage();
        }

        const RUN_DISTANCE = 160;

        placeNoInitial();
        window.addEventListener("resize", placeNoInitial);

        actions.addEventListener("mousemove", (e) => {
            const nb = noBtn.getBoundingClientRect();
            const dist = Math.hypot(
                (nb.left + nb.width / 2) - e.clientX,
                (nb.top + nb.height / 2) - e.clientY
            );
            if (dist < RUN_DISTANCE) moveNoAway(e.clientX, e.clientY);
        });

        noBtn.addEventListener("pointerenter", (e) => moveNoAway(e.clientX, e.clientY));
        noBtn.addEventListener("pointerdown", (e) => {
            e.preventDefault();
            moveNoAway(e.clientX, e.clientY);
        });

        yesBtn.addEventListener("click", () => {
            document.getElementById("title").textContent = "YAYYYYY 💖";
            note.textContent = "Best decision ever! 😍";
            noBtn.disabled = true;
            noBtn.style.opacity = "0.25";
        });
    }

    window.addEventListener("load", setupNoButton);
    setupNoButton();
</script>

<audio id="bgMusic" autoplay loop style="display:none;">
    <source src="data:audio/mpeg;base64,""" + music_data + """" type="audio/mpeg">
</audio>

<button id="bgAudioToggle" style="position: fixed; bottom: 30px; right: 30px; z-index: 9999; background: #ff2e7a; border: none; color: white; padding: 12px 16px; border-radius: 50%; cursor: pointer; font-size: 20px; box-shadow: 0 4px 12px rgba(255, 46, 122, 0.3); transition: all 0.3s ease;">🔊</button>

<script>
    const audio = document.getElementById('bgMusic');
    const btn = document.getElementById('bgAudioToggle');
    audio.play().catch(err => {
        audio.muted = true;
        audio.play();
    });
    btn.onclick = function() {
        if (audio.paused) {
            audio.play();
            btn.textContent = '🔊';
        } else {
            audio.pause();
            btn.textContent = '🔇';
        }
    };
</script>
"""
components.html(html_code, height=600)

# Navigation button to gallery
st.markdown("<div style='text-align: center; margin-top: 30px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Go to our Memories  💕", use_container_width=True, key="nav_to_gallery"):
        st.switch_page("pages/1_Gallery.py")

# Hide Streamlit default UI elements and set background
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffb3d9 !important;
    }
    [data-testid="stHeader"] {
        background-color: #ffb3d9 !important;
    }
    .stApp {
        background-color: #ffb3d9 !important;
    }
    body, html {
        background-color: #ffb3d9 !important;
    }
</style>
""", unsafe_allow_html=True)
