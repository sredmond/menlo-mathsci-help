$(document).ready(function()
{
	$("#submit_button").click(function()
	{
		alert("Hit the submit button!");
	});
	$("#first-name").blur(function()
	{
		var label = $("#test-label")
		$("#test-label").html("You blurred away from me! :(");
	});
});