$(document).ready(function() {
	$("#sign_up").click(function() {
		//alert("yesss");
		$("#sign_up_form").css('display', 'block');
		$("#sign_in_form").css('display', 'none');
		$("#sign_up_toggle").css('display', 'none');
	});
	$("#sign_in").click(function() {
		$("#sign_in_form").css('display', 'block');
		$("#sign_up_form").css('display', 'none');
		$("#sign_in_toggle").css('display', 'none');
	});

	$('#checkout_btn').click(function() {
		$("#shipping_info_form").css('display', 'block');
	});
	$('.close').click(function() {
		$('#shipping_info_form').css('display', 'none');
	});

	/*$('#shipping_info_form').on('submit', function(event) {
		$.ajax({
			url : '/buy/checkout',
			data : {
				shipAdd : $('#shipAdd').val(),
				shipCity : $('#shipCity').val(),
				shipState : $('#shipState').val(),
				shipCountry : $('#shipCountry').val(),
				shipPhone : $('#shipPhone').val(),
				shipZip : $('#shipZip').val()
			},
			type : 'POST',
			success : function(response) {
				window.location.href = '/buy/checkout'
			},
			error : function() {
				$('#error_box').innerHTML = 'All fields are reuired'
			},
		})
		event.preventDefault()
		
	});*/

	$('#dropdown_btn').click(function() {
		/*$('.dropdown_link').css('display', 'inline-block')*/
		$('.dropdown_link').slideToggle()
	});
});
