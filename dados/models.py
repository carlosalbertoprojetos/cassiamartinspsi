import datetime
from django.db import models

from ckeditor.fields import RichTextField


class Endereco(models.Model):
    endereco = models.CharField(max_length=255)
    atual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.endereco

    def save(self, *args, **kwargs):
        # Se o campo 'atual' for marcado como True
        if self.atual:
            # Define 'atual=False' para os outros endereços
            Endereco.objects.filter(atual=True).exclude(id=self.id).update(atual=False)

        # Chama o método save() original para salvar o endereço
        super().save(*args, **kwargs)


class Email(models.Model):
    email = models.EmailField()
    atual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Se o campo 'atual' for marcado como True
        if self.atual:
            # Define 'atual=False' para os outros endereços
            Endereco.objects.filter(atual=True).exclude(id=self.id).update(atual=False)

        # Chama o método save() original para salvar o endereço
        super().save(*args, **kwargs)


class Telefone(models.Model):
    numero = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Telefones"

    def __str__(self):
        return self.numero


# https://acervolima.com/RichTextField-modelos-django/
class Grupo(models.Model):
    titulo = models.CharField(max_length=50)
    texto = RichTextField(blank=True, null=True)
    atual = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Se o campo 'atual' for marcado como True
        if self.atual:
            # Define 'atual=False' para os outros endereços
            IndicesAbordagem.objects.filter(atual=True).exclude(id=self.id).update(
                atual=False
            )

        # Chama o método save() original para salvar o endereço
        super().save(*args, **kwargs)


class SubGrupo(models.Model):
    sub_titulo = models.CharField(max_length=100)
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
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1.1 Redes Sociais"

    def __str__(self):
        return self.nome


class Home(models.Model):
    titulo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="home/foto/")
    letreiro = models.JSONField(blank=True, null=True)
    redes_sociais = models.ManyToManyField(RedeSocial)
    atual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1 HomePages"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Se o campo 'atual' for marcado como True
        if self.atual:
            # Define 'atual=False' para os outros endereços
            Home.objects.filter(atual=True).exclude(id=self.id).update(atual=False)

        # Chama o método save() original para salvar o endereço
        super().save(*args, **kwargs)


class Apresentacao(Grupo, SubGrupo):
    foto = models.ImageField(upload_to="apresentacao/foto/")

    class Meta:
        verbose_name_plural = "2 Apresentações"

    def __str__(self):
        return str(self.titulo)


class Abordagem(Grupo):

    class Meta:
        verbose_name_plural = "3 Abordagens"

    def __str__(self):
        return self.titulo


class IndicesAbordagem(TimestampedModel):
    abordagem = models.ForeignKey(Abordagem, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    atual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "3.1 Índices"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Se o campo 'atual' for marcado como True
        if self.atual:
            # Define 'atual=False' para os outros endereços
            IndicesAbordagem.objects.filter(atual=True).exclude(id=self.id).update(
                atual=False
            )

        # Chama o método save() original para salvar o endereço
        super().save(*args, **kwargs)


class TextosIndiceAbordagem(SubGrupo, TimestampedModel):
    indice = models.ForeignKey(IndicesAbordagem, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "3.2 Textos"

    def __str__(self):
        return self.indice.titulo


class GrupoExperiencia(models.Model):
    nome = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "4 A - Grupo Experiência"

    def __str__(self):
        return self.nome


class Experiencia(Grupo):

    class Meta:
        verbose_name_plural = "4 Experiências"

    def __str__(self):
        return self.titulo


class Card(Grupo, TimestampedModel):
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoExperiencia, on_delete=models.CASCADE)
    imagem = models.ImageField()

    class Meta:
        verbose_name_plural = "4.1 Cards"

    def __str__(self):
        return f"{self.experiencia.titulo} - {self.grupo.nome} - {self.titulo}"


class Topico(Grupo):

    class Meta:
        verbose_name_plural = "5 Tópicos"

    def __str__(self):
        return self.titulo


class SubTopico(SubGrupo, TimestampedModel):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "5.1 Subtópicos"

    def __str__(self):
        return self.topico.titulo
