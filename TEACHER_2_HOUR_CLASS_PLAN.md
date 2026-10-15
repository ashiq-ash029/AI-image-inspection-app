# Teacher Plan: Two-Hour Class

## Preparation (before class)
- Check Python 3.11, VS Code with Python extension, Git and GitHub sign-in on student laptops.
- Pre-download Python dependencies where possible using `pip install -r requirements.txt` in each student's `.venv`. This can take a while.
- Test the model weights download, or have stable internet.
- Prepare 3 approved JPG files: car + person, indoor chair/table, and a challenging dark/occluded example.
- Put all students in **their own project folders**, not a shared class folder.

## 0–15 min — Why use VS Code, Python environments and Git?
Explain: IDE/editor, integrated terminal, Python interpreter, project folder, library, Git local, GitHub online.
Ask: “Can you send a Python source file alone to another computer and expect it to run without dependencies?”

## 15–30 min — Folder, environment, requirements
- Students extract starter pack and open folder in VS Code.
- Show `app.py`, `requirements.txt`, `.gitignore`, `README.md`.
- Create `.venv` using VS Code GUI; select interpreter.
- Install dependencies (ideally done before class).
- Ask each student to predict what a `.gitignore` does.

## 30–65 min — Build and understand application
- Teacher first shows minimal Streamlit (`st.title("Hello AI")`) and runs it.
- Students progressively inspect and execute sections of `app.py`.
- Highlight the input `st.file_uploader`, load model, predict, annotated image, boxes and CSV.
- Ask students to describe the flow: **image → preprocessing → YOLO → boxes/classes/confidence → displayed report**.
- Define a confidence threshold. Stress: confidence is *not a guaranteed probability of correctness*.

## 65–80 min — Run & test
- Upload first photo; ensure result table and both download buttons are visible.
- Test thresholds 0.15 versus 0.60 and observe effect.
- Try difficult image and discuss missed objects and false alarms.
- No identity recognition or intent inference should be claimed.

## 80–95 min — Git local
- Draw: working files → Git staging → local commit → remote GitHub.
- Show `git status`, `git init`, `git add .`, `git commit`.
- Explain commit as a labeled snapshot, not an online upload.

## 95–110 min — GitHub remote
- Create empty repository on GitHub. Explain Public vs Private.
- Connect origin remote and `git push -u origin main`.
- Check code in browser (README renders, `.venv` and weights not present).

## 110–120 min — Second commit and assessment
- Students change title, commit `Update application title`, push again.
- Verify a second commit appears on GitHub.
- Collect GitHub link, app screenshot, threshold comparison and output files via private classroom submission.

## Assessment rubric (10 points)
- Local app launches / detects objects: 3
- Explains model and thresholds correctly: 2
- Annotated image + CSV produced: 2
- Git commits + push verified: 2
- Privacy / .gitignore respected: 1

## Teacher reminder
The sample application uses a pretrained model and local CPU inference. Uploading code to GitHub does not deploy a live web app. Teaching image detection is not a substitute for lessons in data labeling, training, validation, or recognition systems.
