from django.contrib import admin
from .models import Produto, Categoria, Cesta, Padaria, Endereco

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cesta)
admin.site.register(Padaria)
admin.site.register(Endereco)