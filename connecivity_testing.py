import requests

def test_internet_connection():
    try:
        # Test a simple GET request to a public API
        response = requests.get("https://api.github.com")
        if response.status_code == 200:
            print("Internet connection is working. Status Code:", response.status_code)
        else:
            print("Received a non-200 status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

def test_openai_api():
    try:
        # Test a POST request to the OpenAI API
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer "
        }
        data = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hello, OpenAI!"}]
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            print("OpenAI API request succeeded. Status Code:", response.status_code)
        else:
            print("OpenAI API request failed. Status Code:", response.status_code)
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("OpenAI API request failed:", e)

if __name__ == "__main__":
    test_internet_connection()
    test_openai_api()
