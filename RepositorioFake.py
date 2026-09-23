class RepositorioFake:
    def __init__(self):
        self.compras = []

    def guardar(self, usuario, cantidad):
        self.compras.append({
            "usuario": usuario,
            "cantidad": cantidad
        })

#repo = RepositorioFake()
#repo.guardar("Ana", 2)
#repo.guardar("Juan", 3)
#print(repo.compras)