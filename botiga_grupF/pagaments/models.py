from django.db import models
from django.contrib.auth import get_user_model
# from .carrito import Carrito
# from .usuarios import Usuarios, UsuariosTarjetas

# tabla de pagos
class Pagos(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    # id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    # id_tarjeta = models.ForeignKey(UsuariosTarjetas, on_delete=models.CASCADE)
    # id_usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# linies comentades per poder executar i provar el funcionament de la ruta confirm_card...