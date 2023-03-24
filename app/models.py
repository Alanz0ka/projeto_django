from django.db import models

# Ccreate your models here.


class paginainicial (models.Model):
    home_text  = models.BigAutoField(primary_key=True)
    publicacao_date = models.DateTimeField( ' date published ' )



class  cadastro( models.Model ):
    escolha= models.CharField( max_length=20)
    home_text= models.ForeignKey( paginainicial, on_delete=models. CASCADE)
    

class aluno( models.Model ):
    cpf= models.CharField( max_length=14)
    senha= models.CharField( max_length=8) 
    matricula= models.IntegerField( max_length=10)
    escolha_text= models.ForeignKey(cadastro, on_delete=models. CASCADE)

class servidor( models.Model ):
    email= models.CharField( max_length=30)
    senha= models.CharField( max_length=8) 
    escolha_text= models.ForeignKey(cadastro, on_delete=models. CASCADE)

class alerta( models.Model ):
    concordo_text  = models.CharField( max_length=20)
    nãoconcordo_text  = models.CharField( max_length=20)

class duvidas( models.Model ):
    materia= models.CharField(max_length=8)
    pergunta= models.CharField(max_length=200)
    resposta=  models.CharField(max_length=150) 




