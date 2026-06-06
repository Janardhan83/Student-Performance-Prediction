<h1 align="center">🎓 Student Performance Prediction System</h1>

<p align="center">
  A Machine Learning Web Application that predicts a student's Performance Index
  based on study habits, previous scores, sleep hours, extracurricular activities,
  and sample paper practice.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project uses a <b>Multiple Linear Regression</b> model to predict a student's
overall performance based on several academic and lifestyle factors.
</p>

<p>
The trained model is deployed using <b>Flask</b> and can be accessed through a simple
web interface where users enter student information and receive a predicted performance score.
</p>

<hr>

<h2>🎯 Problem Statement</h2>

<p>
Educational institutions often want to understand which factors influence
student performance. This project aims to build a predictive system that estimates
student performance using historical student data.
</p>

<p>
The model helps demonstrate how Machine Learning can be applied to educational analytics.
</p>

<hr>

<h2>📊 Dataset Features</h2>

<table border="1" cellpadding="8">
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Hours Studied</td>
<td>Number of hours studied per day</td>
</tr>

<tr>
<td>Previous Scores</td>
<td>Academic scores obtained previously</td>
</tr>

<tr>
<td>Extracurricular Activities</td>
<td>Participation in extracurricular activities (Yes/No)</td>
</tr>

<tr>
<td>Sleep Hours</td>
<td>Average sleeping hours per day</td>
</tr>

<tr>
<td>Sample Question Papers Practiced</td>
<td>Number of sample papers solved</td>
</tr>

<tr>
<td>Performance Index</td>
<td>Target variable</td>
</tr>

</table>

<hr>

<h2>⚙️ Machine Learning Workflow</h2>

<h3>Step 1: Data Collection</h3>

<ul>
<li>Load dataset using Pandas</li>
<li>Explore dataset structure</li>
<li>Check missing values</li>
<li>Understand feature distributions</li>
</ul>

<h3>Step 2: Data Preprocessing</h3>

<ul>
<li>Convert categorical values into numerical format</li>
<li>
Extracurricular Activities:
<ul>
<li>Yes → 1</li>
<li>No → 0</li>
</ul>
</li>
</ul>

<h3>Step 3: Feature Selection</h3>

<p>
Independent Variables (X):
</p>

<ul>
<li>Hours Studied</li>
<li>Previous Scores</li>
<li>Extracurricular Activities</li>
<li>Sleep Hours</li>
<li>Sample Question Papers Practiced</li>
</ul>

<p>
Dependent Variable (Y):
</p>

<ul>
<li>Performance Index</li>
</ul>

<h3>Step 4: Train-Test Split</h3>

<ul>
<li>Training Data = 75%</li>
<li>Testing Data = 25%</li>
<li>Random State = 42</li>
</ul>

<h3>Step 5: Model Training</h3>

<p>
The model is trained using:
</p>

<pre>
LinearRegression()
</pre>

<h3>Step 6: Model Evaluation</h3>

<p>
The following evaluation metrics are used:
</p>

<ul>
<li>R² Score</li>
<li>Root Mean Squared Error (RMSE)</li>
</ul>

<h3>Step 7: Model Serialization</h3>

<p>
The trained model is saved using Pickle:
</p>

<pre>
s_mlr.pkl
</pre>

<h3>Step 8: Deployment</h3>

<p>
The model is deployed using Flask and Gunicorn.
</p>

<hr>

<h2>🛠 Technologies Used</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Matplotlib</li>
<li>Seaborn</li>
<li>Scikit-Learn</li>
<li>Flask</li>
<li>Gunicorn</li>
<li>HTML</li>
<li>Pickle</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
Student-Performance-Prediction/
│
├── app.py
├── model.py
├── requirements.txt
├── Procfile
├── README.md
├── s_mlr.pkl
├── Student_Performance.csv
│
├── templates/
│   └── index.html

</pre>

<hr>

<h2>🚀 Installation Guide</h2>

<h3>1. Clone Repository</h3>

<pre>
git clone https://github.com/your-username/Student-Performance-Prediction.git
</pre>

<h3>2. Move into Project Folder</h3>

<pre>
cd Student-Performance-Prediction
</pre>

<h3>3. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4. Run Flask Application</h3>

<pre>
python app.py
</pre>

<h3>5. Open Browser</h3>

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>🖥 Web Application Workflow</h2>

<pre>
User Input
     ↓
HTML Form
     ↓
Flask Application
     ↓
Pickle Model
     ↓
Prediction
     ↓
Result Displayed
</pre>

<hr>

<h2>📈 Model Performance</h2>

<p>
Performance metrics are calculated on both training and testing datasets.
</p>

<ul>
<li>R² Score</li>
<li>Root Mean Squared Error (RMSE)</li>
</ul>

<p>
These metrics help evaluate the accuracy and generalization capability of the model.
</p>

<hr>

<h2>📷 Application Screenshots</h2>

<p>
Add screenshots after deployment:
</p>

<ul>
<li>Home Page Screenshot</li>
<li>Prediction Result Screenshot</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>Add advanced feature engineering</li>
<li>Implement multiple regression algorithms</li>
<li>Perform hyperparameter tuning</li>
<li>Create a responsive UI design</li>
<li>Deploy on cloud platforms</li>
<li>Add user authentication</li>
<li>Store prediction history</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Janardhan m</b><br>
Aspiring Data Scientist<br>
Passionate about Machine Learning, Data Science, and Generative AI.
</p>

<hr>

<h2>⭐ If you found this project useful</h2>

<p>
Please consider giving this repository a star.
</p>

<p align="center">
⭐ Thank You For Visiting This Repository ⭐
</p>
