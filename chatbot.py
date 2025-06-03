import tkinter as tk
from tkinter import scrolledtext
import random

# chatbot simples com interface gráfica
def chatbot_response(user_input):
    # lista de palavras ofensivas
    offensive_words = open("palavras.txt")
    conteudo = offensive_words.read()
    offensive_words = conteudo.splitlines()
    defensive_responses = ["Chatbot: Por favor, evite falar palavras ofensivas.", "Chatbot: Isso é ofensivo, por favor não fale coisas assim.", "Chatbot: Isso não é legal, as pessoas podem se ofender com isso. "]
    # Checar palavras 
    if any(word in user_input for word in offensive_words):
        return random.choice(defensive_responses)
    
    # palavras-chave e respostas
    responses = {
        "oi": ["Chatbot: Oi, eu estava esperando por você", "Chatbot: Olá, como posso ajudá-lo?", "Chatbot: Opa, tudo certo?"],
        "eae": ["Chatbot: Oi, eu estava esperando por você", "Chatbot: Olá, como posso ajudá-lo?", "Chatbot: Opa, tudo certo?"],
        "olá": ["Chatbot: Oi, eu estava esperando por você", "Chatbot: Olá, como posso ajudá-lo?", "Chatbot: Opa, tudo certo?"],
        "tudo bem": ["Chatbot: Eu sou só um robô, mas estou ótimo!", "Chatbot: É meio solitário dentro do computador, mas estou bem!"],
        "como vai": ["Chatbot: Eu sou só um robô, mas estou ótimo!", "Chatbot: É meio solitário dentro do computador, mas estou bem!"],
        "clima": ["Chatbot: O clima não existe no mundo digital.", "Chatbot: Não sou capaz de sentir o clima, mas em Recife com certeza está calor!"],
        "tempo": ["Chatbot: O tempo climático não existe aqui.", "Chatbot: Não sou capaz de sentir o clima, mas em Recife com certeza está calor!"],
        "Tchau": ["Chatbot: Adeus! Cuidado onde anda!", "Chatbot: Te vejo mais tarde!", "Chatbot: Tchau! Tenha um ótimo dia!"],
        "xau": ["Chatbot: Adeus! Cuidado onde anda!", "Chatbot: Te vejo mais tarde!", "Chatbot: Tchau! Tenha um ótimo dia!"],
        "adeus": ["Chatbot: Adeus! Cuidado onde anda!", "Chatbot: Te vejo mais tarde!", "Chatbot: Tchau! Tenha um ótimo dia!"],
        "default": ["Chatbot: Isto é interessante, me fale mais.", "Chatbot: Sério? Pode elaborar mais?", 
                    "Chatbot: Hmm entendo. O que aconteceu depois?", "Chatbot: Isto é fascinante!", 
                    "Chatbot: Poderia explicar isso melhor?",
                    "Chatbot: Uau! Eu não sabia disso!"],
        "anime": ["Chatbot: Meu anime favorito é Jojo's Bizarre Adventure!"],
        "naruto": ["Chatbot: Eu gosto de Naruto mas prefiro Dragon Ball!"],
        "dragon ball": ["Chatbot: Dragon ball é bem melhor que naruto!"],

    }
    
   
    for keyword, possible_responses in responses.items():
        if keyword in user_input:
            return random.choice(possible_responses)
        elif user_input == "":
            return "Chatbot: Você precisa digitar alguma coisa."


    return random.choice(responses["default"])


def send_message(event=None): 
    user_input = user_entry.get().strip().lower()
    if user_input == "sair":
        root.destroy()  # Fecha a janela se o usuário digitar "exit"
        return
    
    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, f"{response}\n")
    user_entry.delete(0, tk.END)

# Cria a interface gráfica
root = tk.Tk()
root.title("Chatbot")


chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_window.pack(padx=10, pady=10)


user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)


user_entry.bind("<Return>", send_message)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


root.mainloop()