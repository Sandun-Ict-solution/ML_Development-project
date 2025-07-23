BottleBot 🍷 - Wine Quality Classification - Machine Learning App

This project demonstrates a complete Machine Learning workflow—from data exploration and model training to deploying an interactive web app using Streamlit.

The objective is to classify red wine samples based on physicochemical features and predict their quality score using a supervised ML model.

📌 Table of Contents

•	📊 Project Overview

•	📁 Dataset Information

•	🧪 Technologies & Libraries

•	📂 Project Structure

•	📸 Features

•	🧠 Machine Learning Model

•	🚀 How to Run the App Locally

•	🌐 Live Deployment

•	📷 Screenshots

•	📄 License

•	👨‍💻 Author

📊 Project Overview
This interactive app allows users to:
- Explore and visualize the Red Wine Quality Dataset
- Input chemical properties of wine samples
- Predict wine quality (score from 0 to 10) using a trained ML model
- View performance metrics such as accuracy and confusion matrix

Built with Streamlit for a user-friendly interface and deployed on Streamlit Cloud.
📁 Dataset Information
- Title: Red Wine Quality Dataset
- Source: Kaggle - Red Wine Quality EDA & Classification (https://www.kaggle.com/datasets/eisgandar/red-wine-quality-eda-classification)
- Description: Contains various chemical features (e.g., acidity, sugar, alcohol, pH) used to classify wine quality.

Download the dataset:
kaggle datasets download -d eisgandar/red-wine-quality-eda-classification

🧪 Technologies & Libraries
- Python 3.8+
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Pickle
  
📂 Project Structure

wine-quality-classifier/

├── app.py                   # Main Streamlit app

├── model.pkl                # Trained ML model

├── requirements.txt         # List of dependencies

├── README.md                # Project documentation

├── data/

│   └── winequality-red.csv  # Dataset (CSV format)

└── notebooks/
  
  └── model_training.ipynb # Data analysis and model training notebook
    
📸 Features
✅ Data Exploration
- Dataset preview and statistics
- Interactive filtering and summary

✅ Data Visualization
- Distribution of wine quality
- Correlation heatmap
- Dynamic charts with user controls

✅ Model Prediction
- User inputs for chemical features
- Instant quality prediction with probability
- Error handling for inputs

✅ Model Performance
- Accuracy, confusion matrix
- Model comparison (optional)
- Real-time feedback display
  
🧠 Machine Learning Model
- Algorithm: Random Forest Classifier
- Preprocessing: Feature scaling and cleaning
- Evaluation: Accuracy, confusion matrix
- Model Serialization: Using pickle
- Target: Wine quality (integer score from 0 to 10)


🚀 How to Run the App Locally
🛠 Prerequisites
- Python 3.8+
- pip
- Git

📦 Steps
1. Clone the Repository

        git clone https://github.com/your-username/wine-quality-classifier.git
        cd wine-quality-classifier

2. Create Virtual Environment

       python -m ml venv

        # Windows:
       venv\Scripts\activate
       # macOS/Linux:
       source venv/bin/activate

3. Install Required Packages

       pip install -r requirements.txt

5. Run the App

       streamlit run app.py

🌐 Live Deployment

🚀 App is live on Streamlit Cloud!

🔗 [Click Here to Access the Live App](https://mldevelopment-project-krcwooehrfjapp9za8vd7ad.streamlit.app/)

📷 Screenshots 

<img width="1903" height="950" alt="Screenshot 2025-07-24 031859" src="https://github.com/user-attachments/assets/ae49e151-255b-4c63-b717-61729c4859f2" />
<img width="1907" height="966" alt="Screenshot 2025-07-24 031830" src="https://github.com/user-attachments/assets/3b017f7d-3c95-4af5-8f46-8ceba801288e" />
<img width="1907" height="982" alt="Screenshot 2025-07-24 031756" src="https://github.com/user-attachments/assets/a00e7c64-5b37-4c8c-9fbe-ae575267719e" />

📄 License

This project is intended for educational and learning purposes only.

Dataset is sourced from Kaggle under the UCI Machine Learning Repository License.

MIT license

👨‍💻 Author

- Name: Sandun Wijesingha

- LinkedIn: www.linkedin.com/in/sandunind98
