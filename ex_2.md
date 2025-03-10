# 🚀 **Exercise: Create a GitHub Action for a Python Script**

## **Objective**
You are tasked with creating a GitHub Action to automate the execution of a Python script that scrapes data and saves the output files. The GitHub Action will:
- Run the scraper.
- Save the output files.
- Commit and push the results back to the repository.

---

## **Background**
You already have seen Python script (`batch_scrape.py`) located in the `app/` folder. The script outputs the scraped data as:
- `scraped_data.json`
- `scraped_data.csv`

Your goal is to create a GitHub Action that:
- Installs dependencies.
- Runs the scraper.
- Pushes the results to the repository.

---

## **Instructions**
### 🏆 **Step 1: Create the GitHub Action YAML File**
1. Create the following folder in your project:
'.github/workflows/'

2. Create a new file in that folder:
'.github/workflows/batch_scraper.yml'

---

### 🏆 **Step 2: Define the GitHub Action Workflow**
- The workflow file should have the following sections:

#### ✅ **1. Define the workflow name and trigger**
- Name the workflow `"Run Batch Scraper and Save Files"`.
- Use `workflow_dispatch` to allow manual triggering of the workflow.

---

#### ✅ **2. Create a job to run the scraper**
- The job should:
  - Run on `ubuntu-latest`.

---

#### ✅ **3. Step: Checkout the code**
- Use the `actions/checkout@v3` action to clone the repository.

---

#### ✅ **4. Step: Set up Python**
- Use the `actions/setup-python@v4` action to set up Python.
- Set the Python version to `3.9`.

---

#### ✅ **5. Step: Install dependencies**
- Upgrade `pip`.
- Install the required dependencies from `requirements.txt`.

---

#### ✅ **6. Step: Run the scraper**
- Run the `batch_scrape.py` script using Python.

---

#### ✅ **7. Step: Commit and push the results**
- Set up the GitHub bot for committing.
- Add the scraped files.
- Commit the changes with a meaningful message.
- Push the changes to the repository using `GITHUB_TOKEN`.

---