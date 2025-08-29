# Algorithmic-Trading-Platform
Scalable algorithmic trading platform with back testing, paper trading, and monitoring built with production - ready architecture
Backtesting Engine

Ingests free historical price data (via Yahoo Finance API).

Supports multiple strategies (e.g., moving average crossover, RSI, momentum).

Computes performance metrics like Sharpe ratio, drawdown, PnL.

Paper Trading & Live Simulation

Integrated with Alpaca’s free paper trading API.

Event-driven execution engine simulates real-world trade placement.

Trade logs and account balance tracking for auditability.

Risk Management & Strategy Layer

Position sizing rules (fixed, percentage-based).

Stop-loss and take-profit mechanisms.

Modular strategy interface for plugging in custom strategies.

Dashboard & Monitoring

Streamlit-based interface for monitoring open positions and equity curve.

Live updates from broker feeds.

Performance analytics with interactive charts.

Engineering & Deployment

Dockerized services for reproducibility.

GitHub Actions for CI/CD with automated testing.

Modular folder structure for clarity and scalability.

SQLite/PostgreSQL for trade logs and historical storage.

🔹 Tech Stack
Language: Python

Data & Analytics: Pandas, NumPy, Matplotlib

APIs: Yahoo Finance (data), Alpaca (execution)

Backend: SQLite/Postgres for persistence

Frontend: Streamlit (dashboard)

Infra: Docker, GitHub Actions (CI/CD)
