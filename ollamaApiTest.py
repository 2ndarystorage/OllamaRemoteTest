import tkinter as tk
import requests
import json
import threading

# Ollamaにリクエストを送る関数（別スレッドで実行）
def send_to_ollama():
    user_input = entry.get()
    if not user_input.strip():
        return

    # 応答エリアをクリア
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Ollamaに送信中...\n")

    def worker():
        try:
            response = requests.post(
                'http://localhost:11434/api/chat',
                json={
                    "model": "deepseek-r1:14b",
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                },
                stream=True,
                timeout=30
            )

            output_text.delete('1.0', tk.END)  # 再度クリア

            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    content = data.get("message", {}).get("content", "")
                    output_text.insert(tk.END, content)
                    output_text.see(tk.END)  # 常にスクロール

        except Exception as e:
            output_text.insert(tk.END, f"\nエラーが発生しました：{str(e)}")

    threading.Thread(target=worker).start()

# --- GUI部分 ---
root = tk.Tk()
root.title("Ollama Chat")

# 入力欄
entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=10)

# 送信ボタン
send_button = tk.Button(root, text="送信", command=send_to_ollama)
send_button.pack(padx=10, pady=5)

# 応答欄
output_text = tk.Text(root, width=80, height=20)
output_text.pack(padx=10, pady=10)

root.mainloop()