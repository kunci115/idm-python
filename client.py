import socket
from datetime import datetime


def tcp_handler(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('hli-tcp-router-apim.apps.ocp-dev.hanabank.co.id', 32449))
    client_socket.send(bytes(data, encoding='utf-8'))
    reply = client_socket.recv(131072)
    return reply.decode()


def prepare_to_tcp(data):
    try:
        time_stamp = data['Timestamp']
        client_id = data["ClientID"]
        key = data['Key']
        branch_id = data['BranchID']
        counter_id = data['CounterID']
        product_type = data['ProductType']
        trx_type = data['TrxType']
        get_detail_trx_id = data['Detail']['TrxId']
        get_detail_token = data['Detail']['Token']
        no_hp = data['Detail']['noHP']
        amount = data['Detail']['Amount']
        timeout = data['Timeout']
        versi_program = data['VersiProgram']
        resp_code = data['RespCode']
        resp_detail = data['RespDetail']
        time_now = datetime.today().strftime('%Y%m%d%H%M%S')+""
        header_component = "0189"
        switch_code = "RAPI"
        counter = 0000
        n = 0
        data = header_component + switch_code + time_now + f'{n:06}' + "TOKO" +\
               "  " + "IDMCSHO" + time_stamp + client_id+ "    " + key + "    " + branch_id +\
               counter_id + product_type + "    " + trx_type + "                       " + \
               get_detail_trx_id + get_detail_token + no_hp + "    " + amount + "                   "
        return data
    except ValueError as e:
        return e.args
