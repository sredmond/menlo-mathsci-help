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

	function isEmail(str)
	{
		var patt = /^[a-zA-Z0-9._%+-]+$/;
		return patt.test(str);
	}

	$("#submit_button").click(function()
	{
		//Do something here
	});

//Some form validation
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

	$("#last-name").blur(function()
	{
		var group = $("#last-name-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#last-name-label");
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

	$("#grade").blur(function()
	{
		var group = $("#grade-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#grade-label");
		//Reset classes to default
		label.removeClass(); 
		label.addClass('label');

		var text = escapeHTML($(this).val());
		if (text === '9' || text === '10' || text === '11' || text === '12')
		{
			mark_success(group, label);
		}
		else
		{
			mark_error(group, label, "Grade must be either 9, 10, 11, or 12");
		}
	});

	$("#email").blur(function()
	{
		var group = $("#email-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#email-label");
		//Reset classes to default
		label.removeClass(); 
		label.addClass('label');

		var text = escapeHTML($(this).val());
		if (isEmail(text))
		{
			mark_success(group, label);
		}
		else if (isEmpty(text))
		{
			mark_warning(group, label, "You need to enter something!");			
		}
		else
		{
			mark_error(group, label, "I don't think that is a valid email address. Please change it.");
		}
	});

	//Enables the textarea if a user toggles to the 'other' radio button, and disables it if a user toggles to some other radio button
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