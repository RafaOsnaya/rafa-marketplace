from django.db import models

# class Category(models.Model):
#     # category_name = models.CharField(max_length=50)
    
#     ROPA = 'ropa'
#     CALZADO = 'calzado'
#     ELECTRONICA = 'electronica'
#     JOYERIA = 'joyeria'
#     HERRAMIENTAS = 'herramientas'
#     ELECTRODOMESTICOS = 'electrodomesticos'
    
#     CATEGORIES_CHOICES = [
#         (ROPA, 'Ropa'),
#         (CALZADO, 'Calzado'),
#         (ELECTRONICA, 'Electronica'),
#         (JOYERIA, 'Joyeria'),
#         (HERRAMIENTAS, 'Herramientas'),
#         (ELECTRODOMESTICOS, 'Eletrodomesticos'),
#     ]


#     def __str__(self):
#         # return self.category_name
#         return '__all__'
    
    
class Product(models.Model):
    
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    ROPA = 'ropa'
    CALZADO = 'calzado'
    ELECTRONICA = 'electronica'
    JOYERIA = 'joyeria'
    HERRAMIENTAS = 'herramientas'
    ELECTRODOMESTICOS = 'electrodomesticos'
    
    CATEGORIES_CHOICES = [
        (ROPA, 'Ropa'),
        (CALZADO, 'Calzado'),
        (ELECTRONICA, 'Electronica'),
        (JOYERIA, 'Joyeria'),
        (HERRAMIENTAS, 'Herramientas'),
        (ELECTRODOMESTICOS, 'Eletrodomesticos'),
    ]

    nombre = models.CharField(max_length=150, null= False)
    marca = models.CharField(max_length=50, null= False)
    modelo = models.CharField(max_length=100, null= False)
    descripcion = models.TextField(max_length=300, null= False)
    estatus = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    categoria = models.CharField(max_length=20, choices=CATEGORIES_CHOICES, default=ROPA)
    precio = models.FloatField(max_length=50, null= False, default=0.0)
    imagen = models.ImageField(upload_to='products/statics/imagenes', null=True)
    
    def __str__(self):
        # return f'{self.nombre} - {self.imagen} - {self.marca} - {self.modelo} - {self.descripcion} - {self.estatus} - {self.categoria}'
        return '__all__'