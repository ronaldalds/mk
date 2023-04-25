class Coin:
    def __init__(self):
        self._crm = { 'title':'CRM', 'id': '1791381'}
        self._gestao = {'title':'Gestão', 'id': '1856707'}
        self._financeiro = {'title':'Financeiro', 'id': '946094'}
        self._workspace = {'title':'Workspace', 'id': '1833270'}
        self._estoque = {'title':'Estoque', 'id': '1200344'}
        self._tecnico = {'title':'Técnico', 'id': '1511788'}
        self._integradores = {'title':'Integradores', 'id': '169073'}
        self._maps = {'title':'Maps', 'id': '1162115'}
        self._suporte = {'title':'Suporte', 'id': '1631783'}
        self._ajuda = {'title':'Ajuda', 'id': '1185636'}
        self._home = {'title':'Home', 'id': '1504596'}
        self._configuracoes = {'title':'Configurações', 'id': '545976'}

    def crm(self):
        return self._crm
class Crm(Coin):
    def __init__(self):
        super().__init__()
        self._painelDinamico = {'title': 'Painel Dinâmico', 'id': '388243'}
        self._geradorDeInviabilidades = {'title': 'Gerenciador de Inviabilidades', 'id': '1052995'}
        self._gerenciadorDeFechamento = {'title': 'Gerenciador de Fechamento', 'id': '539320'}
        self._gerenciadorDeComissoes = {'title': 'Gerenciador de Comissões', 'id': '887989'}
        self._gerenciadorDeCancelamento = {'title': 'Gerenciador de Cancelamento', 'id': '1406061'}
        self._mapaDeCrm = {'title': 'Mapa de CRM', 'id': '1998852'}

    def painelDinamico(self, coin: bool = False):
        if coin: return super().crm()
        return self._painelDinamico

    def geradorDeInviabilidades(self, coin: bool = False):
        if coin: return super().crm()
        return self._geradorDeInviabilidades