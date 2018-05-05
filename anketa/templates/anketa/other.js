		$('input[type=radio][name=liableForMilit]').change(function()
		{
			if (this.value == "yes")
			{
				$("#isServedRow").show();
			}
			else
			{
				$("#isServedRow").hide();
			}
		});
		$('input[type=radio][name=isServed]').change(function()
		{
			if (this.value == "yes")
			{
				$("#armyRow").show();
			}
			else
			{
				$("#armyRow").hide();
			}
		});
	$('#rank').select2({
		allowClear:true,
		placeholder: "Рядовой",
		language:"ru",
		ajax:{
			url:{% url 'rank' %},
			dataType: 'json',
			delay: 250,
			data:function(params){
				return{
					query: params
				};
			},
			processResults: function (data, page) {
				return {
					results: data
				};
			},
			cache: true
		}
	});
	$('#flang').select2({
		language:"ru",
		ajax:{
			url:{% url 'flang' %},
			dataType: 'json',
			delay: 250,
			data:function(params){
				return{
					query: params
				};
			},
			processResults: function (data, page) {
				return {
					results: data
				};
			},
			cache: true
		}
	});