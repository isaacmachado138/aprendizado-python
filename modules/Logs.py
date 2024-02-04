'''Módulo de Log'''


# Logs


def Logger(level, message):
    '''Função utilizada para exibir logs na tela e salvar no arquivo file.log
    Caso o arquivo ainda não existir ela cria
    Exemplo de chamada:  Logger("warning", "Atenção, parâmetro errado!")
    '''


    import logging
    import os

    # Obtém o caminho absoluto da pasta raiz do projeto
    caminhoRaiz = os.path.abspath(os.path.dirname(__file__))
    caminhoLog = os.path.join(caminhoRaiz, "Log.log") #caminho que sera usado para salvar logs

    logger = logging.getLogger(__name__)

    # verificacao se logger ja existe
    if not (len(logger.handlers)):
        logging.basicConfig(level=logging.INFO)

        # Criando objetos de log para exibir na tela e gravar no arquivo
        streamHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler(caminhoLog)

        # Criando formatação
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Setando formatação
        streamHandler.setFormatter(format)
        fileHandler.setFormatter(format)

        # Adicionando handlers ao logger
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)

        # Setando o nível de erro para o logger
        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)
        else:
            logger.critical(message)

Logger("warning",
       "Atenção, parâmetro errado!")  # Saída esperada: 2024-02-04 16:58:11,584 - __main__ - WARNING - Atenção, parâmetro errado!
