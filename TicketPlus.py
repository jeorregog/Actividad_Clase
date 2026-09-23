import EmailDummy as EmailDummy
import Spy as InventarioSpy
import InventarioStub as InventarioStub
from unittest.mock import Mock
import RepositorioFake as RepositorioFake
import Usuario as Usuario

email_mock = Mock()
inventario_spy = InventarioSpy.InventarioSpy()
class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
    
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)  
      return True
   
#service = TicketService()
#service = TicketService(None, None, None)
#service = TicketService(InventarioStub.InventarioStub(), None, None)
#serice = TicketService(InventarioStub.InventarioStub(), Usuario.Usuario(), None)
#service = TicketService(InventarioStub.InventarioStub(), RepositorioFake.RepositorioFake(), None) 
#service = TicketService(InventarioStub.InventarioStub(), RepositorioFake.RepositorioFake(), email_mock())
#resultado = service.comprar("Ana",2)
#resultado = service.comprar(Usuario.UsuarioDummy(), 2)
#print(resultado)
#email_mock.enviar_confirmacion.assert_called_once()

service = TicketService(inventario_spy, 
RepositorioFake.RepositorioFake(),
email_mock)
service.comprar(Usuario.UsuarioDummy(), 2)
print (inventario_spy.veces_consultado)

service.comprar(Usuario.UsuarioDummy(), 2)
print (inventario_spy.veces_consultado)