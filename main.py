import os
import openai

# API Referrence :https://platform.openai.com/docs/guides/chat/introduction
openai.organization = "ORGANIZATION_ID"  # OpenAI登録組織ID
openai.api_key = "OPENAI_API_KEY"  # APIキーを設定
openai.Model.list()


def request_openai(message_text):
    """メッセージをChatGPTにリクエスト、レスポンスのテキストを返す。
    Args:
        message_text (_str_): ユーザーからの質問文

    Returns:
        _str_: ChatGPTのレスポンスのメッセージ内容
    """
    message_text = message_text
    # OpenAIにリクエストを送信
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message_text},
        ]
    )
    # response check and return
    finish_reason = response['choices'][0]['finish_reason']
    if finish_reason == "stop":  # APIが完全なモデル出力
        return response['choices'][0]['message']['content']
    elif finish_reason == "length":  # パラメータまたはトークンの制限により、不完全なモデル出力
        return (response['choices'][0]['message']['content'] \
                +"トークンの制限により、不完全な回答です。")
    else:  #null: API 応答がまだ進行中または不完全です
        return "回答を得られませんでした。"

if __name__ == '__main__':
    message_text = input('質問内容を記述してください。')
    # message_text = "1900年以降の日本の内閣総理大臣の名前を列挙せよ。"
    res = request_openai(message_text)
    print(res)










