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
});
