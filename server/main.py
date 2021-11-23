from flask import Flask, jsonify
from flask_cors import CORS
import base64
import time

app = Flask(__name__)
CORS(app)


# Configurações da votação de teste
titulo = "Qual o seu animal favorito?"
data = time.strftime('%d/%m/%Y')
candidatos = ["Cachorro", "Gato"]
uf = "SP"


def loadFoto(filename):
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')


def encode(s):
    # pra que eles fazem isso?? não entendi!
    b = base64.b64encode(s.encode('utf-8') +
                         b'-remover-esse-texto-').decode('ascii')
    return 5*'-' + b[:5] + 5*'!' + b[5:-2] + 10*'@' + b[-2:]


@app.route("/autenticacao/autenticar", methods=['POST'])
def autenticar():
    return jsonify({'primeiroAcesso': False, 'token': 'auth-me-321', 'qualidadeFotoPlugInMobile': 90})


# só se primeiro acesso
@app.route("/eleitor/verificacaoDeDados", methods=['PUT'])
def verificacaoDeDados():
    return jsonify({})


# só se primeiro acesso
@app.route("/eleitor/verificacaoDeDocumentos", methods=['POST'])
def verificacaoDeDocumentos():
    return jsonify({})


@app.route("/eleitor/verificacaoFacial", methods=['POST'])
def verificacaoFacial():
    return jsonify({'ocorrencia': 'blah'})


@app.route("/autenticacao/autenticarEleitor", methods=['POST'])
def autenticarEleitor():
    return jsonify({'token': 'auth-me-123', 'qualidadeFotoPlugInMobile': 90})


@app.route("/eleitor/buscarDocumento", methods=['POST'])
def buscarDocumento():
    return jsonify({})


@app.route("/eleicao/listarEleicao", methods=['GET'])
def listarEleicao():
    return jsonify([{"idEleicao": "1", "tituloEleicao": titulo, "dataInicioEleicao": data, "dataFimEleicao": data, "turno": "1"}])


@app.route("/eleicao/consultarVotacao", methods=['POST'])
def consultarVotacao():
    return jsonify({
        "idEleicao": encode("1"),
        "tituloEleicao": encode(titulo),
        "dataEleicaoIni": encode(data),
        "dataEleicaoFim": encode(data),
        "turno": encode("1"),
        "candidatos": [{
            "idCandidato": encode(str(i)),
            "nome": encode(nome),
            "uf": encode(uf),
            "foto": loadFoto(f"{nome}.jpg")
        } for i, nome in enumerate(candidatos)]
    })


@app.route("/eleicao/confirmarVoto", methods=["POST"])
def confirmarVoto():
    return jsonify({})


@app.route("/eleicao/consultarComprovante", methods=['POST'])
def consultarComprovante():
    return jsonify({
        "titulo": titulo,
        "dataInicioEleicao": data,
        "dataFimEleicao": data,
        "turno": "1",
        "dataHoraVoto": f"{data} às 13:37",
        "chave": "Batatinha frita 123"
    })


@app.route("/eleicao/listarEleicaoVoto", methods=['GET'])
def listarEleicaoVoto():
    return jsonify([{
        "idEleicao": "1",
        "idApuracao": "1",
        "titulo": titulo,
        "dataInicioEleicao": data,
        "dataFimEleicao": data,
        "turno": "1"
    }])


@app.route("/eleicao/listarEleicaoResultados", methods=['GET'])
def listarEleicaoResultados():
    return jsonify([{
        "idEleicao": "1",
        "idApuracao": "1",
        "tituloEleicao": titulo,
        "dataInicioEleicao": data,
        "dataFimEleicao": data,
        "turno": "1"
    }])


@app.route("/eleicao/eleicaoResultado", methods=["POST"])
def eleicaoResultado():
    return jsonify({
        "tituloEleicao": titulo,
        "dataInicioEleicao": data,
        "dataFimEleicao": data,
        "turno": "1",
        "resultados": [{
            "nome": nome,
            "porcentual": str(100//len(candidatos)),
            "avatar": loadFoto(f"{nome}.jpg")
        } for i, nome in enumerate(candidatos)]
    })


if __name__ == '__main__':
    app.run(debug=True, port=8000)
