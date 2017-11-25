$(document).ready(function() {


$("Cambiar").click(function(){
    $("Camb").html("{% for product in products %}
	<div class="item">
		<a href="{{ product.get_absolute_url }}">
		<img src="{% if product.image %}{{ product.image.url }}{% else %}{% static 'img/no_image.png' %}{% endif %}">
		</a>
		<a href="{{ product.get_absolute_url }}">{{ product.name }}</a><br>
		${{ product.price }}
	</div>
{% endfor %}");
});

});