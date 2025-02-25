
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "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"  # 🔹 Coloque sua chave real aqui


app = Flask(__name__

# 🚀 Garantindo que a variável de ambiente seja carregada corretamente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "API do Chatbot está rodando no Render!"

@app.route('/pergunta', methods=['POST'])
def responder_pergunta():
    try:
        dados = request.json
        if not dados or "pergunta" not in dados:
            return jsonify({"erro": "Envie uma pergunta válida no formato JSON."}), 400

        pergunta = dados.get("pergunta")

        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o Professor Caqui, um assistente do Metodo M5, que responde dúvidas sobre aulas e materiais."},
                {"role": "user", "content": pergunta}
            ]
        )

        return jsonify({"resposta": resposta["choices"][0]["message"]["content"]})

    except openai.error.AuthenticationError:
        return jsonify({"erro": "Erro de autenticação na OpenAI. Verifique sua API Key."}), 401
    except openai.error.OpenAIError as e:
        return jsonify({"erro": f"Erro na API OpenAI: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
