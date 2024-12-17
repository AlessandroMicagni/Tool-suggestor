import requests
from dotenv import load_dotenv
import os

# Load API key from environment variables
load_dotenv()
PREMAI_API_KEY = os.getenv("PREMAI_API_KEY")

# Function to upload a file to an existing repository
def upload_file_to_repository(repo_id, file_path):
    url = f"https://api.prem.ai/v1/repositories/{repo_id}/documents/"  # Prem API endpoint
    headers = {
        "Authorization": f"Bearer {PREMAI_API_KEY}"
    }
    # Open the file in binary mode and upload
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(url, headers=headers, files=files)

        # Handle responses
        if response.status_code == 201:
            print("✅ File uploaded successfully:", response.json())
        else:
            print(f"❌ Failed to upload file. Status: {response.status_code}, Response: {response.text}")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Use an existing repository ID
    repository_id = "your_existing_repository_id"  # Replace with actual repository ID
    file_path = "./tools_and_workflows.txt"  # Ensure this file exists in your directory

    # Upload the file
    upload_file_to_repository(repository_id, file_path)
