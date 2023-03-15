import os
import json
import openai
from dotenv import load_dotenv

def answer(request_text, system_text=""):
    HISTORY_PATH='history.log'
    # .envファイルの内容を読み込み
    load_dotenv()

    openai.api_key = os.environ['api_key']

    history = []
    if os.path.isfile(HISTORY_PATH):
      with open(HISTORY_PATH, 'r') as f:
        history = json.load(f)
        history.append({"role": "user", "content": request_text})
    else:
      if system_text:
        history.append({"role": "user", "content": request_text})

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=history
    )
    response_content = response["choices"][0]["message"]["content"]

    history.append({"role": "assistant", "content": response_content})
    with open(HISTORY_PATH, mode="w") as f:
      json.dump(history, f)
      f.close()
    return response_content

if __name__ == "__main__": 
    print(answer("犬はなんと鳴きますか？", "語尾になのだをつけてください"))