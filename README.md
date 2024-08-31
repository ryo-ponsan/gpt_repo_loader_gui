# GPT Repository Loader GUI

This project provides a Streamlit-based GUI for the `gpt_repository_loader.py` script, allowing users to easily extract and view information from a Git repository.

## Getting Started

### 1. Clone the Repositories

First, clone the `gpt_repository_loader` repository:

```bash
git clone https://github.com/mpoon/gpt-repository-loader.git
```

Next, clone this project repository:

```bash
git clone https://github.com/ryo-ponsan/gpt_repo_loader_gui.git
```

### 2. Install Python 3 and Required Libraries

Ensure that Python 3 is installed on your system. Then, navigate to the project directory and install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Configuration File

Copy the `config.template.ini` file to create `config.ini`:

```bash
copy config.template.ini config.ini
```

Edit the `config.ini` file to match your environment by setting the following paths:

```ini
[Paths]
# Path to the directory where the script is located (MUST EDIT)
script_directory = C:\path\to\your\gpt-repository-loader

# Default path to the output file (MUST EDIT)
output_path = C:\path\to\your\output\output.txt
```

### 4. Run the Streamlit App

To start the Streamlit UI, run the following command:

```bash
streamlit run .\gpt_repo_loader_gui.py
```

### 5. Using the GUI

In the UI, specify the path to your local Git repository, then click the "Run" button.

Once the `gpt_repository_loader.py` script completes, the extracted information from the Git repository will be displayed on the screen, allowing you to copy and paste the results as needed.

## License

This project is open source and available under the MIT License.