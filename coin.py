from abc import ABC, abstractmethod
import typing


class Coin(ABC):
    def __init__(
        self,
        title: str,
        id: str,
    ) -> None:
        self._title: str = title
        self._id: str = id
        self._xpath: str = f'//a[@title="{self._title}"]'

    @abstractmethod
    def title(self) -> str:
        pass

    @abstractmethod
    def xpath(self) -> str:
        pass

    @abstractmethod
    def id(self) -> str:
        pass


class Crm(Coin):
    def __init__(self,) -> None:
        super().__init__(title='CRM', id='1791381')

    def title(self) -> str:
        return self._title

    def xpath(self) -> str:
        return self._xpath

    def id(self) -> str:
        return self._id


class Aside:
    class Crm:
        PAINEL_DINAMICO = {'title': 'Painel Dinâmico',
                           'id': '388243', 'xpath': '//a[@title="Painel Dinâmico"]'}
        GERENCIADOR_DE_INVIABILIDADES = {'title': 'Gerenciador de Inviabilidades',
                                         'id': '1052995', 'xpath': '//a[@title="Gerenciador de Inviabilidades"]'}
        GERENCIADOR_DE_FECHAMENTO = {'title': 'Gerenciador de Fechamento',
                                     'id': '539320', 'xpath': '//a[@title="Gerenciador de Fechamento"]'}
        GERENCIADOR_DE_COMISSOES = {'title': 'Gerenciador de Comissões',
                                    'id': '887989', 'xpath': '//a[@title="Gerenciador de Comissões"]'}
        GERENCIADOR_DE_CANCELAMENTO = {'title': 'Gerenciador de Cancelamento',
                                       'id': '1406061', 'xpath': '//a[@title="Gerenciador de Cancelamento"]'}
        MAPA_DE_CRM = {'title': 'Mapa de CRM', 'id': '1998852',
                       'xpath': '//a[@title="Mapa de CRM"]'}

    class Gestao:
        APLICATIVOS_MOVEIS = {'title': 'Aplicativos Móveis',
                              'id': '1310310', 'xpath': '//a[@title="Aplicativos Móveis"]'}
        CONEXOES = {'title': 'Conexões', 'id': '1347324',
                    'xpath': '//a[@title="Conexões"]'}
        CONTRATOS = {'title': 'Contratos', 'id': '1123443',
                     'xpath': '//a[@title="Contratos"]'}
        CRM = {'title': 'CRM', 'id': '1125021', 'xpath': '//a[@title="CRM"]'}
        NET_MAPS = {'title': 'Net Maps', 'id': '646340',
                    'xpath': '//a[@title="Net Maps"]'}
        ORDENS_DE_SERVICO = {'title': 'Ordens de Serviço',
                             'id': '1695691', 'xpath': '//a[@title="Ordens de Serviço"]'}
        RECEITAS_E_DESPESAS = {'title': 'Receitas e Despesas',
                               'id': '1226468', 'xpath': '//a[@title="Receitas e Despesas"]'}
        EXTRATOS_SINTETICOS = {'title': 'Extratos Sintéticos',
                               'id': '372612', 'xpath': '//a[@title="Extratos Sintéticos"]'}

        class ExtratosSinteticos:
            CONCILIACOES = {'title': 'Conciliações',
                            'id': '1879464', 'xpath': '//a[@title="Conciliações"]'}
            CONEXOES_ATUAIS = {'title': 'Conexões atuais',
                               'id': '1088126', 'xpath': '//a[@title="Conexões atuais"]'}
            CONEXOES_EVENTOS = {'title': 'Conexões - Eventos',
                                'id': '341618', 'xpath': '//a[@title="Conexões - Eventos"]'}
            CRM = {'title': 'CRM', 'id': '1640807',
                   'xpath': '//a[@title="CRM"]'}
            ORDENS_DE_SERVICO = {'title': 'Ordens de Serviço',
                                 'id': '801642', 'xpath': '//a[@title="Ordens de Serviço"]'}
            PLANO_DE_CONTAS = {'title': 'Plano de Contas',
                               'id': '1522033', 'xpath': '//a[@title="Plano de Contas"]'}
            PROGRAMACAO_DE_PAGAMENTO = {'title': 'Programação de Pagamento',
                                        'id': '1247005', 'xpath': '//a[@title="Programação de Pagamento"]'}

    class Financeiro:
        PAINEL_DINAMICO = {'title': 'Painel Dinâmico',
                           'id': '218633', 'xpath': '//a[@title="Painel Dinâmico"]'}
        LEITURA_DE_RETORNO = {'title': 'Leitura de Retorno',
                              'id': '845808', 'xpath': '//a[@title="Leitura de Retorno"]'}
        REMESSAS = {'title': 'Remessas', 'id': '1288915',
                    'xpath': '//a[@title="Remessas"]'}
        FATURAMENTO = {'title': 'Faturamento - Painel', 'id': '333317',
                       'xpath': '//a[@title="Faturamento"]'}
        GERENCIADOR_DE_CONCILIACOES = {'title': 'Gerenciador de Conciliações',
                                       'id': '1710589', 'xpath': '//a[@title="Gerenciador de Conciliações"]'}
        GERENCIADOR_DE_FILAS_E_LOTES_DE_EMAILS = {'title': 'Gerenciador de filas e lotes de emails',
                                                  'id': '1958978', 'xpath': '//a[@title="Gerenciador de filas e lotes de emails"]'}
        GERENCIADOR_DE_FLUXO_DE_CAIXAS = {'title': 'Gerenciador de Fluxo de Caixas',
                                          'id': '1650767', 'xpath': '//a[@title="Gerenciador de Fluxo de Caixas"]'}
        GERENCIADOR_DE_CENTRO_DE_CUSTOS = {'title': 'Gerenciador de Centro de Custos',
                                           'id': '1042182', 'xpath': '//a[@title="Gerenciador de Centro de Custos"]'}
        GERENCIADOR_DE_COBRANCAS = {'title': 'Gerenciador de Cobranças',
                                    'id': '1458450', 'xpath': '//a[@title="Gerenciador de Cobranças"]'}
        GERENCIADOR_DE_CONTAS_A_PAGAR = {'title': 'Gerenciador de Contas a Pagar',
                                         'id': '1878993', 'xpath': '//a[@title="Gerenciador de Contas a Pagar"]'}
        GERENCIADOR_DE_CONTAS_A_RECEBER = {'title': 'Gerenciador de Contas a Receber',
                                           'id': '1171825', 'xpath': '//a[@title="Gerenciador de Contas a Receber"]'}
        GERENCIADOR_DE_CONTRATOS = {'title': 'Gerenciador de Contratos',
                                    'id': '1976290', 'xpath': '//a[@title="Gerenciador de Contratos"]'}
        GERENCIADOR_DE_INADIMPLENCIA = {'title': 'Gerenciador de Inadimplência',
                                        'id': '1118213', 'xpath': '//a[@title="Gerenciador de Inadimplência"]'}
        GERENCIADOR_DE_NFSE = {'title': 'Gerenciador de NFSE',
                               'id': '1552812', 'xpath': '//a[@title="Gerenciador de NFSE"]'}
        PROGRAMACAO_DE_PAGAMENTOS = {'title': 'Programação de Pagamentos',
                                     'id': '1391737', 'xpath': '//a[@title="Programação de Pagamentos"]'}
        GERENCIADOR_DE_PLANO_DE_CONTAS = {'title': 'Gerenciador de Plano de contas',
                                          'id': '462340', 'xpath': '//a[@title="Gerenciador de Plano de contas"]'}
        PAINEL_DO_CLIENTE = {'title': 'Painel do Cliente',
                             'id': '639769', 'xpath': '//a[@title="Painel do Cliente"]'}
        PAGSEGURO = {'title': 'PagSeguro', 'id': '1490613',
                     'xpath': '//a[@title="PagSeguro"]'}
        NF_21_22_NFSE_E_NOTA_DE_DEBITO = {'title': 'NF 21/22/NFSE e Nota de débito',
                                          'id': '22857', 'xpath': '//a[@title="NF 21/22/NFSE e Nota de débito"]'}
        TRANSACOES_VIA_CARTAO = {'title': 'Transações via Cartão',
                                 'id': '1439721', 'xpath': '//a[@title="Transações via Cartão"]'}
        TRANSACOES_VIA_PIX = {'title': 'Transações via PIX',
                              'id': '1270636', 'xpath': '//a[@title="Transações via PIX"]'}

    class Workspace:
        PAINEL_DINAMICO = {'title': 'Painel Dinâmico',
                           'id': '555968', 'xpath': '//a[@title="Painel Dinâmico"]'}
        MKBOT_ASSISTANT = {'title': 'MKBot Assistant',
                           'id': '1843438', 'xpath': '//a[@title="MKBot Assistant"]'}
        MKBOT_CHAT = {'title': 'MKBOT - Chat', 'id': '824589',
                      'xpath': '//a[@title="MKBOT - Chat"]'}
        AGENDAMENTOS_DIAGNOSTICO = {'title': 'Agendamentos - Diagnóstico',
                                    'id': '759593', 'xpath': '//a[@title="Agendamentos - Diagnóstico"]'}
        ATENDIMENTOS_DIAGNOSTICO = {'title': 'Atendimentos - Diagnóstico',
                                    'id': '1414703', 'xpath': '//a[@title="Atendimentos - Diagnóstico"]'}
        ATENDIMENTOS_PAINEL = {'title': 'Atendimentos - Painel',
                               'id': '681671', 'xpath': '//a[@title="Atendimentos - Painel"]'}
        O_S_AGENDA = {'title': 'O.S. - Agenda', 'id': '58874',
                      'xpath': '//a[@title="O.S. - Agenda"]'}
        O_S_DIAGNOSTICO = {'title': 'O.S. - Diagnóstico',
                           'id': '1239736', 'xpath': '//a[@title="O.S. - Diagnóstico"]'}
        O_S_MAPA = {'title': 'O.S. -  Mapa', 'id': '1811217',
                    'xpath': '//a[@title="O.S. -  Mapa"]'}
        O_S_PAINEL = {'title': 'O.S. - Painel', 'id': '1117358',
                      'xpath': '//a[@title="O.S. - Painel"]'}
        PESSOAS_OU_EMPRESAS = {'title': 'Pessoas ou Empresas',
                               'id': '176177', 'xpath': '//a[@title="Pessoas ou Empresas"]'}
        PAINEL_DE_RECADOS = {'title': 'Painel de Recados',
                             'id': '263933', 'xpath': '//a[@title="Painel de Recados"]'}
        PAINEL_DE_TAREFAS = {'title': 'Painel de Tarefas',
                             'id': '871824', 'xpath': '//a[@title="Painel de Tarefas"]'}
        CHAT_PAINEL = {'title': 'Chat - Painel', 'id': '25100',
                       'xpath': '//a[@title="Chat - Painel"]'}
        SMS_PAINEL = {'title': 'SMS - Painel', 'id': '418523',
                      'xpath': '//a[@title="SMS - Painel"]'}

    class Estoque:
        PAINEL_DINAMICO = {'title': 'Painel Dinâmico',
                           'id': '1947945', 'xpath': '//a[@title="Painel Dinâmico"]'}
        COMPRA = {'title': 'Compra', 'id': '508868',
                  'xpath': '//a[@title="Compra"]'}
        ESTOQUISTA = {'title': 'Estoquista', 'id': '1638245',
                      'xpath': '//a[@title="Estoquista"]'}
        GERENCIADOR_DE_IDS = {'title': 'Gerenciador de IDs',
                              'id': '1377474', 'xpath': '//a[@title="Gerenciador de IDs"]'}
        GERENCIADOR_DE_IMOBILIZADOS = {'title': 'Gerenciador de Imobilizados',
                                       'id': '589689', 'xpath': '//a[@title="Gerenciador de Imobilizados"]'}
        GERENCIADOR_DE_VEICULOS = {'title': 'Gerenciador de veículos',
                                   'id': '583121', 'xpath': '//a[@title="Gerenciador de veículos"]'}
        PAINEL_DE_DEVOLUCAO = {'title': 'Painel de Devolução',
                               'id': '1314265', 'xpath': '//a[@title="Painel de Devolução"]'}
        PAINEL_DE_NOTAS = {
            'title': 'Painel de Notas (NF-e)', 'id': '1729850', 'xpath': '//a[@title="Painel de Notas (NF-e)"]'}
        RASTREABILIDADE = {'title': 'Rastreabilidade',
                           'id': '1627534', 'xpath': '//a[@title="Rastreabilidade"]'}
        MOVIMENTACAO_SAIDAS = {'title': 'Movimentação - Saídas',
                               'id': '279678', 'xpath': '//a[@title="Movimentação - Saídas"]'}

    class Tecnico:
        PAINEL_DINAMICO = {'title': 'Painel Dinâmico',
                           'id': '191885', 'xpath': '//a[@title="Painel Dinâmico"]'}
        PAINEL_DE_DESCONEXAO = {'title': 'Painel de Desconexão',
                                'id': '1057440', 'xpath': '//a[@title="Painel de Desconexão"]'}
        ANALISE_DE_AUTENTICACOES = {'title': 'Análise de Autenticações',
                                    'id': '1931284', 'xpath': '//a[@title="Análise de Autenticações"]'}
        EQUIPAMENTOS = {'title': 'Equipamentos',
                        'id': '1747898', 'xpath': '//a[@title="Equipamentos"]'}
        ANALISE_DE_TRAFEGO = {'title': 'Análise de Tráfego',
                              'id': '660051', 'xpath': '//a[@title="Análise de Tráfego"]'}
        BLOQ_DESB_POR_ACEITES_ELETRONICOS = {'title': 'Bloq./desb. por aceites eletrônicos',
                                             'id': '1016052', 'xpath': '//a[@title="Bloq./desb. por aceites eletrônicos"]'}
        DIAGNOSTICOS = {'title': 'Diagnósticos',
                        'id': '1304091', 'xpath': '//a[@title="Diagnósticos"]'}
        CONSULTA_DE_ONUS = {'title': 'Consulta de ONUs',
                            'id': '1350035', 'xpath': '//a[@title="Consulta de ONUs"]'}
        INTEGRACOES_DE_RADIUS = {'title': 'Integrações de Radius',
                                 'id': '1409340', 'xpath': '//a[@title="Integrações de Radius"]'}
        HISTORICO_DE_EVENTOS = {'title': 'Histórico de eventos',
                                'id': '148578', 'xpath': '//a[@title="Histórico de eventos"]'}
        IPS_E_ROTAS = {'title': 'IPs e Rotas', 'id': '1971144',
                       'xpath': '//a[@title="IPs e Rotas"]'}
        MK_NETMAPS = {'title': 'MK NetMaps', 'id': '1672987',
                      'xpath': '//a[@title="MK NetMaps"]'}
        NOTIFICACOES_DE_PARADA = {'title': 'Notificações de parada',
                                  'id': '1534349', 'xpath': '//a[@title="Notificações de parada"]'}

        class MkNetMaps:
            PAINEL_DE_CABOS = {'title': 'Painel de cabos',
                               'id': '1986382', 'xpath': '//a[@title="Painel de cabos"]'}
            GERENCIADOR_FTTH = {'title': 'Gerenciador FTTH',
                                'id': '269234', 'xpath': '//a[@title="Gerenciador FTTH"]'}
            PAINEL_DE_DOCUMENTACAO = {'title': 'Painel de documentação',
                                      'id': '1051374', 'xpath': '//a[@title="Painel de documentação"]'}
            DIAGRAMA_DE_REDE = {'title': 'Diagrama de Rede',
                                'id': '1117449', 'xpath': '//a[@title="Diagrama de Rede"]'}
            DIAGRAMA_DE_REDE = {'title': 'Diagrama de Rede',
                                'id': '1117449', 'xpath': '//a[@title="Diagrama de Rede"]'}
            MAPA = {'title': 'Mapa', 'id': '540405',
                    'xpath': '//a[@title="Mapa"]'}
            ELEMENTOS = {'title': 'Elementos', 'id': '991491',
                         'xpath': '//a[@title="Elementos"]'}
            PROVISIONAMENTO = {'title': 'Provisionamento',
                               'id': '1723305', 'xpath': '//a[@title="Provisionamento"]'}
            CABOS_E_POSTES = {'title': 'Cabos e Postes',
                              'id': '422864', 'xpath': '//a[@title="Cabos e Postes"]'}
            RESERVA_DE_PORTAS_DE_ATENDIMENTO = {'title': 'Reserva de portas de atendimento',
                                                'id': '1151903', 'xpath': '//a[@title="Reserva de portas de atendimento"]'}
            IMPORTACAO_DE_DADOS = {'title': 'Importação de dados',
                                   'id': '1957622', 'xpath': '//a[@title="Importação de dados"]'}

    class Integradores:
        INTEGRADORES_HOME = {'title': 'Integradores - Home',
                             'id': '801250', 'xpath': '//a[@title="Integradores - Home"]'}
        EXPORTACOES = {'title': 'Exportações', 'id': '1557924',
                       'xpath': '//a[@title="Exportações"]'}
        GERENCIADOR_DE_EXPORTACOES_DE_DADOS = {'title': 'Gerenciador de exportações de dados',
                                               'id': '1323590', 'xpath': '//a[@title="Gerenciador de exportações de dados"]'}
        GERENCIADOR_DE_LICENCAS = {'title': 'Gerenciador de licenças',
                                   'id': '1867500', 'xpath': '//a[@title="Gerenciador de licenças"]'}
        GERENCIADOR_DE_REPLICADORES = {'title': 'Gerenciador de Replicadores',
                                       'id': '1624043', 'xpath': '//a[@title="Gerenciador de Replicadores"]'}
        GERENCIADOR_DE_WEBSERVICES = {'title': 'Gerenciador de Webservices',
                                      'id': '1852392', 'xpath': '//a[@title="Gerenciador de Webservices"]'}
        GERENCIAMENTO_TV = {'title': 'Gerenciamento TV',
                            'id': '876404', 'xpath': '//a[@title="Gerenciamento TV"]'}
        MK_TALK = {'title': 'MK Talk', 'id': '876404',
                   'xpath': '//a[@title="MK Talk"]'}
        DICI = {'title': 'DICI', 'id': '1418047',
                'xpath': '//a[@title="DICI"]'}
        TELEFONIA = {'title': 'Telefonia', 'id': '1198776',
                     'xpath': '//a[@title="Telefonia"]'}

        class Exportacoes:
            CONFIGURACAO_DE_PADROES = {'title': 'Configuração de Padrões',
                                       'id': '297519', 'xpath': '//a[@title="Configuração de Padrões"]'}
            EXPORTAR = {'title': 'Exportar', 'id': '1021506',
                        'xpath': '//a[@title="Exportar"]'}

        class GerenciamentoTv:
            CLIENTES_DE_TV = {'title': 'Clientes de TV',
                              'id': '567696', 'xpath': '//a[@title="Clientes de TV"]'}
            BIBLIOTECAS = {'title': 'Bibliotecas', 'id': '1606965',
                           'xpath': '//a[@title="Bibliotecas"]'}
            HEADENDS = {'title': 'Headends', 'id': '959848',
                        'xpath': '//a[@title="Headends"]'}
            OPERADORAS = {'title': 'Operadoras', 'id': '1162559',
                          'xpath': '//a[@title="Operadoras"]'}
            OTTS = {'title': 'OTTs', 'id': '1569738',
                    'xpath': '//a[@title="OTTs"]'}

        class MkTalk:
            CADASTRO_DE_PROMOCOES = {'title': 'Cadastro de Promoções',
                                     'id': '324120', 'xpath': '//a[@title="Cadastro de Promoções"]'}
            CADASTRO_DE_RAMAIS = {'title': 'Cadastro de Ramais',
                                  'id': '381343', 'xpath': '//a[@title="Cadastro de Ramais"]'}
            CONFIG = {'title': 'Config', 'id': '1898453',
                      'xpath': '//a[@title="Config"]'}
            DIRECIONAMENTO_DE_CHAMADAS_ENTRANTES = {'title': 'Direcionamento de Chamadas Entrantes',
                                                    'id': '254736', 'xpath': '//a[@title="Direcionamento de Chamadas Entrantes"]'}
            LIGACOES_EM_TEMPO_REAL = {
                'title': 'Ligações em tempo Real (NOVO)', 'id': '1214744', 'xpath': '//a[@title="Ligações em tempo Real (NOVO)"]'}
            LOG_DE_LIGACOES = {'title': 'Log de ligações',
                               'id': '680287', 'xpath': '//a[@title="Log de ligações"]'}
            MEU_RAMAL = {'title': 'Meu Ramal', 'id': '254228',
                         'xpath': '//a[@title="Meu Ramal"]'}
            PAINEL_DE_LIGACOES = {'title': 'Painel de Ligações',
                                  'id': '1351303', 'xpath': '//a[@title="Painel de Ligações"]'}
            PERSONALIZANDO_DASHBOARDS = {'title': 'Personalizando Dashboards',
                                         'id': '153604', 'xpath': '//a[@title="Personalizando Dashboards"]'}
            STATUS_DOS_RAMAIS = {'title': 'Status dos Ramais',
                                 'id': '1017690', 'xpath': '//a[@title="Status dos Ramais"]'}

        class Telefonia:
            ASSINANTES = {'title': 'Assinantes', 'id': '1065899',
                          'xpath': '//a[@title="Assinantes"]'}
            FATURAMENTO = {'title': 'Faturamento', 'id': '810287',
                           'xpath': '//a[@title="Faturamento"]'}
            NUMEROS_VIRTUAIS = {'title': 'Números virtuais',
                                'id': '1516854', 'xpath': '//a[@title="Números virtuais"]'}
            IMPORTACOES = {'title': 'Importações', 'id': '981109',
                           'xpath': '//a[@title="Importações"]'}

    class Maps:
        CONFIGURACOES_GERAIS = {'title': 'Configurações gerais',
                                'id': '880579', 'xpath': '//a[@title="Configurações gerais"]'}
        GERENCIADOR_DE_ELEMENTOS = {'title': 'Gerenciador de Elementos',
                                    'id': '158345', 'xpath': '//a[@title="Gerenciador de Elementos"]'}
        MAPAS = {'title': 'Mapas', 'id': '1136568',
                 'xpath': '//a[@title="Mapas"]'}
        PROVISIONAMENTO = {'title': 'Provisionamento',
                           'id': '451406', 'xpath': '//a[@title="Provisionamento"]'}
        IMPORTACAO_KML = {'title': 'Importação KML',
                          'id': '908602', 'xpath': '//a[@title="Importação KML"]'}

    class Home:
        pass

    class Configuracoes:
        pass

    class Ajuda:
        pass

    class Suporte:
        pass


# class Painel: