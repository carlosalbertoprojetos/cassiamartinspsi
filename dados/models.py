import datetime
from django.db import models

from ckeditor.fields import RichTextField


class AtualizadorModel(models.Model):
    atual = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.atual:
            # Define 'atual=False' para outras instâncias do mesmo modelo
            self.__class__.objects.filter(atual=True).exclude(id=self.id).update(
                atual=False
            )
        super().save(*args, **kwargs)


class Endereco(AtualizadorModel):
    endereco = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Endereço"

    def __str__(self):
        return self.endereco


class Email(AtualizadorModel):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Email"

    def __str__(self):
        return self.email


class Telefone(models.Model):
    numero = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Telefone"

    def __str__(self):
        return self.numero


class Grupo(AtualizadorModel):
    titulo = models.CharField(max_length=50)
    texto = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True


class SubGrupo(models.Model):
    sub_titulo = models.CharField(max_length=100)
    sub_texto = RichTextField(blank=True, null=True)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    data = models.DateField(default=datetime.datetime.now)
    exibindo = models.BooleanField(default=False)
    data_publicacao = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class RedeSocial(models.Model):
    nome = models.CharField(max_length=30)
    icone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1.1 Rede Social"

    def __str__(self):
        return self.nome


class Home(AtualizadorModel):
    titulo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="home/foto/", blank=True, null=True)
    letreiro = models.JSONField(blank=True, null=True)
    redes_sociais = models.ManyToManyField(RedeSocial)

    class Meta:
        verbose_name_plural = "1 HomePage"

    def __str__(self):
        return self.titulo


class Apresentacao(Grupo, SubGrupo):
    foto = models.ImageField(upload_to="apresentacao/foto/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "2 Apresentação"

    def __str__(self):
        return str(self.titulo)


class Abordagem(Grupo):

    class Meta:
        verbose_name_plural = "3 Abordagem"

    def __str__(self):
        return self.titulo


class IndicesAbordagem(TimestampedModel):
    abordagem = models.ForeignKey(Abordagem, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "3.1 Índice"

    def __str__(self):
        return self.titulo


class TextosIndiceAbordagem(SubGrupo, TimestampedModel):
    indice = models.ForeignKey(IndicesAbordagem, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "3.2 Texto"

    def __str__(self):
        return str(self.indice)


class GrupoExperiencia(models.Model):
    nome = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "4.1 Título Grupo Card"

    def __str__(self):
        return self.nome


class Experiencia(Grupo):

    class Meta:
        verbose_name_plural = "4 Experiência"

    def __str__(self):
        return self.titulo


class Card(Grupo, TimestampedModel):
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoExperiencia, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="card/foto/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "4.2 Card"

    def __str__(self):
        return f"{self.experiencia.titulo} - {self.grupo.nome} - {self.titulo}"


class Topico(Grupo):

    class Meta:
        verbose_name_plural = "5 Tópico"

    def __str__(self):
        return self.titulo


class SubTopico(SubGrupo, TimestampedModel):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "5.1 Subtópico"

    def __str__(self):
        return self.topico.titulo
