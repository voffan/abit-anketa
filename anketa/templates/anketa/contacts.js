$('#kladrbtn').on('click', function(e){
			//$('#KladrModal').modal();
			Kladr($('#street'));
		});
$(document).on("click","button[id*='delContactRow']", function()
		{
			if(contactsrow>1)
			{
				$(this).parent().parent().remove();
				contactsrow--;
			}
		});
$("#addContact").on("click", function()
{
	if(contactsrow<maxContacts)
	{
		contactsrow++;
		var newRow = $('<tr class="info"><td><select id="contacttype" name = "contacttype" class="form-control">{% if contacts_type %}{% for item in contacts_type %}<option value="{{item.id}}">{{item.value}}</option>{% endfor %}{% endif %}</select></td><td><input type="text" class="form-control" name="contactvalue"></td><td><button class="btn btn-default btn-sm" id="delContactRow" type="button">Удалить</button></td></tr>');
		$("#contactsTable").append(newRow);
	}
});