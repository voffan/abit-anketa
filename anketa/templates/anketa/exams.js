$('input[name^="egeDisc"]').each(function()
		{
			initSelect2($(this));
		});
$('input[name^="examType"]').each(function()
		{
			initSelect2_examType($(this));
		});
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
$("#addExam").on("click", function()
		{
			if(egerows<maxExams)
			{
				egerows++;
				var newRow = $('<tr><td><input type="hidden" class="form-control" name="egeDisc"></td><td><input type="hidden" class="form-control" name="examType"></td><td><input type="text" class="form-control" name="egePoints"></td><td><input type="text" class="form-control" name="egeYear"></td><td><button class="btn btn-default btn-sm" id="delExamRow" type="button">Удалить</button></td></tr>');
				$("#egeTableBody").append(newRow);
				initSelect2(newRow.find('input[name^="egeDisc"]'));
				initSelect2_examType(newRow.find('input[name^="examType"]'));
			}

		});
$(document).on("click","button[id*='delExamRow']", function()
		{
			if(egerows>1)
			{
				$(this).parent().parent().remove();
				egerows--;
			}
		});