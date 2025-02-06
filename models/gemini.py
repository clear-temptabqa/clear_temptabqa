import time
import requests


API_KEY = ""


def gemini(prompt: str) -> str:
    timeout = 30
    url = "https://api.gemini.com/v1/pro-flash"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    while True:
        try:
            response = requests.post(
                url,
                json={"model": "gemini-1.5-pro-flash", "prompt": prompt},
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            print(f"Retrying with timeout {timeout} seconds due to: {e}")
            time.sleep(timeout / 10)
            timeout *= 2
            continue
        except Exception as e:
            print(f"Unhandled exception: {e}")
            exit()
        break

    try:
        response_data = response.json()
        response_str = response_data.get("choices", [{}])[0].get("text", "")
        assert response_str is not None
    except Exception:
        response_str = ""
    return response_str
