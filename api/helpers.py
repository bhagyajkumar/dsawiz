import requests

API_EXECUTE_URL = "https://emkc.org/api/v2/piston/execute"


def execute_code(runtime: str, version:str, code: str):

    data={
            "language": runtime,
            "version": version,
            "files": [
                {
                    "name": f"main.{runtime}",
                    "content": code
                }
            ]
        }

    req = requests.post(
        API_EXECUTE_URL,
        json=data
    )

    resp = req.json()
    return resp
