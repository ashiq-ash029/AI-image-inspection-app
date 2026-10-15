# Invendo AI Academy — Project 1: AI Image Inspection Tool

**Goal:** Upload an image, run a pretrained YOLO object detection model, see an annotated image, and download a CSV report.

This is a **local Streamlit app** developed using **VS Code**. It runs in your browser but the code runs on your own computer; it is not automatically published as a website when you upload the source to GitHub.

## Requirements

- Windows 10/11, **Python 3.11 (64-bit)**, VS Code with Microsoft Python extension
- Git, GitHub account, internet for the first package installation and model download
- Recommended at least 8 GB RAM and sufficient free disk space; use CPU (no GPU required)

## 1. Open in VS Code

Extract the project ZIP to a folder such as `Documents\Invendo-Image-Inspection`.
In VS Code choose **File → Open Folder**, select the extracted folder, and open **Terminal → New Terminal**.

## 2. Create a project-specific Python environment

Preferred VS Code GUI: **Ctrl+Shift+P → Python: Create Environment → Venv → Python 3.11**.
Then **Python: Select Interpreter → .venv**.

Alternative PowerShell commands if you prefer the terminal:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

If you used **Python: Create Environment**, you still need to run the installation command below unless VS Code already installed the requirements automatically:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Run the application

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Your default browser should open at **http://localhost:8501**. Upload a JPG or PNG of cars, chairs, bottles, dogs, or people (only photos you have permission to use). The **first run** can take longer as the pretrained weights are downloaded.

If the terminal shows an error, read the *first relevant error line*, then fix it rather than reinstalling everything blindly.

## 4. Understand the code

| Part | Meaning |
|---|---|
| `st.file_uploader` | Browser input for an image |
| `Image.open` | Reads the image |
| `YOLO("yolo11n.pt")` | Loads a pretrained object detector |
| `model.predict` | Runs inference on the photo |
| `result.plot` | Draws bounding boxes and labels |
| `result.boxes` | Provides object classes, confidence and coordinates |
| `pd.DataFrame` | Creates a table |
| `st.download_button` | Downloads the output image / CSV |

## 5. Practice tasks

1. Upload a different image and explain why the detections change.
2. Compare minimum confidence **0.15** and **0.60**. Count the detections.
3. Change the app title in `app.py` and run again.
4. In the report, identify what X1, Y1, X2, Y2 represent.
5. Explain the difference between a pretrained model and training a model yourself.

**Note:** YOLO's out-of-the-box model detects a defined set of common classes. It does **not** recognize faces by identity, read number plates, or understand a person's intentions.

## 6. Publish code using Git + GitHub

Create a new **empty** GitHub repository named `ai-image-inspection` (do not initialize with a README or `.gitignore`). Then, in the VS Code terminal within the project folder:

```powershell
git --version
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git init
git branch -M main
git add .
git status
git commit -m "Initial AI image inspection app"
git remote add origin https://github.com/YOUR-USERNAME/ai-image-inspection.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. You may be asked to sign in through the browser. If using a privacy-preserving GitHub `noreply` email, use that email in Git config. **Do not put passwords or tokens in code.**

**Publish a second version:** change the title in `app.py`, save it, then:

```powershell
git status
git add app.py
git commit -m "Update application title"
git push
```

Open the GitHub repository page to verify that your updated source is present.

## 7. What should be on GitHub?

Include: `app.py`, `requirements.txt`, `README.md`, `.gitignore`.

Do **not** upload: `.venv`, downloaded `*.pt` weights, private students' photos, `.env`, or credentials.

## 8. Submission

- Link to GitHub repository.
- Screenshot of running app with a test image.
- Downloaded `detections.csv` and annotated output (submit privately to teacher if photos contain people).
- Two observations comparing threshold 0.15 versus 0.60.

## Common troubleshooting

| Problem | What to check |
|---|---|
| `python` or `py` not recognized | Install Python 3.11, restart terminal; check `py -3.11 --version` |
| VS Code does not detect packages | Select `.venv` interpreter; run `.venv\Scripts\python.exe -m pip install -r requirements.txt` |
| Large/slow install | Torch is large. Have stable internet and available disk space |
| First model run slow | Downloading weights / CPU inference |
| `git` not recognized | Install Git for Windows and restart VS Code |
| Git commit asks who you are | Configure Git user.name and user.email |
| GitHub push rejected | Check repository URL, login, and that the GitHub repository was created empty |
| No detections | Try a clearer photo or lower minimum confidence |

## Official references

- VS Code Python getting started: https://code.visualstudio.com/docs/python/python-tutorial
- Streamlit fundamentals: https://docs.streamlit.io/get-started/fundamentals/main-concepts
- Ultralytics predict: https://docs.ultralytics.com/modes/predict/
- About Git (GitHub): https://docs.github.com/en/get-started/using-git/about-git
