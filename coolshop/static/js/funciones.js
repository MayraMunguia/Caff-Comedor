$(document).ready(function() {


var numeric = document.getElementById("the_form");
numeric.quantity.value = "1";


	$val= numeric.quantity.value;
	
	$('#numericcontrol a.plus').click(function(){
		$val++;
		numeric.quantity.value = $val;
	});
	$('#numericcontrol a.minus').click(function(){
		
		if($val>1)
		{
		$val--;	
		numeric.quantity.value = $val;
		}
		else
		{
			alert("La cantidad no puede ser menor a 0");
		}
	});

});