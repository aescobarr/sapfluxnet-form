jQuery( document ).ready(function( $ ) {
	if ($("#metadata_file").text() != ''){
	    $("#metadata_file input[type='file']").css('color','transparent');
	}
	if ($("#sapflow_file").text() != ''){
	    $("#sapflow_file input[type='file']").css('color','transparent');
	}
	if ($("#envdata_file").text() != ''){
	    $("#envdata_file input[type='file']").css('color','transparent');
	}

	if($('#id_envdata_included').is(":checked")){
        $("#id_envdata_file").prop('disabled', true);
        var control = $("#id_envdata_file");
        control.replaceWith( control.val('').clone( true ) );
	}

	if($('#id_sapflow_included').is(":checked")) {
        $("#id_sapflow_file").prop('disabled', true);
        var control = $("#id_sapflow_file");
        control.replaceWith( control.val('').clone( true ) );
    }

    $('#id_envdata_included').change(function() {
        if($(this).is(":checked")) {
            $("#id_envdata_file").prop('disabled', true);
            var control = $("#id_envdata_file");
            control.replaceWith( control.val('').clone( true ) );
        }else{
            $("#id_envdata_file").prop('disabled', false);
        }
    });

    $('#id_sapflow_included').change(function() {
        if($(this).is(":checked")) {
            $("#id_sapflow_file").prop('disabled', true);
            var control = $("#id_sapflow_file");
            control.replaceWith( control.val('').clone( true ) );
        }else{
            $("#id_sapflow_file").prop('disabled', false);
        }
    });
});