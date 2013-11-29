$(document).ready(function()
{
	//Enable tooltips on elements with rel="tooltip"  
	$(function () {
        $("[rel='tooltip']").tooltip();
    });

    //Enable popovers on elements with rel="popover"
    $(function () {
        $("[rel='popover']").popover();
    });

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

	/** 
	* Verify a LEARN request before it is sent to the server.
	* Possible Errors:
	* No class selected
	* 'Other' issue selected but nothing filled in
	* Nothing in the 'title' section
	* Nothing in the 'specific challenge' section
	*/
	$("#submit_learn_request").click(function()
	{
		//An array to hold all the error messages.
		var errors = new Array();

		//Get values
		var subj_title = escapeHTML($("#subj_title").val().trim());
		var issue_type = escapeHTML($("input[name=issue]").filter(':checked').val().trim());
		var elaboration = escapeHTML($("#elaboration").val().trim());
		var title_text = escapeHTML($("#title").val().trim());
		var challenge_text = escapeHTML($("#challenge").val().trim());
		
		if (isEmpty(subj_title))
		{
			errors.push("You must select a class in which you would like help.");
		}
		if (["hw","test","proj","other"].indexOf(issue_type) == -1)
		{
			errors.push("Please do not change the source code of the radio button values.");
		}
		if (issue_type == "other" && isEmpty(elaboration))
		{
			errors.push("You indicated an alternative type of challenge, yet failed to elaborate.");
		}
		if (isEmpty(title_text))
		{
			errors.push("You cannot have an empty title.");
		}
		if (isEmpty(challenge_text))
		{
			errors.push("You must say something in the speciic challenge field.");
		}
		//The moment of truth - are there errors?
		if (errors.length > 0)
		{
			var error_str = errors.join(" ");
			$("#alert").removeClass("hidden");
			$("#alert-text").html(error_str);
			$("html, body").animate({ scrollTop: 0 }, "slow"); //Scroll to the top
			return false;
		}
		//Otherwise, the form is sent to the server.
	});

	//Verify a request before it is sent to the server
	$("#submitRequest").submit(function()
	{
		//Kinda a ghetto way to inform people of what error they made. Add the error message to a string.
		var errors = new Array();

		//Get the values
		var first_name_text = escapeHTML($("#first-name").val().trim());
		var last_name_text = escapeHTML($("#last-name").val().trim());
		var grade_text = escapeHTML($("#grade").val().trim());
		var email_text = escapeHTML($("#email").val().trim());

		var num_classes_selected = $("option:selected").length;

		var title_text = escapeHTML($("#title").val().trim());
		var challenge_text = escapeHTML($("#challenge").val().trim());

		//Specialized error messages
		if (isEmpty(first_name_text))
		{
			errors.push("Your first name cannot be empty.");
		}
		else if (!isAlpha(first_name_text))
		{
			errors.push("Your first name must be composed of letters only.");
		}
		if (isEmpty(last_name_text))
		{
			errors.push("Your last name cannot be empty.");
		}
		else if (!isAlpha(last_name_text))
		{
			errors.push("Your last name must be composed of letters only.");
		}
		if (!(grade_text==='9' || grade_text==='10' || grade_text==='11' || grade_text==='12'))
		{
			errors.push("Your grade must be either '9', '10', '11', or '12'.");	
		}
		if (isEmpty(email_text))
		{
			errors.push("Your email cannot be empty");
		}
		else if (!isEmail(email_text))
		{
			errors.push("Your email must contain only letters, numbers, or any of '._+-'.");
		}
		if (num_classes_selected == 0)
		{
			errors.push("You must select at least one class.");
		}
		if (isEmpty(title_text))
		{
			errors.push("You must title the request.");
		}
		if (isEmpty(challenge_text))
		{
			errors.push("You must describe your specific challenge.");
		}

		//The moment of truth - are there errors?
		if (errors.length > 0)
		{
			var error_str = errors.join(" ");
			$("#alert").removeClass("hidden");
			$("#alert-text").html(error_str);
			$("html, body").animate({ scrollTop: 0 }, "slow"); //Scroll to the top
			return false;
		}
		//Otherwise, the form is sent to the server.
	});

	$(".btn-group button").click(function () 
	{
	    $("#subj_title").val($(this).text());
	});


//Some clientside form validation
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

		var text = escapeHTML($(this).val().trim());
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

		var text = escapeHTML($(this).val().trim());
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

		var text = escapeHTML($(this).val().trim());
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

		var text = escapeHTML($(this).val().trim());
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

	$("#title").blur(function()
	{
		var group = $("#title-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#title-label");
		//Reset classes to default
		label.removeClass(); 
		label.addClass('label');

		var text = escapeHTML($(this).val().trim());
		if (isEmpty(text))
		{
			mark_error(group, label, "You should title your requests!");			
		}
		else
		{
			mark_success(group, label);
		}
	});
	$("#challenge").blur(function()
	{
		var group = $("#challenge-control-group");
		//Reset classes to default
		group.removeClass();
		group.addClass('control-group');

		var label = $("#challenge-label");
		//Reset classes to default
		label.removeClass(); 
		label.addClass('label');

		var text = escapeHTML($(this).val().trim());
		if (isEmpty(text))
		{
			mark_error(group, label, "Please tell us about your challenge!");			
		}
		else
		{
			mark_success(group, label);
		}
	});

	//Enables the textarea if a user toggles to the 'other' radio button, and disables it if a user toggles to some other radio button
	//Not the fastest... but it works for now :/
	$("input[name=issue]").change(function()
	{
		var myRadio = $(this);
		var checkedVal = myRadio.filter(':checked').val().trim();
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