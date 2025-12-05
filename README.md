# CFG Parser (CYK Algorithm)

A Python implementation of a Context-Free Grammar (CFG) parser using the Cocke-Younger-Kasami (CYK) algorithm. This project determines if a string belongs to a given grammar and visualizes the derivation tree.

## 📋 Project Description
This tool accepts a Context-Free Grammar (in Chomsky Normal Form) and an input string. It uses a dynamic programming approach (CYK) to parse the string. If the string is valid, the program generates and prints the parse tree structure to the console.

**Key Features:**
* **Modular Design:** Split into Grammar, Normalizer, Parser, and Visualizer modules.
* **Validation:** Checks if the input grammar follows CNF rules.
* **Visualization:** Text-based hierarchical printout of the parse tree.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Installation
1.  Clone this repository or download the source code.
2.  Navigate to the project directory.

### Usage
1.  Open `cfg_parser.py`.
2.  Modify the `grammar_text` variable in the `__main__` section to define your rules.
    * *Note: Rules must be in Chomsky Normal Form (e.g., A -> BC or A -> 'a').*
3.  Set the `test_string` variable to the string you want to test.
4.  Run the script:

```bash
python cfg_parser.py
📂 Project Structure (Team Roles)
Member 1: Grammar Structure & Input handling.

Member 2: Grammar Normalization & CNF Validation.

Member 3: CYK Algorithm (Dynamic Programming logic).

Member 4: Tree Reconstruction & Visualization.

📝 Example
Grammar:

Plaintext

S -> AB | BC
A -> BA | 'a'
B -> CC | 'b'
C -> AB | 'a'
Input String: baaba

Output:

Plaintext

String 'baaba' is ACCEPTED! Generating Parse Tree...

S
  B
    b
  C
    A
      a
    ...
👥 Authors
[Member 1 Name]

[Member 2 Name]

[Member 3 Name]

[Member 4 Name]


---

### Part 2: How to Upload to GitHub

You have two options. The **Web Interface** is the easiest if you aren't comfortable with the command line.

#### Option A: The "Easiest" Way (Web Interface)

1.  **Create the Repo:**
    * Go to [GitHub.com](https://github.com) and log in.
    * Click the **+** icon in the top right and select **New repository**.
    * Name it `CFG-Parser`.
    * **Important:** Check the box that says **"Add a README file"**.
    * Click **Create repository**.

2.  **Upload Code:**
    * On your new repository page, click **Add file** -> **Upload files**.
    * Drag and drop your `cfg_parser.py` file here.
    * Click **Commit changes**.

3.  **Update the README:**
    * Click on the `README.md` file in the file list.
    * Click the **Pencil Icon** (Edit).
    * Delete the default text, paste the README content I provided above, and fill in your team names.
    * Click **Commit changes**.

---

#### Option B: The "Professional" Way (Command Line)

If you have Git installed on your computer, do this:

1.  **Create the Repo on GitHub** (Don't check "Add README" this time, leave it empty).
2.  **Open your terminal/command prompt** in your project folder.
3.  **Run these commands in order:**

```bash
# 1. Initialize Git in your folder
git init

# 2. Add your files (python script and readme)
git add .

# 3. Save the changes
git commit -m "Initial commit of CFG Parser"

# 4. Link your computer to the GitHub website
# (Replace the URL below with the link to your specific repo)
git remote add origin https://github.com/YOUR_USERNAME/CFG-Parser.git

# 5. Send the files to GitHub
git push -u origin master