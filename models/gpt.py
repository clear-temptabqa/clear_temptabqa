import openai
from openai import OpenAI
import time

openai_client = OpenAI(
    api_key=""
)


def gpt3(prompt: str) -> str:
    timeout = 30
    while True:
        try:
            response = openai_client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [{"role": "user", "content": prompt}],
                timeout = timeout
            )
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError, openai.UnprocessableEntityError):
            print(f"retrying with timeout {timeout} seconds")
            time.sleep(timeout/10)
            timeout *= 2
            continue
        except Exception as e:
            print(e)
            exit()
        break

    try:
        response_str = response.choices[0].message.content
        assert response_str is not None
    except Exception:
        response_str = ""
    return response_str


def gpt4(prompt: str) -> str:
    timeout = 30
    while True:
        try:
            response = openai_client.chat.completions.create(
                model = "gpt-4o",
                messages = [{"role": "user", "content": prompt}],
                timeout = timeout
            )
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError, openai.UnprocessableEntityError):
            print(f"retrying with timeout {timeout} seconds")
            time.sleep(timeout/10)
            timeout *= 2
            continue
        except Exception as e:
            print(e)
            exit()
        break

    try:
        response_str = response.choices[0].message.content
        assert response_str is not None
    except Exception:
        response_str = ""
    return response_str
