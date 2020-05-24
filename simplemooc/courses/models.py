from django.db import models

# Create your models here.
class CourseManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
		models.Q(name__icontains=query) | \
		models.Q(descrípition__icontains=query)
		)
class Course(models.Model):
		name = models.CharField('Nome', max_length=100)
		slug = models.SlugField('Atalho')
		descrípition = models.TextField('Descrição', blank=True)
		start_date = models.DateField(
			'Data de Início', null=True, blank=True
		)
		image = models.ImageField(null=True, blank=True)

		created_at = models.DateTimeField(
			'Criado em', auto_now_add=True
		)
		updated_at = models.DateTimeField('Atualizado em', auto_now=True)

		obj = CourseManager()

		def __str__(self):
			return (self.name)

		class Meta:

			verbose_name = 'Curso'
			verbose_name_plural = 'Cursos'
			ordering = ['id']
