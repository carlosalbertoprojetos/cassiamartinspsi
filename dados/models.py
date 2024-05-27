import datetime
from django.db import models

from ckeditor.fields import RichTextField
from django.utils.html import mark_safe


class Email(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email


class Telefone(models.Model):
    numero = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Telefones"

    def __str__(self):
        return self.numero


# https://acervolima.com/richtextfield-modelos-django/
class Grupo(models.Model):
    titulo = models.CharField(max_length=30)
    texto = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True


class SubGrupo(models.Model):
    sub_titulo = models.CharField(max_length=30)
    sub_texto = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True


# https://github.com/carlosalbertoprojetos/reinosdeferro/blob/master/reinosdeferro/models.py
class TimestampedModel(models.Model):
    data = models.DateField(default=datetime.datetime.now)
    publicado = models.BooleanField(default=False)
    data_publicacao = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


# https://github.com/carlosalbertoprojetos/reinosdeferro/blob/master/reinosdeferro/models.py
class RedeSocial(models.Model):
    nome = models.CharField(max_length=30)
    icone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Home(Grupo):
    foto = models.ImageField(upload_to="home/foto/")
    letreiro = models.JSONField(blank=True, null=True)
    redes_sociais = models.ManyToManyField(RedeSocial)

    class Meta:
        verbose_name_plural = "Home Page"

    def __str__(self):
        return self.titulo

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="200px" />' % self.foto.url)


class Apresentacao(Grupo, SubGrupo):
    foto = models.ImageField(upload_to="apresentacao/foto/")

    class Meta:
        verbose_name_plural = "Apresentação"

    def __str__(self):
        return str(self.titulo)

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="200px" />' % self.foto.url)


class Abordagem(Grupo):

    class Meta:
        verbose_name_plural = "Abordagens"

    def __str__(self):
        return self.titulo


class Indice(TimestampedModel):
    abordagem = models.ForeignKey(Abordagem, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


class IndiceAbordagem(SubGrupo, TimestampedModel):
    indice = models.ForeignKey(Indice, on_delete=models.CASCADE)


# class Experiencia(Grupo):

#     class Meta:
#         verbose_name = "Bloco de Imagem"
#         verbose_name_plural = "Blocos de Imagens"

#     def __str__(self):
#         return self.titulo


# class Bloco(SubGrupo, TimestampedModel):
#     experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
#     titulo = models.CharField(max_length=10)


# class ImagemBloco(SubGrupo, TimestampedModel):
#     bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
#     imagem = models.ImageField()

#     @property
#     def view_image(self):
#         return mark_safe('<img src="%s" width="400px" />' % self.icone.url)
#         view_image.short_description = "Ícone"
#         view_image.allow_tags = True


class Topico(Grupo):

    class Meta:
        verbose_name_plural = "Tópicos"

    def __str__(self):
        return self.titulo


# class SubTopico(SubGrupo, TimestampedModel):
#     topico = models.ForeignKey(Topico, on_delete=models.CASCADE)


# class Mensagem(models.Model):
#     nome = models.CharField(max_length=30)
#     email = models.EmailField()
#     titulo = models.CharField(max_length=30)
#     texto = models.TextField()
#     data = models.DateField(default=datetime.datetime.now)

#     class Meta:
#         verbose_name_plural = "Mensagens"

#     def __str__(self):
#         return self.nome
