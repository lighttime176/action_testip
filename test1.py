import requests
import json
import os

def create_gist(github_token, description, filename, content, public=True):
    """
    Create a GitHub Gist and return its ID
    
    Args:
        github_token (str): Your GitHub personal access token
        description (str): Description of the Gist
        filename (str): Filename for the Gist file
        content (str): Content of the Gist file
        public (bool): Whether the Gist should be public (default: True)
        
    Returns:
        str: The ID of the created Gist
    """
    # GitHub API endpoint for creating Gists
    api_url = "https://api.github.com/gists"
    
    # Prepare headers with authorization token
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Prepare data payload
    data = {
        "description": description,
        "public": public,
        "files": {
            filename: {
                "content": content
            }
        }
    }
    
    # Make POST request to create Gist
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    # Check if the request was successful
    if response.status_code == 201:
        response_json = response.json()
        gist_id = response_json["id"]
        gist_url = response_json["html_url"]
        print(f"Gist created successfully!")
        print(f"Gist ID: {gist_id}")
        print(f"Gist URL: {gist_url}")
        return gist_id
    else:
        print(f"Failed to create Gist. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

if __name__ == "__main__":
    # You need to create a GitHub personal access token with the 'gist' scope
    # https://github.com/settings/tokens
    
    # Get token from environment variable or input
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        github_token = input("Enter your GitHub personal access token: ")
    
    # Gist details
    description = "My Python Gist created via API"
    filename = "example.py"
    content = """
def hello_world():
    print("Hello, GitHub Gist!")
    
if __name__ == "__main__":
    hello_world()
"""
    
    # Create the Gist
    gist_id = create_gist(github_token, description, filename, content, public=True)
    
    if gist_id:
        print(f"You can now use this Gist ID for other operations: {gist_id}")
