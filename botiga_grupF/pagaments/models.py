from django.db import models
from django.contrib.auth import get_user_model
from carrito.models import Carrito
from usuarios.models import Usuarios


# tabla pagos
class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)  # la PK se define como AutoField
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

# id_usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

