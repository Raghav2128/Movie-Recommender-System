# 🎬 Movie Recommender System

This project is a content-based movie recommendation system built using **Python**, **Streamlit**, and **Machine Learning techniques**. It allows users to select a movie and get recommendations for similar movies along with their posters using The Movie Database (TMDb) API.

---

## 🚀 Features

- Recommend 5 similar movies based on content similarity
- Fetch posters using TMDb API
- Built with Streamlit for an interactive UI
- Designed with scalability in mind

---

## 🧠 How It Works

- Movie data was processed from a dataset containing over 4,800 movie entries  
- Feature engineering and text vectorization were applied to generate a similarity matrix  
- When a user selects a movie, cosine similarity is used to recommend the top 5 closest matches  

---

## 📁 Project Structure

```
├── app.py                          # Streamlit app
├── movie-recommender-system.ipynb  # Development notebook
├── requirements.txt                # Python dependencies
├── movies.pkl                      # Movie metadata (❌ Not uploaded due to file size limits)
├── similarity.pkl                  # Precomputed similarity matrix (❌ Not uploaded due to file size limits)
```

---

## ⚠️ Missing Files

> The following files were **too large to upload to GitHub**:
- `movies.pkl`: Pickled movie metadata  
- `similarity.pkl`: Pickled similarity matrix  
- Source `.csv` files used for data preprocessing  

These files are required to run the app fully. Please contact the author if you need access.

---

## 🛠️ Getting Started

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Dependencies

- streamlit  
- requests  
- pickle (standard library)

---

## 👤 Author

**Raghav Ramesh**  
GitHub: [@Raghav2128](https://github.com/Raghav2128)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
