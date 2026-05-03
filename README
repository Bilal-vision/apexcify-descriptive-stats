# 🌸 Iris — Descriptive Statistics Dashboard

A Python + Flask web dashboard that loads the Iris dataset and displays
descriptive statistics in a clean dark-themed UI.

---

## 📁 Folder Structure

```
descriptive_stats/
├── app.py                  ← Flask web server
├── descriptive_stats.py    ← Terminal/console version
├── requirements.txt        ← All required libraries
├── README.md               ← This file
└── templates/
    └── index.html          ← Dashboard UI (dark theme)
```

---

## ⚙️ Setup — Run Once

### Step 1 — Create Virtual Environment
```powershell
python -m venv venv
```

### Step 2 — Activate (Windows PowerShell)
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\activate
```

### Step 3 — Install Libraries
```powershell
pip install pandas scikit-learn flask
```

---

## ▶️ Run the Web Dashboard

```powershell
python app.py
Browser automatically open ho jayega!

## 💻 Run Console Version (Terminal only)

```powershell
python descriptive_stats.py
```

---

## 📊 What the Dashboard Shows

| Section                  | Pandas Method                           |
|--------------------------|-----------------------------------------|
| Stat Cards (mean/std)    | df.mean(), df.std()                     |
| Full Summary Table       | df.describe()                           |
| Manual Calculations      | mean(), median(), min(), max(), std()   |
| Range Visual (bar)       | min → mean → max                        |
| Species-wise Breakdown   | df.groupby("species").mean()            |
| First 5 Rows             | df.head()                               |

---

## 🛠️ Libraries Used

| Library        | Purpose                        |
|----------------|--------------------------------|
| pandas         | Data manipulation & statistics |
| scikit-learn   | Loading Iris dataset           |
| flask          | Web server / localhost UI      |

---

## ❓ Common Issues

| Problem                   | Fix                                                                 |
|---------------------------|---------------------------------------------------------------------|
| PowerShell script error   | Run: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned |
| ModuleNotFoundError       | Make sure venv is active, then pip install the missing library      |
| Port already in use       | Change port in app.py: app.run(port=5001)                          |
| templates folder error    | Make sure index.html is inside a folder named templates/            |
