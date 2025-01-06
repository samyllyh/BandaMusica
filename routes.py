from flask import Blueprint, request
from datetime import datetime
from operation.use_equipamentoSuporte import CreateEquipamentoSuporte
from operation.use_evento import CreateEvento
from operation.use_integrante import CreateIntegrate
from operation.use_intrumento import CreateInstrumento
from operation.use_toca import CreateToca
from operation.use_utiliza import CreateUtiliza

api_bp = Blueprint("api_bp", __name__)

@api_bp.route("/api/integrante",  methods=["GET", "POST"])
def list_integrantes():
    if request.method == 'POST': return CreateIntegrate.create_integrante()
    elif request.method == 'GET': return CreateIntegrate.buscar_all_integrante()
    else: return "Metodo nao encontrado"

@api_bp.route("/api/integrante/<string:cpf>", methods=["GET", "PUT", "DELETE"])
def mani_integrantes(cpf):
    if request.method == "GET": return CreateIntegrate.buscar_integrante(cpf)
    elif request.method == "PUT": return CreateIntegrate.update_integrante(cpf)
    elif request.method == "DELETE": return CreateIntegrate.deletar_integrante(cpf)
    else: return "Metodo nao encontrado"

######################################################################################################

@api_bp.route("/api/instrumento", methods=["GET", "POST"])
def list_instrumento():
    if request.method == 'POST': return CreateInstrumento.create_instrumento()
    elif request.method == 'GET': return CreateInstrumento.buscar_all_instrumento()
    else: return "Metodo nao encontrado"

@api_bp.route("/api/instrumento/<int:id>", methods=["GET", "PUT", "DELETE"])
def mani_instrumento(id):
    if request.method == 'GET': return CreateInstrumento.buscar_instrumento(id)
    elif request.method == 'PUT': return CreateInstrumento.update_instrumento(id)
    elif request.method == 'DELETE': return CreateInstrumento.delete_instrumento(id)
    else: return "Metodo nao encontrado"

########################################################################################################

@api_bp.route("/api/evento", methods=["GET", "POST"])
def list_evento():
    if request.method == 'POST': return CreateEvento.create_evento()
    elif request.method == 'GET': return CreateEvento.get_all_eventos()
    else: return "Método nao encontrado"

@api_bp.route("/api/evento/<string:id>", methods=["GET", "PUT", "DELETE"])
def mani_evento(id):
    if request.method == 'PUT': return CreateEvento.update_evento(id)
    elif request.method == 'DELETE': return CreateEvento.delete_evento(id)

@api_bp.route("/api/<dia>/evento", methods=["GET"])
def get_evento(dia):
    dia_formatado = datetime.strptime(dia, '%Y-%m-%d').date()
    if request.method == 'GET': return CreateEvento.get_evento_by_day(dia_formatado)
    else: return "Método nao encontrado"

########################################################################################################

@api_bp.route("/api/equipamento/<string:cpf>", methods=["GET", "POST", "PUT", "DELETE"])
def list_equipamento(cpf):
    if request.method == 'POST': return CreateEquipamentoSuporte.create_equipamentoSuporte(cpf)
    elif request.method == 'GET' : return CreateEquipamentoSuporte.get_equipamentoSuporte_by_cpf(cpf)
    elif request.method == 'PUT' : return CreateEquipamentoSuporte.update_equipamentoSuporte(cpf)
    elif request.method == 'DELETE': return CreateEquipamentoSuporte.delete_equipamentoSuporte(cpf)
    else: return "Metodo nao encontrado"

@api_bp.route("/api/equipamento", methods=["GET"])
def get_equipamento():
    if request.method == 'GET': return CreateEquipamentoSuporte.get_all_equipamentoSuporte()
    else: return "Metodo nao encontrado"

########################################################################################################
@api_bp.route("/api/toca", methods=["GET", "POST"])
def list_toca():
    if request.method == 'POST': return CreateToca.create_toca()
    else: return "Metodo nao encontrado"

@api_bp.route("/api/toca/<string:cpf>/<string:evento_id>", methods=["GET", "DELETE"])
def mani_toca(cpf, evento_id):
    if request.method == "GET": return CreateToca.get_toca_by_day_and_cpf(cpf, evento_id)
    elif request.method == "DELETE": return CreateToca.delete_toca(cpf, evento_id)
    else: return "Metodo nao encontrado"

########################################################################################################
@api_bp.route("/api/utiliza", methods=["POST"])
def list_utiliza():
    if request.method == 'POST': return CreateUtiliza.create_utiliza()
    else: return "Metodo nao encontrado"

@api_bp.route("/api/utiliza/<string:cpf>", methods=["GET"])
def get_utiliza(cpf):
    if request.method == 'GET': return CreateUtiliza.get_utiliza_by_cpf(cpf)
    else: return "Metodo nao encontrado"

@api_bp.route("/api/utiliza/<string:cpf>/<int:id>", methods=["DELETE"])
def del_utiliza(cpf, id):
    if request.method == 'DELETE': return CreateUtiliza.delete_utiliza(cpf, id)
    else: return "Metodo nao encontrado"