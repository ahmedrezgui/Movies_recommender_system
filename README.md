# 🎬 Content-Based Movie Recommender System

This project is a **content-based movie recommendation system** that suggests the **top 5 most similar movies** based on the input movie title. It utilizes the [TMDB 10000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and offers an interactive **web interface built with Streamlit**.

---

## 🚀 Features

- ✅ Content-based filtering using movie metadata (genres, keywords, cast, crew, overview, etc.)
- ✅ Suggests **Top 5** similar movies to the input title
- ✅ Fast and intuitive **Streamlit web interface**
- ✅ Built using Python and Pandas

---

## 🧠 How It Works

This recommender system uses a **content-based approach**, where similarity between movies is calculated using:

- **Textual metadata**: genres, overview, cast, keywords, director
- **TF-IDF** and **cosine similarity** to compute movie similarity scores

When a user enters a movie title, the system finds similar movies based on these features and returns the top 5 most relevant ones.

---

## 📁 Dataset

The dataset used is the [TMDB 10000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which includes:
- Movie ID
- Title
- Genres
- Keywords
- Overview
- Cast & Crew
- Production companies

---

## 🛠️ Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn (TF-IDF & Cosine Similarity)
- Streamlit (for web interface)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/ahmedrezgui/movie-recommender.git
cd movie-recommender
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

---

## 📸 Demo

![App Screenshot](screenshot.png)

---

## 📁 Project Structure

```
├── data/
│   ├── tmdb_movies_dataset.csv     # Raw dataset
│   └── movies.csv                  # Preprocessed dataset
│
├── src/
│   ├── model/                      
│   │   └── movies_list.pkl
│   │   └── similarity.pkl
│   │
│   ├── notebooks/                  
│   │   └── preprocessing.ipynb     # Jupyter notebooks for EDA and development
│   │
│   └── web/                        
│       └── app.py                  # Streamlit web interface
│
├── requirements.txt
└── README.md

```

---

## 👨‍💻 Author

Ahmed Rezgui  
Feel free to connect on [LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/ahmed-rezgui-a4983a276/)) or contribute!
