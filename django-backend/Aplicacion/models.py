from django.db import models

class Cliente(models.Model):
     nombre = models.CharField(verbose_name="Nombre", max_length=100, blank=True, null=True)
     cedula = models.CharField(verbose_name="Cedula", max_length=10, blank=True, null=True)
     apellido = models.CharField(verbose_name="Apellido", max_length=100, blank=True, null=True)
     celular = models.CharField(verbose_name="Celular", max_length=10, blank=True, null=True)
     
     def __str__(self):
        return self.nombre

     class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
   
class Propiedad(models.Model):
    cedula = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=200, blank=True, null=True)
    direccion = models.CharField(verbose_name="Direccion", max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.direccion

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

class Tarifa(models.Model):
     tarifa= models.CharField(verbose_name="Tarifa", max_length=200, blank=True, null=True)
     Valor = models.CharField(verbose_name="Valor", max_length=200, blank=True, null=True)
     
     def __str__(self):
        return self.tarifa

     class Meta:
        verbose_name = 'Tarifa'
        verbose_name_plural = 'Tarifas'


class Medidor(models.Model):
    codigo_pro=models.ForeignKey(Propiedad,on_delete=models.CASCADE,blank=True,null=True)
    codigo_tar=models.ForeignKey(Tarifa,on_delete=models.CASCADE,blank=True,null=True)
    estado = models.BooleanField( default=True)
    
    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Medidor'
        verbose_name_plural = 'Medidores'

class Lectura(models.Model):
     Num_med=models.ForeignKey(Medidor,on_delete=models.CASCADE,blank=True,null=True)
     fecha_lec = models.DateTimeField(auto_now_add=False, null=True)
     periodo_consumo = models.DurationField(blank=True, null=True)
     lec_anterior = models.DateTimeField(auto_now_add=False, null=True)
     lec_actual = models.DateTimeField(auto_now_add=False, null=True)
     estado = models.BooleanField( default=True)
     


class Concepto(models.Model):
    concepto= models.FloatField( blank=True, null=True)
    valor= models.FloatField( blank=True, null=True)

class Cabecera_Planilla(models.Model):
    cedula = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    observacion = models.CharField(verbose_name="Descripcion", max_length=200, blank=True, null=True)
    interes_mora=models.IntegerField(verbose_name="Interes",blank=True,null=True)
    imp_med_amb=models.IntegerField(verbose_name="Impuesto",blank=True,null=True)
    subtotal= models.FloatField( blank=True, null=True)
    descuento= models.FloatField( blank=True, null=True)
    base= models.FloatField( blank=True, null=True)
    descuento=models.IntegerField(verbose_name="Interes",blank=True,null=True)
    total= models.FloatField( blank=True, null=True)

class Detalle_Planilla(models.Model):
    numero = models.ForeignKey(Cabecera_Planilla,on_delete=models.CASCADE,blank=True,null=True)
    codigo_lec= models.ForeignKey(Lectura,on_delete=models.CASCADE,blank=True,null=True)
    codigo_con = models.ForeignKey(Concepto,on_delete=models.CASCADE,blank=True,null=True)
    medidor = models.ForeignKey(Medidor,on_delete=models.CASCADE,blank=True,null=True)
    Precio_unit= models.FloatField( blank=True, null=True)
    Precio_total= models.FloatField( blank=True, null=True)