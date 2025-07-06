# 📊 Share Recommendation System

## Features
- Nifty50/100 stock screener using RSI + MACD strategy
- Entry price, target price, holding days recommendation
- Daily stock scan and signal generation
- Paper trading simulation with P&L tracking
- Flask backend with PostgreSQL
- Scheduler, Telegram bot, and dashboard UI

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
python seed.py
python run.py
```