var saveObject;
function Kladr(object){
	saveObject = object;
	if($(object).val().length < 1){
		$('#region').select2('val','');
		$('#district').select2('val','');
		$('#city').select2('val','');
		$('#village').select2('val','');
		$('#street').select2('val','');
		$('#city').select2('enable',true);
		$('#district').select2('enable',true);
		$('#KladrModal').modal();
	} if ($(object).val().length > 1){
		$.ajax({
			url:"{% url 'kladr:get_objects_by_id' %}",
			method:"GET",
			data:{'id':$(object).val()},
			dataProcess:true,
			timeout:500,
			success:function(data){
				//console.log(data);
				console.log('success!');
				if (data[0]['success']=='1'){
					console.log('should print');
					$('#city').select2('enable',true);
					$('#district').select2('enable',true);
					$('#region').select2('data',data[0]['data']['region']);
					if (data[0]['data']['district']['text'].length > 0){
						$('#district').select2('enable',true);
						$('#city').select2('enable',false);
						$('#district').select2('data',data[0]['data']['district']);
					}
					else $('#district').select2('val','');
					if (data[0]['data']['city']['text'].length > 0){
						$('#city').select2('enable',true);
						$('#district').select2('enable',false);
						$('#city').select2('data',data[0]['data']['city']);
					}
					else $('#city').select2('val','');
					if (data[0]['data']['village']['text'].length > 0) $('#village').select2('data',data[0]['data']['village']);
					else $('#village').select2('val','');
					$('#street').select2('data',data[0]['data']['street']);
					$('#KladrModal').modal();
				}else{
					alert(data[0][['error']]);
				}
			},
			error:function(){
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
	placeholder:'Выберете регион РФ',
	allowClear:true
});
$('#district').select2({
	initSelection:function(e,callback){
		console.log(e);
		console.log(callback);
		callback({'id':'','text':''});
	},
	placeholder:'Выберете район',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_district' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				region: $('#region').val(),
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
	placeholder:'Выберете город',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_city' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				region: $('#region').val(),
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
	placeholder:'Выберете населенный пункт',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_village' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			return{
				query: params, // search term
				district: $('#district').val(),
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
	placeholder:'Выберете улицу',
	allowClear:true,
	ajax:{
		url:"{% url 'kladr:get_street' %}",
		dataType: 'json',
		delay: 250,
		data:function(params){
			var obj;
			if ($('#village').val().length > 0){
				obj = $('#village').val();
			}else{
				obj = $('#city').val();
			}
			return{
				query: params, // search term
				village: obj,
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
    $('adrsp').text = "fffff";

	$(saveObject).val($('#street').val());
	$('#KladrModal').modal('hide');


});
$('#region').on("change",function(e){
	$('#district').select2('val','');
	$('#village').select2('val','');
	$('#street').select2('val','');
	$('#city').select2('enable',true);
});
$('#district').on("change",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (e.val.length > 0)$('#city').select2('enable',false);
});
$('#district').on("select2-removed",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	$('#city').select2("enable",true);
});
$('#city').on("change",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	if (e.val.length > 0)$('#district').select2('enable',false);
});
$('#city').on("select2-removed",function(e){
	$('#village').select2('val','');
	$('#street').select2('val','');
	$('#district').select2('enable',true);
});
$('#village').on("change",function(e){
	$('#street').select2('val','');
});