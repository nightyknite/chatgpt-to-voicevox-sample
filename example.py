import readline, voicebox, chatgpt

# 前提条件
pre_text = '語尾に"のだ"や"なのだ"を使って、敬語を使わないで話してください。' 
question_text = input('Enter text: ')
speak_id = 0 # 春日部つむぎの声
voicebox.speak(question_text, speak_id)
answer_text = chatgpt.answer(question_text, pre_text)
speak_id = 1 # ずんだもんの声
voicebox.speak(answer_text, speak_id)
print(answer_text)
