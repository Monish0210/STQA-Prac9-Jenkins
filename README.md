STQA Practical 09 — Jenkins Continuous Testing
This project demonstrates a continuous testing pipeline using Python, PyTest, Git, GitHub and Jenkins.
Files
`calculator.py`: calculator application functions.
`test_calculator.py`: 20 automated test cases.
`requirements.txt`: Python test dependency.
`Jenkinsfile`: pipeline stages for checkout, environment checks, dependency installation and tests.
Run locally (Windows PowerShell)
```powershell
python -m pip install -r requirements.txt
python -m pytest -v
```
Jenkins
Create a Pipeline job and select Pipeline script from SCM:
SCM: Git
Repository URL: your GitHub repository URL
Branch: `*/main`
Script Path: `Jenkinsfile`
The JUnit XML report is generated as `test-results.xml` and published by Jenkins when the JUnit plugin is available.