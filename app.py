import streamlit as st
import streamlit.components.v1 as components
import os
from pathlib import Path

# Load environment variables from .env file if it exists
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    with open(env_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

# Get configuration from environment variables with defaults
PAGE_TITLE = os.getenv('PAGE_TITLE', 'Will You Be My Valentine?')
PRIMARY_COLOR = os.getenv('PRIMARY_COLOR', '#ff2e7a')
SECONDARY_COLOR = os.getenv('SECONDARY_COLOR', '#e63b3b')
GRADIENT_START = os.getenv('BACKGROUND_GRADIENT_START', '#ff006e')
GRADIENT_END = os.getenv('BACKGROUND_GRADIENT_END', '#fb5607')
QUESTION_TEXT = os.getenv('QUESTION_TEXT', 'Will you be my Valentine?')
YES_TEXT = os.getenv('YES_TEXT', 'Yes')
NO_TEXT = os.getenv('NO_TEXT', 'No')
SUCCESS_MESSAGE = os.getenv('SUCCESS_MESSAGE', 'YAYYYYY 💖')
SUCCESS_NOTE = os.getenv('SUCCESS_NOTE', 'Best decision ever! 😍')
FOOTER_NOTE = os.getenv('FOOTER_NOTE', '"No" seems a bit shy 😈')

st.set_page_config(page_title=PAGE_TITLE, layout="centered", initial_sidebar_state="collapsed")

html_code = f"""
<style>
    * {{ box-sizing: border-box; }}
    
    body {{
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, {GRADIENT_START} 0%, {GRADIENT_END} 100%);
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
        color: #222;
        overflow: hidden;
    }}

    .card {{
        width: min(720px, 92vw);
        height: min(480px, 68vh);
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
    }}

    h1 {{
        margin: 0;
        text-align: center;
        font-weight: 800;
        letter-spacing: -0.4px;
        font-size: clamp(22px, 3vw, 34px);
        color: #222;
    }}

    .actions {{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 26px;
        margin-top: 10px;
        position: relative;
        height: 90px;
    }}

    button {{
        border: 0;
        cursor: pointer;
        font-weight: 800;
        border-radius: 999px;
        transition: transform .12s ease, filter .12s ease, background .12s ease;
        user-select: none;
        -webkit-tap-highlight-color: transparent;
    }}

    #yesBtn {{
        background: {PRIMARY_COLOR};
        color: white;
        padding: 18px 44px;
        font-size: 20px;
        box-shadow: 0 14px 26px rgba(255,46,122,.28);
        position: relative;
        z-index: 2;
    }}

    #yesBtn:hover {{
        background: #ff0f66;
        transform: translateY(-1px) scale(1.02);
    }}

    #yesBtn:active {{
        transform: translateY(1px) scale(.98);
    }}

    #noBtn {{
        background: {SECONDARY_COLOR};
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
    }}

    .note {{
        position: absolute;
        bottom: 14px;
        font-size: 12px;
        color: #666;
        opacity: .9;
    }}
</style>

<div class="card" id="card">
    <h1 id="title">{QUESTION_TEXT}</h1>

    <div class="actions" id="actions">
        <button id="yesBtn" type="button">{YES_TEXT}</button>
        <button id="noBtn" type="button">{NO_TEXT}</button>
    </div>

    <div class="note" id="note">{FOOTER_NOTE}</div>
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

    function setupNoButton() {{
        const yesBtn = document.getElementById("yesBtn");
        const noBtn = document.getElementById("noBtn");
        const actions = document.getElementById("actions");
        const note = document.getElementById("note");

        if (!yesBtn || !noBtn || !actions) {{
            setTimeout(setupNoButton, 100);
            return;
        }}

        function updateMessage() {{
            const randomMsg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
            note.textContent = randomMsg;
        }}

        function placeNoInitial() {{
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
            noBtn.style.width = `${{Math.max(b.width, yesRect.width)}}px`;
            noBtn.style.height = `${{Math.max(b.height, yesRect.height)}}px`;
        }}

        function moveNoAway(fromX, fromY) {{
            const a = actions.getBoundingClientRect();
            const b = noBtn.getBoundingClientRect();
            const pad = 10;

            const minX = pad;
            const maxX = a.width - b.width - pad;
            const minY = pad;
            const maxY = a.height - b.height - pad;

            const cx = fromX - a.left;
            const cy = fromY - a.top;

            let best = {{ x: Math.random() * (maxX - minX) + minX, y: Math.random() * (maxY - minY) + minY, d: -1 }};

            for (let i = 0; i < 18; i++) {{
                const x = Math.random() * (maxX - minX) + minX;
                const y = Math.random() * (maxY - minY) + minY;
                const dx = (x + b.width / 2) - cx;
                const dy = (y + b.height / 2) - cy;
                const d = Math.hypot(dx, dy);
                if (d > best.d) best = {{ x, y, d }};
            }}

            noBtn.style.left = clamp(best.x, minX, maxX) + 'px';
            noBtn.style.top = clamp(best.y, minY, maxY) + 'px';
            updateMessage();
        }}

        const RUN_DISTANCE = 160;

        placeNoInitial();
        window.addEventListener("resize", placeNoInitial);

        actions.addEventListener("mousemove", (e) => {{
            const nb = noBtn.getBoundingClientRect();
            const dist = Math.hypot(
                (nb.left + nb.width / 2) - e.clientX,
                (nb.top + nb.height / 2) - e.clientY
            );
            if (dist < RUN_DISTANCE) moveNoAway(e.clientX, e.clientY);
        }});

        noBtn.addEventListener("pointerenter", (e) => moveNoAway(e.clientX, e.clientY));
        noBtn.addEventListener("pointerdown", (e) => {{
            e.preventDefault();
            moveNoAway(e.clientX, e.clientY);
        }});

        yesBtn.addEventListener("click", () => {{
            document.getElementById("title").textContent = "{SUCCESS_MESSAGE}";
            note.textContent = "{SUCCESS_NOTE}";
            noBtn.disabled = true;
            noBtn.style.opacity = "0.25";
        }});
    }}

    window.addEventListener("load", setupNoButton);
    setupNoButton();
</script>
"""

components.html(html_code, height=600)
