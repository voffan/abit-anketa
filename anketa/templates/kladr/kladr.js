var saveObject;
var code = [];
var codetype = [];


function Kladr(object) {
	saveObject = object;
	if($(object).val().length < 1) {
		$('#region').select2('val', '');
		$('#district').select2('val', '');
		$('#city').select2('val', '');
		$('#village').select2('val', '');
		$('#street').select2('val', '');
		$('#city').select2('enable', true);
		$('#district').select2('enable', true);
		$('#KladrModal').modal();
		code = [];
		codetype = [];
	} if ($(object).val().length > 1) {
		$.ajax({
			url:"{% url 'kladr:get_objects_by_id' %}",
			method:"GET",
			data:{'id':$(object).val()},
			dataProcess:true,
			timeout:500,
			success:function(data){
				//console.log(data);
				console.log('success!');
				if (data[0]['success'] === '1') {
					console.log('should print');
					$('#city').select2('enable', true);
					$('#district').select2('enable', true);
					$('#region').select2('data', data[0]['data']['region']);
					if (data[0]['data']['district']['text'].length > 0){
						$('#district').select2('enable', true);
						$('#city').select2('enable', false);
						$('#district').select2('data', data[0]['data']['district']);
					}
					else $('#district').select2('val', '');
					if (data[0]['data']['city']['text'].length > 0) {
						$('#city').select2('enable', true);
						$('#district').select2('enable', false);
						$('#city').select2('data', data[0]['data']['city']);
					}
					else $('#city').select2('val', '');
					if (data[0]['data']['village']['text'].length > 0) {
                        $('#village').select2('data', data[0]['data']['village']);
                    }
					else {
                        $('#village').select2('val', '');
                    }
					$('#street').select2('data', data[0]['data']['street']);
					$('#KladrModal').modal();
				} else {
					alert(data[0][['error']]);
				}
			},
			error: function() {
				alert('error while getting data!');
			}
		});
	}
}


$('#region').select2({
	ajax:{
		url:"{% url 'kladr:get_region' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
			};
		},
		processResults: function (data, page) {
			// parse the results into the format expected by Select2.
			// since we are using custom formatting functions we do not need to
			// alter the remote JSON data
			return {
			  results: data
			};
		},
		cache: true
	},
	escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
	minimumInputLength: 1,
	language:"ru",
	placeholder:'Выберите республику, край, область...',
	allowClear:true
});


$('#district').select2({
	initSelection:function(e,callback){
		console.log(e);
		console.log(callback);
		callback({'id':'','text':''});
	},
	placeholder:'Выберите район',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_district' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				code: code[code.length - 1],
			};
		},
		processResults: function (data, page) {
			// parse the results into the format expected by Select2.
			// since we are using custom formatting functions we do not need to
			// alter the remote JSON data
			return {
			  results: data
			};
		},
		cache: true
	},
	escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
	minimumInputLength: 1,
	language:"ru"
});
$('#city').select2({
	initSelection:function(e, callback){
		console.log(e.val().text);
		console.log(callback);

		callback({'id':'','text':''});
	},
	placeholder:'Выберите город',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_city' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				code: code[code.length - 1],
			};
		},
		processResults: function (data, page) {
			// parse the results into the format expected by Select2.
			// since we are using custom formatting functions we do not need to
			// alter the remote JSON data
			return {
			  results: data
			};
		},
		cache: true
	},
	escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
	minimumInputLength: 1,
	language:"ru"
});
$('#village').select2({
	placeholder:'Выберите населенный пункт',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_village' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				code: code[code.length - 1],
			};
		},
		processResults: function (data, page) {
			// parse the results into the format expected by Select2.
			// since we are using custom formatting functions we do not need to
			// alter the remote JSON data
			return {
			  results: data
			};
		},
		cache: true
	},
	escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
	minimumInputLength: 1,
	language:"ru"
});
$('#street').select2({
	placeholder:'Выберите улицу',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_street' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				code: code[code.length - 1],
			};
		},
		processResults: function (data, page) {
			// parse the results into the format expected by Select2.
			// since we are using custom formatting functions we do not need to
			// alter the remote JSON data
			return {
			  results: data
			};
		},
		cache: true
	},
	escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
	minimumInputLength: 1,
	language:"ru"
});
$('#SaveKladr').on('click',function(e){
	if ($('#street').val() === "") {
		alert("Выберите улицу");
		return;
	}

	if ($('#adrshouse').val() === "") {
		alert("Введите номер дома");
		return;
	}

    $('adrsp').text = "fffff";
    var address = $('#region').select2('data').text;
    if ($('#district').select2('data')) {
        address += ", ";
        address += $('#district').select2('data').text;
    }
    if ($('#city').select2('data')) {
        address += ", ";
        address += $('#city').select2('data').text;
    }
    if ($('#village').select2('data')) {
        address += ", ";
        address += $('#village').select2('data').text;
    }
    if ($('#street').select2('data')) {
        address += ", ";
        address += $('#street').select2('data').text;
    }
    if ($('#adrshouse').val()) {
        address += ", ";
        address += $('#adrshouse').val();
    }
    if ($('#adrsbuilding').val()) {
        address += " корпус ";
        address += $('#adrsbuilding').val();
    }
    if ($('#adrsflat').val()) {
        address += ", кв. ";
        address += $('#adrsflat').val();
    }
	if (saveObject.selector === "#streetp") {
		$('#adrsp').val(address);
		$('#streetp').val(code[code.length - 1]);
		$('#housep').val($('#adrshouse').val());
		$('#buildingp').val($('#adrsbuilding').val());
		$('#flatp').val($('#adrsflat').val());
	} else {
    	$('#adrsf').val(address);
		$('#streetf').val(code[code.length - 1]);
		$('#housef').val($('#adrshouse').val());
		$('#buildingf').val($('#adrsbuilding').val());
		$('#flatf').val($('#adrsflat').val());
	}
	$('#KladrModal').modal('hide');
});
$('#region').on("change",function(e){
	$('#district').select2('val','');
	$('#city').select2('val','');
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("region") != -1) {
        code.splice(codetype.indexOf("region"), code.length - codetype.indexOf("region"));
        codetype.splice(codetype.indexOf("region"), codetype.length - codetype.indexOf("region"));
    }
    else if (codetype.indexOf("district") != -1) {
        code.splice(codetype.indexOf("district"), code.length - codetype.indexOf("district"));
        codetype.splice(codetype.indexOf("district"), codetype.length - codetype.indexOf("district"));
    }
	else if (codetype.indexOf("city") != -1) {
        code.splice(codetype.indexOf("city"), code.length - codetype.indexOf("city"));
        codetype.splice(codetype.indexOf("city"), codetype.length - codetype.indexOf("city"));
    }
	else if (codetype.indexOf("village") > -1) {
        code.splice(codetype.indexOf("village"), code.length - codetype.indexOf("village"));
        codetype.splice(codetype.indexOf("village"), codetype.length - codetype.indexOf("village"));
    }
	code.push($(this).select2('data').id);
	codetype.push("region");
});
$('#region').on("select2-removed",function(e){
	$('#district').select2('val','');
	$('#city').select2('val','');
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("region") != -1) {
        code.splice(codetype.indexOf("region"), code.length - codetype.indexOf("region"));
        codetype.splice(codetype.indexOf("region"), codetype.length - codetype.indexOf("region"));
    }
});
$('#district').on("change",function(e){
	$('#city').select2('val','');
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("district") != -1) {
        code.splice(codetype.indexOf("district"), code.length - codetype.indexOf("district"));
        codetype.splice(codetype.indexOf("district"), codetype.length - codetype.indexOf("district"));
    }
	else if (codetype.indexOf("city") != -1) {
        code.splice(codetype.indexOf("city"), code.length - codetype.indexOf("city"));
        codetype.splice(codetype.indexOf("city"), codetype.length - codetype.indexOf("city"));
    }
	else if (codetype.indexOf("village") > -1) {
        code.splice(codetype.indexOf("village"), code.length - codetype.indexOf("village"));
        codetype.splice(codetype.indexOf("village"), codetype.length - codetype.indexOf("village"));
    }
	code.push($(this).select2('data').id);
	codetype.push("district");
});
$('#district').on("select2-removed",function(e){
	$('#city').select2('val','');
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("district") != -1) {
        code.splice(codetype.indexOf("district"), code.length - codetype.indexOf("district"));
        codetype.splice(codetype.indexOf("district"), codetype.length - codetype.indexOf("district"));
    }
});
$('#city').on("change",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("city") != -1) {
        code.splice(codetype.indexOf("city"), code.length - codetype.indexOf("city"));
        codetype.splice(codetype.indexOf("city"), codetype.length - codetype.indexOf("city"));
    }
	else if (codetype.indexOf("village") > -1) {
        code.splice(codetype.indexOf("village"), code.length - codetype.indexOf("village"));
        codetype.splice(codetype.indexOf("village"), codetype.length - codetype.indexOf("village"));
    }
	code.push($(this).select2('data').id);
	codetype.push("city");
});
$('#city').on("select2-removed",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (codetype.indexOf("city") != -1) {
        code.splice(codetype.indexOf("city"), code.length - codetype.indexOf("city"));
        codetype.splice(codetype.indexOf("city"), codetype.length - codetype.indexOf("city"));
    }
});
$('#village').on("change",function(e){
	$('#street').select2('val','');
	if (codetype.indexOf("village") > -1) {
        code.splice(codetype.indexOf("village"), code.length - codetype.indexOf("village"));
        codetype.splice(codetype.indexOf("village"), codetype.length - codetype.indexOf("village"));
    }
	code.push($(this).select2('data').id);
	codetype.push("village");
});
$('#village').on("select2-removed",function(e){
	$('#street').select2('val','');
	if (codetype.indexOf("village") > -1) {
        code.splice(codetype.indexOf("village"), code.length - codetype.indexOf("village"));
        codetype.splice(codetype.indexOf("village"), codetype.length - codetype.indexOf("village"));
    }
});
$('#street').on("change",function(e){
	code.push($(this).select2('data').id);
	codetype.push("street");
});