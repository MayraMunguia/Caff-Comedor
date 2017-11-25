function cambiarDiv()
{
  document.getElementById('Camb').innerHTML = "{% for product in products %}<a href="{{ product.get_absolute_url }}">
		<img src="{% if product.image %}{{ product.image.url }}{% else %}{% static 'img/no_image.png' %}{% endif %}">
		</a>
		<a href="{{ product.get_absolute_url }}">{{ product.name }}</a><br>
		${{ product.price }}
	     {% endfor %}";
}