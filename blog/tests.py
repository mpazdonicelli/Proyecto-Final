from django.test import TestCase

# Create your tests here.
from django.db import IntegrityError
from blog.models import Reseña


class ReseñaTests(TestCase):
    """En esta clase van todas las pruebas del modelo Reseña."""

    def test_creacion_reseña(self):
        # caso uso esperado
        reseña = Reseña(titulo="Título", subtitulo="Subtítulo", cuerpo="Cuerpo", autor="Autor", fecha=2023-5-5)
        reseña.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Reseña.objects.count(), 1)
        self.assertEqual(reseña.titulo, "Título")
        self.assertEqual(reseña.subtitulo, "Subtítulo")
        self.assertEqual(reseña.cuerpo, "Cuerpo")
        self.assertEqual(reseña.autor, "Autor")
        self.assertEqual(reseña.fecha, 2023-5-5)

    def test_reseña_str(self):
        reseña = Reseña(titulo="Título")
        reseña.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(reseña.__str__(), "Título")
