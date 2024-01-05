import requests

def post_comment_on_pull_request(owner, repo, pull_number, token, comment_data):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/comments'
    
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, json=comment_data)

    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        print(f"Failed to post comment. Status code: {response.status_code}")
        print(response.text)

owner = "RavindranathShenoy"
repo = "reviewComment"
pull_number = "1"
token = "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"

comment_data = {
    "body": "03 dec comment",
    "commit_id": "c42e7e7ea8352385d01755f9862d14629d900b7f",
    "path": "main1.py",
    "position": 1
}

post_comment_on_pull_request(owner, repo, pull_number, token, comment_data)
