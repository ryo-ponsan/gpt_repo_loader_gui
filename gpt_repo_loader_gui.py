import streamlit as st
import subprocess
import os
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve paths from the configuration file
script_directory = config.get('Paths', 'script_directory')
default_repo_path = config.get('Paths', 'repo_path')
default_output_path = config.get('Paths', 'output_path')

# Streamlit UI
st.title("GPT Repository Loader GUI")

# Explanation for the Git Repository Path input
st.markdown("### Please enter the path to your local Git repository:")

# Input fields for the repository path and output file path
repo_path = st.text_input("**Git Repository Path (Required)**", default_repo_path, help="Enter the full path to your local Git repository.")
output_path = st.text_input("Output File Path", default_output_path, help="Enter the path where the output file should be saved.")

# Button to execute the command
if st.button("Run"):
    script_path = os.path.join(script_directory, "gpt_repository_loader.py")

    if not os.path.exists(script_path):
        st.error(f"Script not found: {script_path}")
    else:
        command = f"python {script_path} {repo_path} -o {output_path}"
        
        try:
            subprocess.run(command, shell=True, check=True, cwd=script_directory)
            st.success(f"Command executed successfully: {command}")
        except subprocess.CalledProcessError as e:
            st.error(f"An error occurred: {e}")
        
        # Check if the output file exists and display its contents
        if os.path.exists(output_path):
            # Always read the file with UTF-8 encoding
            with open(output_path, 'r', encoding='utf-8', errors='ignore') as file:
                output_content = file.read()
                st.text_area("Output Content", output_content, height=400)
        else:
            st.error("Output file not found.")
