
#class formatar os dados em json (NoSQL do Cloud Firestore)
class ProjetoModel:

    def __init__(self,titulo,cliente,data,descricao,equipe,logomarca,pitch,repositorio,tecnologias=list):
        self.titulo = titulo
        self.cliente = cliente
        self.data = data
        self.descricao = descricao
        self.equipe = equipe
        self.logomarca = logomarca
        self.pitch = pitch
        self.repositorio = repositorio
        self.tecnologias = tecnologias

    def toMaps(self):
        return {
            'titulo': self.titulo,
            'cliente': self.cliente,
            'data': self.data,
            'descricao': self.descricao,
            'equipe': self.equipe,
            'logomarca': self.logomarca,
            'pitch': self.pitch,
            'repositorio': self.repositorio,
            'tecnologias': self.tecnologias
            }
    