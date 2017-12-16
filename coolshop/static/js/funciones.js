$(document).ready(function() {

$("button").click(function() {
    $("#Camb").toggle();
})

$("button").click(function() {
    $("#productos").css('visibility','visible');
})

 $('#numericcontrol input[type="text"]').val("1");
	$val=$('#numericcontrol input[type="text"]').val();
	$('#numericcontrol a.plus').click(function(){
		$val++;
		$(this).parent('div#numericcontrol').find('input[type="text"]').val($val);
	});
	$('#numericcontrol a.minus').click(function(){
		
		if($val>1)
		{
		$val--;	
		$(this).parent('div#numericcontrol').find('input[type="text"]').val($val);
		}
		else
		{
			alert("La cantidad no puede ser menor a 0");
		}
	});

});