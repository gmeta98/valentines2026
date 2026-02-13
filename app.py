"""
Valentine's Day Interactive Card Application

A fun and interactive Valentine's Day card built with Streamlit.
Features a playful interface where the "No" button runs away from the cursor!
"""

import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page
st.set_page_config(
    page_title="Will You Be My Valentine?", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# HTML, CSS, and JavaScript code for the interactive Valentine card
html_code = """
<style>
    * { box-sizing: border-box; }
    
    body {
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, #ff006e 0%, #fb5607 100%);
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
        color: #222;
        overflow: hidden;
    }

    .card {
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
    }

    h1 {
        margin: 0;
        text-align: center;
        font-weight: 800;
        letter-spacing: -0.4px;
        font-size: clamp(22px, 3vw, 34px);
        color: #222;
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
        font-size: 12px;
        color: #666;
        opacity: .9;
    }
</style>

<div class="card" id="card">
    <h1 id="title">Will you be my Valentine?</h1>

    <div class="actions" id="actions">
        <button id="yesBtn" type="button">Yes</button>
        <button id="noBtn" type="button">No</button>
    </div>

    <div class="note" id="note">"No" seems a bit shy 😈</div>
</div>

<script>
    // Helper function to clamp a value between min and max
    const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
    
    // Array of funny messages that appear when trying to click "No"
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

    // Main setup function for the "No" button behavior
    function setupNoButton() {
        const yesBtn = document.getElementById("yesBtn");
        const noBtn = document.getElementById("noBtn");
        const actions = document.getElementById("actions");
        const note = document.getElementById("note");

        // Wait for DOM elements to be ready
        if (!yesBtn || !noBtn || !actions) {
            setTimeout(setupNoButton, 100);
            return;
        }

        // Update the message with a random funny quote
        function updateMessage() {
            const randomMsg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
            note.textContent = randomMsg;
        }

        // Position the "No" button on top of "Yes" button initially
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

        // Move the "No" button away from cursor position
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

            // Try multiple random positions and pick the one farthest from cursor
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

        // Distance threshold for when "No" button should run away
        const RUN_DISTANCE = 160;

        // Initialize button positions
        placeNoInitial();
        window.addEventListener("resize", placeNoInitial);

        // Track mouse movement and move "No" button if cursor gets too close
        actions.addEventListener("mousemove", (e) => {
            const nb = noBtn.getBoundingClientRect();
            const dist = Math.hypot(
                (nb.left + nb.width / 2) - e.clientX,
                (nb.top + nb.height / 2) - e.clientY
            );
            if (dist < RUN_DISTANCE) moveNoAway(e.clientX, e.clientY);
        });

        // Additional event listeners for touch/pointer devices
        noBtn.addEventListener("pointerenter", (e) => moveNoAway(e.clientX, e.clientY));
        noBtn.addEventListener("pointerdown", (e) => {
            e.preventDefault();
            moveNoAway(e.clientX, e.clientY);
        });

        // Handle "Yes" button click - show success message
        yesBtn.addEventListener("click", () => {
            document.getElementById("title").textContent = "YAYYYYY 💖";
            note.textContent = "Best decision ever! 😍";
            noBtn.disabled = true;
            noBtn.style.opacity = "0.25";
        });
    }

    // Initialize when page loads
    window.addEventListener("load", setupNoButton);
    setupNoButton();
</script>
"""

# Render the HTML component with the Valentine's card
components.html(html_code, height=600)
