$('input[name^="egeDisc"]').each(function()
		{
			initSelect2($(this));
		});
$("#addExam").on("click", function()
		{
			if(egerows<maxExams)
			{
				egerows++;
				var newRow = $('<tr><td><input type="hidden" class="form-control" name="egeDisc"></td><td><input type="text" class="form-control" name="egePoints"></td><td><input type="text" class="form-control" name="egeYear"></td><td><button class="btn btn-default btn-sm" id="delExamRow" type="button">Удалить</button></td></tr>');
				$("#egeTableBody").append(newRow);
				initSelect2(newRow.find('input[name^="egeDisc"]'));
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