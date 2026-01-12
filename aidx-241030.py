
 -*- coding: utf-8 -*-
import openai

# OpenAI APIキーを設定
openai.api_key = 'your_api_key_here'

# 応答を生成する関数
def generate_response(question):
    # APIにリクエストを送信
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "あなたは顧客サポートアシスタントです。"},
            {"role": "user", "content": question}
        ],
      temperature=0.5,
      max_tokens=150
    )
    # 応答内容を返す
    return response['choices'][0]['message']['content']

# ユーザーの質問を受け取る
def main():
    print("カスタマーサポートチャットボットへようこそ！")
    while True:
        question = input("お客様のご質問を入力してください（終了するには 'exit' と入力）： ")
        if question.lower() == 'exit':
            print("ご利用ありがとうございました。またのご利用をお待ちしています。")
            break
        response = generate_response(question)
        print("サポート：", response)

# メイン関数を実行
if __name__ == "__main__":
    main()
