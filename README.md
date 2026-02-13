# Valentine's Day 2026 🌹💖

A fun, interactive Streamlit web app asking "Will you be my Valentine?" with a playful twist - the "No" button runs away when you try to click it!

## Features

- 💕 Beautiful gradient background
- 🎯 Interactive buttons with playful behavior
- 🎨 Customizable colors, messages, and text
- 📱 Responsive design
- ⚙️ Environment-based configuration

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** to the URL shown (usually `http://localhost:8501`)

## Customization with Environment Variables

You can customize the app's appearance and messages using environment variables:

1. **Copy the example env file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`** with your preferences:
   ```env
   PAGE_TITLE=Will You Be My Valentine?
   QUESTION_TEXT=Will you be my Valentine?
   PRIMARY_COLOR=#ff2e7a
   SECONDARY_COLOR=#e63b3b
   BACKGROUND_GRADIENT_START=#ff006e
   BACKGROUND_GRADIENT_END=#fb5607
   SUCCESS_MESSAGE=YAYYYYY 💖
   ```

3. **Restart the app** to see your changes

### Available Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `PAGE_TITLE` | Browser tab title | "Will You Be My Valentine?" |
| `QUESTION_TEXT` | Main question displayed | "Will you be my Valentine?" |
| `YES_TEXT` | Text on the Yes button | "Yes" |
| `NO_TEXT` | Text on the No button | "No" |
| `PRIMARY_COLOR` | Color of the Yes button | #ff2e7a |
| `SECONDARY_COLOR` | Color of the No button | #e63b3b |
| `BACKGROUND_GRADIENT_START` | Start color of background | #ff006e |
| `BACKGROUND_GRADIENT_END` | End color of background | #fb5607 |
| `SUCCESS_MESSAGE` | Message when Yes is clicked | "YAYYYYY 💖" |
| `SUCCESS_NOTE` | Note shown after Yes click | "Best decision ever! 😍" |
| `FOOTER_NOTE` | Initial footer message | '"No" seems a bit shy 😈' |

## How It Works

The app displays a card with two buttons: "Yes" and "No". When you try to click "No", it cleverly moves away to a random position! The "Yes" button stays in place, making it the only clickable option. 😉

## Tech Stack

- **Streamlit**: Web app framework
- **Python**: Backend logic
- **HTML/CSS/JavaScript**: Interactive UI

## License

Feel free to use and customize this for your own Valentine's Day! 💖
