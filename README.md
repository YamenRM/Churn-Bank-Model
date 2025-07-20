# 📌📌 Bank Customer Churn Prediction :-

**🧠 Project Description:-**

 This project aims to predict whether a customer will churn (leave the bank) based on demographic and account-related features.
 It uses machine learning models trained on real-world customer data to help banks take proactive measures to retain valuable clients.
 
**📊 Dataset :-**

 - Dataset used: https://www.kaggle.com/datasets/kartiksaini18/churn-bank-customer
 - Contains information such as:
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
  - Precision (churn): 0.62
  - Recall (churn): 0.62
  - F1-score (churn): 0.62
  - Non-churn (f1 , precision , recall) : 0.91
 
 **📈 Feature Importance :-** 
 
   Identified important features influencing churn, including:
   - Age
   - Balance
   - Is Active Member
   - Geography (Germany)
   - Credit Score

**🚀How to Run :-**
  -  Clone the repo
     
    - git clone https://github.com/YamenRM/Churn-Bank-Model.git
  
    - cd Churn-Bank-Model

-  Install dependencies
 
   - pip install
      pandas , matplotlib , seaborn , scikit-learn

-  Run the main notebook
  
   - Model.ipynb

**Or**

If you have a jupyter notebook or an enviorment to run it you can download the raw data from the Model.ipynb file in the repo.




**🧑‍💻 Author :-**

- YamenRM , 3RD Year AI ENGINNER at UP , Gaza
  
**stay strong 💪💪**
