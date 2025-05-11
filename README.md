# Welcome to the Market Eye AI project! 🎉 
This is where we build a smart AI system to help analyze stock data, predict future stock prices, and generate investment recommendations. 
All of this will be available in a user-friendly web app powered by Streamlit!


# 🚀 Getting Started

1. Clone the Repo
First, let's grab the code from GitHub. Open your terminal and run this:

git clone https://github.com/khadijalseiari/market-eye-ai.git
cd market-eye-ai

2. Install the Dependencies
We use a requirements.txt file to manage all the Python packages we need. Install them with:

pip install -r requirements.txt

# 🔧 Backend Setup

1. Set Up the Database
Our app uses SQLite to manage users and track activities. Before anything else, we need to set up the database.

Run this Python script to create the necessary tables:

from backend.db import init_db
init_db()  

#This will set up everything!

2. Start the Backend (FastAPI)
To run the backend (where the logic and data processing happens), use this command:

uvicorn backend.app:app --reload

This will start the backend at http://127.0.0.1:8000.

3. What the Backend Does
The backend handles things like:

User login and authentication
Logging user activities (like when they sign in or use the app)
Handling data and running the AI agents

# 🌐 Frontend Setup

1. Running the Streamlit App
For the user interface (UI), we’re using Streamlit. To run the frontend, use this command:

streamlit run frontend/app.py

This will open up the web app at http://localhost:8501, where you can interact with everything!

2. What the Frontend Does
The Streamlit app lets users:

Sign up, log in, and view their account
Select stock tickers (companies) to analyze
See the stock analysis and predictions
Download detailed reports as PDFs
Get investment recommendations powered by AI

# 🛠️ Working with the Database

1. Database Tables
The app uses two main tables in the database:

users: Stores account information (like usernames and passwords)
activity_logs: Tracks user actions (like logins or clicks)
Make sure these tables are set up! If you’re not sure, you can use SQLite to check:

sqlite3 path_to_your_db.db

Run these queries to see the data:

SELECT * FROM users;
SELECT * FROM activity_logs;

# 💻 Running Everything Together

To run both the backend and frontend at the same time, follow these steps:

Start the backend:
uvicorn backend.app:app --reload

Start the frontend:
streamlit run frontend/app.py

Now, you can visit http://localhost:8501 in your browser and interact with the app!

# 🤝 How to Contribute

Fork the repository and create your own branch for any changes or new features you want to work on.
Make sure to commit your changes frequently with clear messages.
When you’re ready, open a pull request and describe what changes you’ve made. Don’t forget to mention how we can test your updates!

# 🌟 Helpful Tips
If you run into any issues or errors, double-check that all the required dependencies are installed. You can find them in requirements.txt.
Always pull the latest changes from the main branch before starting on any new tasks to avoid conflicts.
