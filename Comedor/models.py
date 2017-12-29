from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	name= models.CharField(max_length=200, db_index = True)
	slug= models.SlugField(max_length=200,db_index=True, unique= True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	parent = models.ForeignKey('self',blank=True, null=True ,related_name='children')

	class Meta:
		unique_together = ('slug', 'parent',)
		ordering = ('name',)
		verbose_name = 'Category'
		verbose_name_plural= 'categories'


	def __str__	(self):
		full_path = [self.name]
		k = self.parent

		while k is not None:
			full_path.append(k.name)
			k = k.parent

		return ' -> '.join(full_path[::-1])

	def get_absolute_url(self):
		return reverse('VentaComedor:product_list_by_category', args=[self.slug])

			
class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', null = True, blank = True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)


	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('VentaComedor:product_detail', args=[self.id, self.slug])


