"""
Sistema de log para armazenar o historico do sistema e possíveis erros durante o todo o processo

Níveis de log no python (do menos para o mais grave):

- DEBUG: mensagens detalhadas para depuração
- INFO: mensagens informativas sobre o estado do sistema
- WARNING: mensagens de aviso sobre possíveis problemas
- ERROR: mensagens de erro que impedem o funcionamento do sistema
- CRITICAL: mensagens críticas que indicam falhas graves
"""

import logging


def configurar_logger():
    logger = logging.getLogger("Sistemalog")
    # Setar o tipo de nivel de log
    logger.setLevel(logging.DEBUG)

    # Configuração do handler de arquivo para não apagar o conteúdo existente ou antigo
    file_handler = logging.FileHandler("sistema_log.log", mode="a", encoding="utf-8")

    formato = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formato)
    logger.addHandler(file_handler)

    logger.debug("isso é um debug")
    logger.error("isso é um erro")
    return logger


logger = configurar_logger()
info = logger.info("Sistema de gerenciamento iniciado")


try:
    resultado = 10 / 0
except ZeroDivisionError:
    logger.error("Tentativa de divisão por zero detectada")
