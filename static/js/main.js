$(document).ready(function()
{
	var entityMap = 
	{
		"&": "&amp;",
		"<": "&lt;",
		">": "&gt;",
		'"': '&quot;',
		"'": '&#39;',
		"/": '&#x2F;'
	};

	function escapeHTML(string) 
	{
		return String(string).replace(/[&<>"'\/]/g, function (s) 
		{
			return entityMap[s];
		});
	}

	function mark_success(group, label)
	{
		group.addClass('success');
		label.html("Success");
		label.addClass('label-success');
	}

	function mark_warning(group, label, message)
	{
		group.addClass('warning');
		label.addClass('label-warning');
		label.html(message);
	}
	function mark_error(group, label, message)
	{
		group.addClass('error');
		label.addClass('label-important');
		label.html(message);
	}

	function isAlpha(str)
	{
		var patt = /^[a-zA-Z]+$/;
		return patt.test(str);
	}

	function isEmpty(str)
	{
		return str == null || str == "";
	}

	$("#submit_button").click(function()
	{
		alert("Hit the submit button!");
	});

	$("#first-name").blur(function()
	{
		var group = $("#first-name-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#first-name-label");
		//Reset classes to default
		label.removeClass(); 
		label.addClass('label');

		var text = escapeHTML($(this).val());
		if (isAlpha(text))
		{
			mark_success(group, label);
		}
		else if (isEmpty(text))
		{
			mark_warning(group, label, "You need to enter something!");			
		}
		else
		{
			mark_error(group, label, "Please change this input. I can't understand it.");
		}
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