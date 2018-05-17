$('input[name^="privcat"]').each(function()
		{
			initSelect2_Priv($(this));
		});
$('input[name^="privtype"]').each(function()
		{
			initSelect2_PrivType($(this));
		});
$('input[name^="achievement"]').each(function()
		{
			initSelect2_Achiev($(this));
		});
$('input[name^="achievresult"]').each(function()
		{
			initSelect2_AchievResult($(this));
		});
$('#privcat').select2({
		language:"ru",
		minimumInputLength: 1,
		ajax:{
			url:{% url 'preveduname' %},
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
$('#privtype').select2({
		language:"ru",
		minimumInputLength: 1,
		ajax:{
			url:{% url 'preveduname' %},
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
$('#achievement').select2({
		language:"ru",
		minimumInputLength: 1,
		ajax:{
			url:{% url 'preveduname' %},
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
$('#achievementDoc').select2({
		language:"ru",
		minimumInputLength: 1,
		ajax:{
			url:{% url 'preveduname' %},
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

function initSelect2_Priv(object){
		object.select2({
			language:"ru",
			allowClear:true,
			ajax:{
				url:{% url 'privcat' %},
				dataType:'json',
				delay:250,
				data:function(params){
					return{
						query:params
					};
				},
				processResults:function(data,page)
				{
					return{
						results:data
					};
				},
				cache:true
			}
		});
		if($(object).val() != "")
		{
            var v = $(object).val().split(";");
			object.select2('data',{id:v[0], text:v[1]});
		}
};
function initSelect2_PrivType(object){
		object.select2({
			language:"ru",
			allowClear:true,
			ajax:{
				url:{% url 'privtype' %},
				dataType:'json',
				delay:250,
				data:function(params){
					return{
						query:params
					};
				},
				processResults:function(data,page)
				{
					return{
						results:data
					};
				},
				cache:true
			}
		});
		if($(object).val() != "")
		{
            	var v = $(object).val().split(";");
				object.select2('data',{id:v[0], text:v[1]});
		}
};
function initSelect2_Achiev(object){
		object.select2({
			language:"ru",
			allowClear:true,
			ajax:{
				url:{% url 'achievement' %},
				dataType:'json',
				delay:250,
				data:function(params){
					return{
						query:params
					};
				},
				processResults:function(data,page)
				{
					return{
						results:data
					};
				},
				cache:true
			}
		});
		if($(object).val() != "")
		{
			var v = $(object).val().split(";");
			object.select2('data',{id:v[0], text:v[1]});
		}
};
function initSelect2_AchievResult(object){
		object.select2({
			language:"ru",
			allowClear:true,
			ajax:{
				url:{% url 'achievresult' %},
				dataType:'json',
				delay:250,
				data:function(params){
					return{
						query:params
					};
				},
				processResults:function(data,page)
				{
					return{
						results:data
					};
				},
				cache:true
			}
		});
		if($(object).val() != "")
		{
			var v = $(object).val().split(";");
			object.select2('data',{id:v[0], text:v[1]});
		}
};
$('input[type=radio][name=privileges]').change(function()
	{
		if (this.value == "yes")
		{
			$("#privcatrow").show();
			$("#privtyperow").show();
		}
		else
		{
			$("#privcatrow").hide();
			$("#privtyperow").hide();
		}
	});
$('input[type=radio][name=persach]').change(function()
	{
		if (this.value == "yes")
		{
			$("#achRow").show();
		}
		else
		{
			$("#achRow").hide();
		}
	});
$("#addPriv").on("click", function()
	{   if(privrows<maxPriv)
		{
		privrows++;
		    var newPanel = $('<div class="panel-body">\
		                    <div class="row">\
		                    <div class = "col-xs-6 col-sm-6 col-md-6">\
		                    <label for="privcat">Категория</label>\
							<input type="hidden" class="form-control" name="privcat" value =""><input type="hidden" name="privId" value ="-1">\
							</div>\
							<div class = "col-xs-6 col-sm-6 col-md-6">\
							<label for="privtype">Тип</label>\
							<input type="hidden" class="form-control" name="privtype" value="">\
							</div>\
							</div>\
							<br>\
							<div class="row">\
							<div class="col-xs-4 col-sm-4 col-md-4">\
							<label for="privdocSeria">Серия документа</label>\
							<input type="text" class="form-control" name="privdocSeria" value="">\
							</div>\
							<div class="col-xs-4 col-sm-4 col-md-4">\
							<label for="privdocNomer">Номер документа</label>\
							<input type="text" class="form-control" name="privdocNomer" value="">\
							</div>\
							<div class="col-xs-4 col-sm-4 col-md-4">\
							<label for="privdocData">Дата выдачи</label>\
							<input type="text" class="form-control" name="privdocData" value="">\
							</div>\
							<div class="col-xs-10">\
							<label for="privdocIssuer">Кем выдан</label>\
							<input type="text" class="form-control" name="privdocIssuer" value="">\
							</div>\
							<div class="col-xs-2">\
							<label for="addFile">Файл</label>\
							<button class="btn btn-primary btn-block" type="button" id="addFile">Обзор...</button>\
							</div>\
							</div>\
							<br>');
			//var newRow = $('<tr>\
			//              <td><input type="hidden" class="form-control" name="privcat"><input type="hidden" name="privId" value ="-1"></td>\
			//				<td><input type="hidden" class="form-control" name="privtype"></td>\
			//				<td><input type="text" class="form-control" name="privdocSeria"></td>\
			//				<td><input type="text" class="form-control" name="privdocNomer"></td>\
			//				<td><button class="btn btn-default btn-sm" name="delPrivRow" type="button">Удалить</button></td>\
			//  		    </tr>');
			//$("#privelegesTableBoby").append(newRow);
			$("#privilegesPanelBody").append(newPanel);
			initSelect2_Priv(newPanel.find('input[name^="privcat"]'));
			initSelect2_PrivType(newPanel.find('input[name^="privtype"]'));
		}
	});
$("#addAchiev").on("click", function()
	{   if(achievrows<maxAchiev)
		{
			achievrows++;
			var newRow = $('<tr>\
							<td><input type="hidden" class="form-control" name="achievement" value =""><input type="hidden" name="achievId" value ="-1"></td>\
							<td><input type="hidden" class="form-control" name="achievresult" value =""></td>\
							<td><input type="text" class="form-control" name="achievDoc" value=""></td>\
							<td><button class="btn btn-default btn-sm" name="delAchievRow" type="button">Удалить</button></td>\
							</tr>');
			$("#achievementsTableBoby").append(newRow);
			initSelect2_Achiev(newRow.find('input[name^="achievement"]'));
			initSelect2_AchievResult(newRow.find('input[name^="achievresult"]'));
		}
	});
$(document).on("click","button[name*='delPrivRow']", function()
	{
			if (parseInt($(this).attr('id')) >= 0)
			{
			    console.log($(this).attr('id'));
			    $.ajax({
			        url:{% url 'apiprivileges' %},
			        type:'POST',
			        data:{'id':$(this).attr('id'), 'csrfmiddlewaretoken': '{{ csrf_token }}', 'action':'delete' },
			        //headers: { "X-CSRFToken": getCookie("csrftoken") },
			        dataProcess:true,
					timeout:500,
					success:function(data)
					{
						if (parseInt(data['result'])==1)
						{
							$('#privelegesTableBoby').find('button[id = "'+data['id']+'"]').parent().parent().remove();
				            privrows--;
							$.notify("Удалено.", "success");

						}
						else
						{
							$.notify("Ошибка при удалении :(", "error");
						}
						console.log('Result is loaded!');
					},
					error:function()
					{
						$.notify("Отсутствует соединение :(", "error");
					},
			    });
			}else
			$(this).parent().parent().remove();
	});
$(document).on("click","button[name*='delAchievRow']", function()
	{
			if (parseInt($(this).attr('id')) >= 0)
			{
			    console.log($(this).attr('id'));
			    $.ajax({
			        url:{% url 'apiachievs' %},
			        type:'POST',
			        data:{'id':$(this).attr('id'), 'csrfmiddlewaretoken': '{{ csrf_token }}', 'action':'delete' },
			        //headers: { "X-CSRFToken": getCookie("csrftoken") },
			        dataProcess:true,
					timeout:500,
					success:function(data)
					{
						if (parseInt(data['result'])==1)
						{
							$('#achievementsTableBoby').find('button[id = "'+data['id']+'"]').parent().parent().remove();
				            achievrows--;
							$.notify("Удалено.", "success");

						}
						else
						{
							$.notify("Ошибка при удалении :(", "error");
						}
						console.log('Result is loaded!');
					},
					error:function()
					{
						$.notify("Отсутствует соединение :(", "error");
					},
			    });
			}else
			$(this).parent().parent().remove();
	});