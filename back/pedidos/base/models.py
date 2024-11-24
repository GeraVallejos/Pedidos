# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    fecha_despacho = models.DateTimeField(blank=True, null=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nombre = models.CharField(max_length=45)
    unidad = models.CharField(max_length=45, blank=True, null=True)
    cantidad_stock = models.CharField(max_length=45)
    cantidad_inventario = models.CharField(max_length=45, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    costo_compra = models.IntegerField(blank=True, null=True)
    costo_venta = models.IntegerField(blank=True, null=True)
    bodega = models.CharField(max_length=45)
    proveedor = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    obsoleto = models.IntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    comuna = models.CharField(max_length=45)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    rut = models.CharField(unique=True, max_length=45)
    giro = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45, blank=True, null=True)
    password = models.CharField(unique=True, max_length=45)
    cargo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
