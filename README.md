# Chat with PDF - RAG Application

A Streamlit application that allows users to chat with their documents using Retrieval-Augmented Generation (RAG) powered by Google's Gemini models.

## Features

- Upload and process PDF, DOCX, PPTX files
- Extract text and create vector embeddings
- Chat with your documents using AI
- Supports multiple document formats

## Local Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
6. Run the app: `streamlit run app.py`

## Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Create a GitHub repository and push your code:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin master
   ```

2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select your repository
5. Set the main file path to `app.py`
6. Add your `GOOGLE_API_KEY` in the secrets section:
   ```
   GOOGLE_API_KEY = "your_api_key_here"
   ```
7. Deploy!

### Option 2: Heroku

1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new app: `heroku create your-app-name`
4. Set the buildpack: `heroku buildpacks:set heroku/python`
5. Set environment variables: `heroku config:set GOOGLE_API_KEY=your_api_key`
6. Push to Heroku: `git push heroku master`

### Option 3: Docker

Build and run with Docker:

```bash
docker build -t chat-pdf-app .
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_key chat-pdf-app
```

## Requirements

- Python 3.8+
- Google Gemini API key
- Required packages listed in requirements.txt

## License

MIT