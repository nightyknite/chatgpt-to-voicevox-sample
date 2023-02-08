import os
import openai
from dotenv import load_dotenv

def answer(main_text, pre_text=""):
    HISTORY_PATH='history.log'
    # .envファイルの内容を読み込み
    load_dotenv()
    openai.api_key = os.environ['api_key']

    history = ''
    # リセットフラグが立っていない&ファイルが存在する場合履歴を読み込む
    if os.path.isfile(HISTORY_PATH):
      with open(HISTORY_PATH, 'r') as f:
        history = f.read()
    # 会話として推論するため、会話ログを付け足してリクエストする
    prompt = history + main_text
    response = openai.Completion.create(
      model='text-davinci-003',
      prompt=pre_text + prompt,
      temperature=0, # ランダム性の制御[0-1]
      max_tokens=1000, # 返ってくるレスポンストークンの最大数
      top_p=1.0, # 多様性の制御[0-1]
      frequency_penalty=0.0, # 周波数制御[0-2]：高いと同じ話題を繰り返さなくなる
      presence_penalty=0.0 # 新規トピック制御[0-2]：高いと新規のトピックが出現しやすくなる
    )
    
    texts = ''.join([choice['text'] for choice in response.choices])

    # 会話履歴の保存
    with open(HISTORY_PATH, 'w') as f:
      f.write(prompt)
      f.write(texts)
      # 文の切れ目に改行を追加
      f.write('\n\n')
    return texts

if __name__ == "__main__": 
    print(answer("犬はなんと鳴きますか？", "語尾になのだをつけてください"))