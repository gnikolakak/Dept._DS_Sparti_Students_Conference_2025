Before proceeding with the analysis of the following codes, it is important to briefly outline the basic steps required for their execution. First, all codes have been implemented using the Python programming language; therefore, it is necessary to install an appropriate development environment, such as PyCharm or Visual Studio Code. Additionally, the required libraries (such as OpenAI, PyPDF2, as well as libraries for mathematical computations and visualization) must be installed to ensure the smooth execution of the programs. Furthermore, a valid API key is required to access OpenAI services, along with the necessary input files (such as .txt or .pdf files) located in the same directory as the code.



---------------------------------


# Parameterized LLM-Based Assessment Generation

## Introduction

This project presents a structured approach for generating assessment-oriented educational material using Large Language Models (LLMs).

Instead of relying on ad hoc prompting, this method introduces a **parameterized pipeline** that controls how assessment content is generated. By explicitly defining parameters such as the number of questions, difficulty level, target audience, and domain, the system ensures that the generated material is **consistent, repeatable, and pedagogically aligned**.

The core idea is to treat LLMs not as autonomous content creators, but as **conditional generators operating within a clearly defined framework**. This is especially important in technical domains (e.g., machine learning), where accuracy, structure, and conceptual clarity are essential.

---

## How to Use

Follow the steps below to set up and use the system.

### 1. Install Required Tools

- Install **Python (version 3.10 or later)**
- Install an IDE:
  - Recommended: **PyCharm**
  - Alternative: VS Code

---

### 2. Clone or Download the Repository

Clone the repository:

```bash
git clone <repository_url>
cd <project_folder>

Or download it as a ZIP file and extract it.

3. Set Up a Virtual Environment (Recommended)

Create a virtual environment:

python -m venv venv

Activate it:

macOS / Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
4. Install Dependencies

If a requirements.txt file exists, install dependencies:

pip install -r requirements.txt
5. Configure API Access

Set up your LLM provider API key (e.g., OpenAI or another provider).

Example using environment variables:

macOS / Linux:

export API_KEY="your_api_key_here"

Windows:

set API_KEY=your_api_key_here
6. Define the Parameter Configuration

Specify the parameter tuple used for generation:

Q: Number of questions

A: Answer options per question

CA: Correct answers per question

DL: Difficulty level

TGA: Target audience

DOM: Domain

Example:

Q = 10
A = 4
CA = 1
DL = 3
TGA = "university-level learners"
DOM = "Machine Learning Optimization (Steepest Descent)"
7. Construct the Prompt

Use the defined parameters to build a structured prompt template.

The prompt should clearly specify:

The task (assessment generation)

Structural constraints (Q, A, CA)

Target audience

Domain

Output format (no explanations, only questions and answers)

8. Run the Generation Process

Execute the main script:

python main.py

This will generate a multiple-choice assessment based on the defined parameters.

9. Review the Generated Output

Evaluate the generated assessment:

Check clarity of questions

Verify correctness of answers

Ensure alignment with domain and difficulty level

Confirm only one correct answer per question

(Optional but recommended: expert review)

10. Iterate and Improve

Refine the output by:

Adjusting parameters (e.g., difficulty level)

Improving the prompt structure

Adding domain-specific reference material

This process is iterative and helps improve output quality over time.

Example Sets

The repository includes two example assessment sets:

Set 1

Set 2

These demonstrate how the parameterized pipeline generates assessment material under controlled configurations.


> The following steps describe the practical implementation workflow of the proposed parameterized pipeline, guiding the user from environment setup to controlled assessment generation and evaluation using an LLM.




