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
	//Not the fastest... but it works for now :/
	$("input[name=issue]").change(function()
	{
		var myRadio = $(this);
		var checkedVal = myRadio.filter(':checked').val();
		var textarea = $("#elaboration");
		var a = textarea.attr('disabled');
		if (checkedVal == "other") //We've selected the 'other' option
		{
			//This call is not redundant, since we'll only ever enable the textarea if we're coming from another radio button (where it should have been disabled) 
			textarea.removeAttr('disabled'); 
		}
		else
		{
			textarea.attr('disabled', 'disabled'); //Often redundant, could be more efficient
		}
	});
});