# chatgpt-to-voicebox

chatgptのapiの結果をvoiceboxで読み上げる例

春日部つむぎの声で質問して、ずんだもんの声で回答します。
語尾はなのだを付けるようにします。

voicebox
https://voicevox.hiroshiba.jp/

chatgpt
https://openai.com/blog/chatgpt/


## セットアップ

### voicebox coreのセットアップ

[PythonからVOICEVOX Coreを使ってみる](https://qiita.com/taka7n/items/1dc61e507274b93ee868)

上記を参考に必要なファイルをカレントディレクトリにコピーする。
M1 Macの場合は以下の通り

```

# voicevox_coreのダウンロード
wget https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.1/voicevox_core-0.14.1+cpu-cp38-abi3-macosx_10_7_x86_64.whl

# voicevox_coreのインストール
pip install voicevox_core-0.14.1+cpu-cp38-abi3-macosx_10_7_x86_64.whl

# ONNX Runtimeのダウンロード
wget https://github.com/microsoft/onnxruntime/releases/download/v1.13.1/onnxruntime-osx-universal2-1.13.1.tgz

# ONNX Runtimeファイルを解凍
tar -xvf onnxruntime-osx-universal2-1.13.1.tgz
# libの中身をカレントディレクトリにコピー
cp -pR ./onnxruntime-osx-universal2-1.13.1/lib/* ./

# 辞書ファイルのダウンロード
wget -O open_jtalk_dic_utf_8-1.11.tar.gz https://sourceforge.net/projects/open-jtalk/files/Dictionary/open_jtalk_dic-1.11/open_jtalk_dic_utf_8-1.11.tar.gz/download?use_mirror=jaist

辞書ファイルの解凍
tar -xvf open_jtalk_dic_utf_8-1.11.tar.gz

```

ライブラリをインストール
```
pip install pathlib
pip install simpleaudio
```

動作確認

```
python voicebox.py
```


### chatgptのセットアップ

[ChatGPTで用いられるGPT-3.5系のモデルをAPIから利用してみた](https://qiita.com/kaz2ngt/items/d26dd572bd82fcd3dfd3)

APIの利用方法は上記のサイトを参考にします。

openaiのアカウントを作成し、以下のページで secret API keyを生成します。

https://platform.openai.com/account/api-keys

取得したAPI keyを.envファイルに保存します。
```
touch .env
```

.envファイルの中身は以下の形式とします。
```
api_key=APIキー文字列
```


ライブラリをインストール

```
pip install openai
pip install load_dotenv
```

動作確認

```
python chatgpt.py
```


### main実行

```
python example.py

Enter text: 犬はなんと鳴きますか？


犬はワンと鳴くのだ。
```

