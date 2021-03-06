$('input[name^="egeDisc"]').each(function()
		{
			initSelect2($(this));
		});
$('input[name^="addDisc"]').each(function()
		{
			initSelect2($(this));
		});
$('input[name^="examType"]').each(function()
		{
			initSelect2_examType($(this));
		});
function initSelect2(object){
		object.select2({
			language:"ru",
			allowClear:true,
			ajax:{
				url:{% url 'examsubject' %},
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
			for (var i = 0; i<sub_id.length;i++)
			{
				if(sub_id[i]===parseInt($(object).val()))
				{
					object.select2('data',{id:sub_id[i], text:sub_val[i]});
					return;
				}
			}
		}
};
function initSelect2_examType(object){
			object.select2({
				language:"ru",
				allowClear:true,
				ajax:{
					url:{% url 'examtype' %},
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

$(document).on('change', 'input[name^=egePoints]', function(){
    if (parseInt($(this).val())>100){
        alert("Вы не можете установить кол-во баллов больше 100!");
        $(this).val(0);
    }
    if (parseInt($(this).val())<0){
        alert("Вы не можете установить кол-во баллов меньше 0!");
        $(this).val(0);
    }
});

$(document).on('change', 'input[name^=egeYear]', function(){
    var dyear = new Date();
    var year = parseInt(dyear.getFullYear());
    if (parseInt($(this).val())>year){
        alert("Вы не можете указать год позже "+year+"!");
        $(this).val(2018);
    }
    year = year -4;
    if (parseInt($(this).val())<year){
        alert("Вы не можете установить год раньше "+year+"!");
        $(this).val(2014);
    }
});

$("#addExam").on("click", function()
		{
			if(egerows<maxExams)
			{
				egerows++;
				var newRow = $('<tr>\
				                <td><input type="hidden" class="form-control" name="egeDisc"><input type="hidden" name="examId" value ="-1"></td>\
				                <td><input type="hidden" class="form-control" name="examType"></td>\
				                <td><input type="text" class="form-control" name="egePoints"></td>\
				                <td><input type="text" class="form-control" name="egeYear"></td>\
				                <td><button class="btn btn-default btn-sm" name="delExamRow" type="button" id="-1">Удалить</button></td>\
				                </tr>');
				$("#egeTableBody").append(newRow);
				initSelect2(newRow.find('input[name^="egeDisc"]'));
				initSelect2_examType(newRow.find('input[name^="examType"]'));
			}

		});
$("#addExam2").on("click", function()
		{
			if(addrows<maxAddExams)
			{
				addrows++;
				var newRow = $('<tr class="info">\
								<td><input type="hidden" class="form-control" name="addDisc"><input type="hidden" name="examId" value ="-1"></td>\
								<td><input type="text" class="form-control" name="addPoints" readonly></td>\
								<td><input type="text" class="form-control" name="addYear" readonly></td>\
								<td><button class="btn btn-default btn-sm" name="delExamRow2" type="button" id="-1">Удалить</button></td>\
								</tr>');
				$("#egeTableBodyAdd").append(newRow);
				initSelect2(newRow.find('input[name^="addDisc"]'));
			}

		});
$(document).on("click","button[name*='delExamRow']", function()
		{
		    /*console.log($(this).attr('id'));
		    console.log($(this));*/
			if ((egerows>1) && (parseInt($(this).attr('id')) >= 0))
			{
			    $.ajax({
			        url:{% url 'apiexams' %},
			        type:'POST',
			        data:{'id':$(this).attr('id'), 'csrfmiddlewaretoken': '{{ csrf_token }}', 'action':'delete' },
			        //headers: { "X-CSRFToken": getCookie("csrftoken") },
			        dataProcess:true,
					timeout:500,
					success:function(data)
					{
						if (parseInt(data['result'])==1)
						{
							$('#egeTableBody').find('button[id = "'+data['id']+'"]').parent().parent().remove();
				            egerows--;
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
			{
				$(this).parent().parent().remove();
				egerows--;
			}
		});
$(document).on("click","button[name*='delExamRow2']", function()
		{
			if ((addrows>1) && (parseInt($(this).attr('id')) >= 0))
			{
			    $.ajax({
			        url:{% url 'apiexams' %},
			        type:'POST',
			        data:{'id':$(this).attr('id'), 'csrfmiddlewaretoken': '{{ csrf_token }}', 'action':'delete' },
			        //headers: { "X-CSRFToken": getCookie("csrftoken") },
			        dataProcess:true,
					timeout:500,
					success:function(data)
					{
						if (parseInt(data['result'])==1)
						{
							$('#egeTableBodyAdd').find('button[id = "'+data['id']+'"]').parent().parent().remove();
				            addrows--;
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
			{
				$(this).parent().parent().remove();
				addrows--;
			}
		});
