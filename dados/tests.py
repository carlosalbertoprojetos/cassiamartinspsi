from django.test import TestCase
from .models import (
    Endereco,
    Email,
    Telefone,
    RedeSocial,
    Home,
    Apresentacao,
    Abordagem,
    IndicesAbordagem,
    TextosIndiceAbordagem,
    GrupoExperiencia,
    Experiencia,
    Card,
    Topico,
    SubTopico,
)


class AtualizadorModelTests(TestCase):
    def test_atualizador_model_single_instance(self):
        """Testa se apenas uma instância permanece com `atual=True`"""
        endereco1 = Endereco.objects.create(endereco="Rua 1")
        endereco2 = Endereco.objects.create(endereco="Rua 2", atual=False)

        # Atualiza `atual` no segundo endereço
        endereco2.atual = True
        endereco2.save()

        # Recarrega os objetos do banco
        endereco1.refresh_from_db()
        endereco2.refresh_from_db()

        # Verifica que apenas o segundo endereço está com `atual=True`
        self.assertFalse(endereco1.atual)
        self.assertTrue(endereco2.atual)

    def test_email_unique_atual(self):
        """Verifica que apenas um email pode ser marcado como atual"""
        email1 = Email.objects.create(email="teste1@exemplo.com")
        email2 = Email.objects.create(email="teste2@exemplo.com", atual=False)

        email2.atual = True
        email2.save()

        email1.refresh_from_db()
        email2.refresh_from_db()

        self.assertFalse(email1.atual)
        self.assertTrue(email2.atual)


class TelefoneTests(TestCase):
    def test_criacao_telefone(self):
        """Verifica a criação de instâncias de telefone"""
        telefone = Telefone.objects.create(numero="(11) 99999-9999")
        self.assertEqual(str(telefone), "(11) 99999-9999")


class RedeSocialTests(TestCase):
    def test_criacao_rede_social(self):
        """Verifica a criação de instâncias de rede social"""
        rede_social = RedeSocial.objects.create(
            nome="Facebook", icone="facebook-icon", link="https://facebook.com"
        )
        self.assertEqual(str(rede_social), "Facebook")
        self.assertTrue(rede_social.ativo)


class HomeTests(TestCase):
    def setUp(self):
        self.rede_social = RedeSocial.objects.create(
            nome="Twitter", icone="twitter-icon", link="https://twitter.com"
        )

    def test_home_criacao(self):
        """Verifica a criação de uma instância de Home"""
        home = Home.objects.create(titulo="Página Inicial")
        home.redes_sociais.add(self.rede_social)

        self.assertEqual(str(home), "Página Inicial")
        self.assertIn(self.rede_social, home.redes_sociais.all())

    def test_home_atualizador(self):
        """Testa a lógica de `AtualizadorModel` em Home"""
        home1 = Home.objects.create(titulo="Página 1")
        home2 = Home.objects.create(titulo="Página 2", atual=False)

        home2.atual = True
        home2.save()

        home1.refresh_from_db()
        home2.refresh_from_db()

        self.assertFalse(home1.atual)
        self.assertTrue(home2.atual)


class ApresentacaoTests(TestCase):
    def test_criacao_apresentacao(self):
        """Testa a criação de uma instância de Apresentacao"""
        apresentacao = Apresentacao.objects.create(titulo="Título Apresentação")
        self.assertEqual(str(apresentacao), "Título Apresentação")
        self.assertFalse(bool(apresentacao.foto))

    def test_heranca_grupo_subgrupo(self):
        """Testa se Apresentacao herda corretamente de Grupo e SubGrupo"""
        apresentacao = Apresentacao.objects.create(
            titulo="Título Apresentação", sub_titulo="Subtítulo"
        )
        self.assertEqual(apresentacao.titulo, "Título Apresentação")
        self.assertEqual(apresentacao.sub_titulo, "Subtítulo")


class AbordagemTests(TestCase):
    def test_criacao_abordagem(self):
        """Testa a criação de uma instância de Abordagem"""
        abordagem = Abordagem.objects.create(titulo="Título Abordagem")
        self.assertEqual(str(abordagem), "Título Abordagem")


class IndicesAbordagemTests(TestCase):
    def setUp(self):
        self.abordagem = Abordagem.objects.create(titulo="Título Abordagem")

    def test_criacao_indices_abordagem(self):
        """Testa a criação de uma instância de IndicesAbordagem"""
        indice = IndicesAbordagem.objects.create(
            abordagem=self.abordagem, titulo="Título Índice"
        )
        self.assertEqual(str(indice), "Título Índice")
        self.assertEqual(indice.abordagem, self.abordagem)


class TextosIndiceAbordagemTests(TestCase):
def setUp(self):
    self.abordagem = Abordagem.objects.create(titulo="Título Abordagem")
    self.indice = IndicesAbordagem.objects.create(
        abordagem=self.abordagem, titulo="Título Índice"
    )

def test_criacao_textos_indice_abordagem(self):
    """Testa a criação de uma instância de TextosIndiceAbordagem"""
    texto = TextosIndiceAbordagem.objects.create(
        indice=self.indice, sub_titulo="Subtítulo Texto", exibindo=True
    )
    self.assertEqual(str(texto), "Título Índice")
    self.assertEqual(texto.indice, self.indice)
    self.assertEqual(texto.sub_titulo, "Subtítulo Texto")
    self.assertTrue(texto.exibindo)


class GrupoExperienciaTests(TestCase):
    def test_criacao_grupo_experiencia(self):
        """Testa a criação de uma instância de GrupoExperiencia"""
        grupo = GrupoExperiencia.objects.create(nome="Grupo 1")
        self.assertEqual(str(grupo), "Grupo 1")


class ExperienciaTests(TestCase):
    def test_criacao_experiencia(self):
        """Testa a criação de uma instância de Experiencia"""
        experiencia = Experiencia.objects.create(titulo="Experiência 1")
        self.assertEqual(str(experiencia), "Experiência 1")


class CardTests(TestCase):
    def setUp(self):
        self.grupo = GrupoExperiencia.objects.create(nome="Grupo 1")
        self.experiencia = Experiencia.objects.create(titulo="Experiência 1")

    def test_criacao_card(self):
        """Testa a criação de uma instância de Card"""
        card = Card.objects.create(
            experiencia=self.experiencia, grupo=self.grupo, titulo="Título Card"
        )
        self.assertEqual(str(card), "Experiência 1 - Grupo 1 - Título Card")
        self.assertEqual(card.experiencia, self.experiencia)
        self.assertEqual(card.grupo, self.grupo)
        self.assertFalse(bool(card.imagem))  # Verifica que não há imagem associada


class TopicoTests(TestCase):
    def test_criacao_topico(self):
        """Testa a criação de uma instância de Topico"""
        topico = Topico.objects.create(titulo="Título Tópico")
        self.assertEqual(str(topico), "Título Tópico")


class SubTopicoTests(TestCase):
    def setUp(self):
        self.topico = Topico.objects.create(titulo="Título Tópico")

    def test_criacao_subtopico(self):
        """Testa a criação de uma instância de SubTopico"""
        subtopico = SubTopico.objects.create(
            topico=self.topico, sub_titulo="Subtítulo SubTópico", exibindo=True
        )
        self.assertEqual(str(subtopico), "Título Tópico")
        self.assertEqual(subtopico.topico, self.topico)
        self.assertEqual(subtopico.sub_titulo, "Subtítulo SubTópico")
        self.assertTrue(subtopico.exibindo)
