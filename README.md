# 🏦 Bank Customer Churn Prediction :-

**🧠 Project Description:-**

 This project aims to predict whether a customer will churn (leave the bank) based on demographic and account-related features.
 It uses machine learning models trained on real-world customer data to help banks take proactive measures to retain valuable clients.

 
## 📌 Project Overview :-

Customer churn is a major issue in the banking industry. This project uses machine learning to help predict which customers are likely to churn based on historical data.

The model was trained on features like:
- Geography
- Gender
- Credit Score
- Age
- Tenure
 - Balance
 - Number of Products
 - Has Credit Card
 - Is Active Member
 - Estimated Salary
 - Exited (Target variable: 1 = churned, 0 = stayed)

The app allows users to input customer data and receive a **prediction instantly**.


**📊 Dataset :-**

 - Dataset used: https://www.kaggle.com/datasets/kartiksaini18/churn-bank-customer

**🛠️ Built with :-**
- 🧠 Scikit-learn (Random Forest Classifier)
- 📊 Pandas, NumPy, Seaborn, Matplotlib
- 🌐 Streamlit for interactive web app


**💻 App Features :-**

Interactive sliders and dropdowns for user input

Instant churn prediction

Visual feedback on input values

Clear mapping between model features and UI

**⚙️ Preprocessing :-**
- Dropped unnecessary columns: `RowNumber`, `CustomerId`, `Surname`
- Handled categorical variables:
  - Used `OneHotEncoder` on `Geography`
  - Used `LabelEncoder` on `Gender`
- Scaled numerical features with `StandardScaler`
  
**🧪 Model Used :-** 
 - Logistic Regression
 - Desicion tree
 - Random Forest (best performing model)
 - K-Nearest Neighbors

**✅ Best Reasult :-**
 **Random Forest with GridSearchCV**
  - Accuracy: 0.85
  - Precision (churn): 0.63
  - Recall (churn): 0.61
  - F1-score (churn): 0.62
  - Non-churn (f1 , precision , recall) : 0.91
 
 **📈 Feature Importance :-** 
 
   Identified important features influencing churn, including:
   - Age
   - Balance
   - Is Active Member
   - Geography (Germany)
   - Credit Score

**🚀How to Run Offline :-**
  -  Clone the repo
     
    git clone https://github.com/YamenRM/Churn-Bank-Model.git
  
    cd Churn-Bank-Model

-  Install dependencies
 
       pip install -r requirments

-  Run the main notebook
  
   - Model.ipynb

**Or**

**You can launch the app locally :-**

```bash
streamlit run app.py
```


**👨‍💻 Author :-**

- YamenRM , 3RD Year AI ENGINNER at UP , Gaza
  
**stay strong 💪💪**
