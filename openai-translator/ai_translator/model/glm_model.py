import requests
import simplejson

from model import Model

class GLMModel(Model):
    def __init__(self, model_url: str, timeout: int):
        self.model_url = model_url
        self.timeout = timeout

    def make_request(self, prompt):
        try:
            headers = {
                'Authorization': 'Bearer <id>',
                'Content-Type': 'application/json'
            }
            payload = {
                "model": "glm-4",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            response = requests.post(self.model_url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()
            response_dict = response.json()
            translation = response_dict["choices"][0]["message"]["content"]
            return translation, True
        except requests.exceptions.RequestException as e:
            raise Exception(f"请求异常：{e}")
        except requests.exceptions.Timeout as e:
            raise Exception(f"请求超时：{e}")
        except simplejson.errors.JSONDecodeError as e:
            raise Exception("Error: response is not valid JSON format.")
        except Exception as e:
            raise Exception(f"发生了未知错误：{e}")
        return "", False
