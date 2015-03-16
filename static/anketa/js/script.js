  $(function(){
    $(document).ready(function(){
      $('#id_id_doc').parent().parent().before('<tr><th colspan="2">Документ удостоверяющий личность:</th></tr>');
      $('#id_prev_edu_level').parent().parent().before('<tr><th colspan="2">Предыдущее образование:</th></tr>');
      //$('#id_prev_edu_organisation_name').parent().parent().after('<tr><th colspan="2"><button type="button" id="prev_edu_org" class="prev_edu_org" onclick="prev_edu_organisation_show()">Моего учебного заведения нет в списке</button></td></tr>');
      //$('#id_prev_edu_organisation_name').parent().parent().css('display', 'none');
      $('#id_prev_edu_organisation').parent().parent().css('display', 'none');
      $('#id_prev_edu_doc_type').parent().parent().before('<tr><th colspan="2">Документ об образовании:</th></tr>');
      $('#id_hotel').parent().parent().before('<tr><th colspan="2">Общие сведения:</th></tr>');
      $('input[name$="adm_territory_name"]').parent().parent().css('display', 'none');
      $('input[name$="adm_unit_name"]').parent().parent().css('display', 'none');
      $('input[name$="settlement_name"]').parent().parent().css('display', 'none');
      $('#id_milit-0-served').parent().parent().css('display', 'none');
      $('#id_milit-0-year').parent().parent().css('display', 'none');
      $('#id_milit-0-rank').parent().parent().css('display', 'none');
      $("#id_is_mil_service").trigger('change');
      $("#id_milit-0-served").trigger('change');
      $('select[id $= "id_settlement"]').each(function() {
        if ($('#' + this.id + ' option:selected').text() != '---------') {
          $(this).trigger('change');
        }
        else {
          if ($('#' + this.id.replace("id_settlement", "id_adm_unit") + ' option:selected').text() != '---------') {
            $('#' + this.id.replace("id_settlement", "id_adm_unit")).trigger('change');
          }
          else {
            $('#' + this.id.replace("id_settlement", "id_adm_territory")).trigger('change');
          }
        }
      });
      $('select[id $= "id_spec"]').each(function() {
        if ($('#' + this.id + ' option:selected').text() != '---------') {
          $(this).trigger('change');
        }
        else {
          $('#' + this.id.replace("id_spec", "id_specialn")).trigger('change');
        }
      });
      $('.error input').css('border', '1px solid red');
      $('.error select').css('border', '1px solid red');
    })
  })
  $(function(){
    $('select[id $= "id_adm_territory"]').change(function(){
      var attr = this.id;
      if ($('#' + attr + ' option:selected').text() != 'Республика Саха (Якутия)' && $('#' + attr + ' option:selected').text() != '---------') {
          $.getJSON("/abit-anketa/ajax/categ/",{id:0,type:"Муниципальный район"}, function(j) {
          var options = '<option value="">---------</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
          }
          var name = attr.replace("id_adm_territory", "id_adm_unit");
          $("#" + name).html(options);
          $("#" + name + " option:first").attr('selected', 'selected');
          $("#" + name).attr('disabled', false);
        })
        $("#" + attr).attr('selected', 'selected');
        $.getJSON("/abit-anketa/ajax/categ/",{id:0,type:"Населённый пункт"}, function(j) {
          var options = '<option value="">---------</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
          }
          var name = attr.replace("id_adm_territory", "id_settlement");
          $("#" + name).html(options);
          $("#" + name + " option:first").attr('selected', 'selected');
          $("#" + name).attr('disabled', false);
        })
        var name = attr.replace("id_adm_territory", "id_adm_unit");
        $('select[id = "' + name + '"]').parent().parent().css('display', 'none');
        name = name.replace("id_adm_unit", "adm_unit_name");
        $('input[id = "' + name + '"]').parent().parent().css('display', 'table-row');
        name = name.replace("adm_unit_name", "id_settlement");
        $('select[id = "' + name + '"]').parent().parent().css('display', 'none');
        name = name.replace("id_settlement", "settlement_name");
        $('input[id = "' + name + '"]').parent().parent().css('display', 'table-row');
      }
      else {
        $.getJSON("/abit-anketa/ajax/categ/",{id:+$(this).val(),type:"Муниципальный район"}, function(j) {
          var options = '<option value="">---------</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
          }
          var name = attr.replace("id_adm_territory", "id_adm_unit");
          $("#" + name).html(options);
          $("#" + name + " option:first").attr('selected', 'selected');
          $("#" + name).attr('disabled', false);
        })
        $("#" + attr).attr('selected', 'selected');
        $.getJSON("/abit-anketa/ajax/categ/",{id:+$(this).val(),type:"Населённый пункт"}, function(j) {
          var options = '<option value="">---------</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
          }
          var name = attr.replace("id_adm_territory", "id_settlement");
          $("#" + name).html(options);
          $("#" + name + " option:first").attr('selected', 'selected');
          $("#" + name).attr('disabled', false);
        })
        $("#" + attr).attr('selected', 'selected');
        var name = attr.replace("id_adm_territory", "id_adm_unit");
        $('select[id = "' + name + '"]').parent().parent().css('display', 'table-row');
        name = name.replace("id_adm_unit", "adm_unit_name");
        $('input[id = "' + name + '"]').parent().parent().css('display', 'none');
        $('#' + name).val('');
        name = name.replace("adm_unit_name", "id_settlement");
        $('select[id = "' + name + '"]').parent().parent().css('display', 'table-row');
        name = name.replace("id_settlement", "settlement_name");
        $('input[id = "' + name + '"]').parent().parent().css('display', 'none');
        $('#' + name).val('');
      }
    })
  })
  $(function(){
    $('select[id $= "id_adm_unit"]').change(function(){
      var attr = this.id;
      $.getJSON("/abit-anketa/ajax/categ/",{pid:+$("select#id_address-0-id_adm_territory").val(),id:+$(this).val(),type:"Населённый пункт"}, function(j) {
        var options = '<option value="">---------</option>';
        for (var i = 0; i < j.length; i++) {
          options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
        }
        var name = attr.replace("id_adm_unit", "id_settlement");
        $("#" + name).html(options);
        $("#" + name + " option:first").attr('selected', 'selected');
        $("#" + name).attr('disabled', false);
      })
      $("#" + attr).attr('selected', 'selected');
    })
  })
  $(function(){
    $('select[id $= "id_institute"]').change(function(){
      var attr = this.id;
      $.getJSON("/abit-anketa/ajax/categ/",{id:+$(this).val(),type:"Специальность"}, function(j) {
        var options = '<option value="">---------</option>';
        for (var i = 0; i < j.length; i++) {
          options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
        }
        var name = attr.replace("id_institute", "id_specialn");
        $("#" + name).html(options);
        $("#" + name + " option:first").attr('selected', 'selected');
        $("#" + name).attr('disabled', false);
      })
      $("#" + attr).attr('selected', 'selected');
    })
  })
  $(function(){
    $('select[id $= "id_specialn"]').change(function(){
      var attr = this.id;
      $.getJSON("/abit-anketa/ajax/categ/",{id:+$(this).val(),type:"Специализация"}, function(j) {
        if (1 != j.length) {
          var options = '<option value="">---------</option>';
        }
        for (var i = 0; i < j.length; i++) {
          options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
        }
        var name = attr.replace("id_specialn", "id_spec");
        $("#" + name).html(options);
        $("#" + name + " option:first").attr('selected', 'selected');
        $("#" + name).attr('disabled', false);
        if (1 == j.length)
        {
            $("#" + name).css('border', '1px solid darkgray');
        }
      })
      $("#" + attr).attr('selected', 'selected');
    })
  })
  $(function(){
    $("button.application").click(function(){
      var type = this.id;
      var newElement = $('div.' + type + ':last').clone(true);
      var total = parseInt($('#id_' + type + '-TOTAL_FORMS').val());
      var max = parseInt($('#id_' + type + '-MAX_NUM_FORMS').val());
      if (total <= max) {
        newElement.find(':input').each(function() {
          if ($(this).is(':button')) {
          }
          else
          {
            var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
            $(this).css('border', '1px solid darkgray');
          }
        });
        newElement.find('label').each(function() {
          var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
          $(this).attr('for', newFor);
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $('div.' + type + ':last').after(newElement);
        $('div.' + type + ':last').css('display', 'block');
        $('#id_application-' + (total - 1) + '-id_spec').children().remove();
        $('#id_application-' + (total - 1) + '-id_spec').html('<option value="">---------</option>');
        $('#id_application-' + (total - 1) + '-id_spec option:first').attr('selected', 'selected');
        $('#id_application-' + (total - 1) + '-id_spec').attr('disabled', false);
        if (total == max) {
          $(this).parent().parent().parent().parent().css('display', 'none');
        }
      }
    })
  })
  $(function(){
    $("button.exam").click(function(){
      var type = this.id;
      var newElement = $(this).parent().parent().parent().parent().find('.' + type).last().clone(true);
      var total = parseInt($('#id_' + type + '-TOTAL_FORMS').val());
      var max = parseInt($('#id_' + type + '-MAX_NUM_FORMS').val());
      if (total <= max) {
        newElement.find(':input').each(function() {
          if ($(this).is(':button')) {
          }
          else
          {
            var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
            $(this).css('border', '1px solid darkgray');
          }
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(this).parent().parent().parent().parent().find('.' + type).last().after(newElement);
        $(this).parent().parent().parent().parent().find('.' + type).last().css('display', 'table-row');
      }
    })
  })
  $(function(){
    $("button.delete").click(function(){
      $(this).parent().parent().css('display', 'none');
      $(this).parent().parent().find(':input').each(function() {
        if ($(this).is(':button')) {
        }
        else
        {
          $(this).val('');
        }
      });
    })
  })
  $(function(){
    $("button.del").click(function(){
      $(this).parent().parent().parent().parent().parent().css('display', 'none');
      var type = 'application';
      var total = parseInt($('#id_' + type + '-TOTAL_FORMS').val());
      var max = parseInt($('#id_' + type + '-MAX_NUM_FORMS').val());
      total--;
      $('#id_' + type + '-TOTAL_FORMS').val(total);
      $(this).parent().parent().parent().parent().find(':input').each(function() {
        if ($(this).is(':button')) {
        }
        else
        {
          $(this).val('');
        }
      });
      if (total < max) {
        $('button#application').parent().parent().parent().parent().css('display', 'table');
      }
    })
  })
  $(function(){
    $("#id_is_coincides").change(function() {
      var type = 'address';
      var total = parseInt($('#id_' + type + '-TOTAL_FORMS').val());
      if('false' == $(this).val()) {
        var newElement = $('.address').last().clone(true);
        newElement.find(':input').each(function() {
          var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
          var id = 'id_' + name;
          $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
          $(this).css('border', '1px solid darkgray');
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(this).parent().parent().parent().parent().after(newElement);
      }
      else if (total == 2) {
        $('.address').last().remove();
        total--;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
      }
    })
  })
  $(function(){
    $("#id_is_mil_service").change(function() {
      if ($('#' + this.id + ' option:selected').text() == 'военнообязанный') {
        $('#id_milit-0-served').parent().parent().css('display', 'table-row');
      }
      else {
        $(this).parent().parent().parent().find('[id^=id_milit-0-]').each(function() {
          $(this).parent().parent().css('display', 'none');
          $(this).val('');
        });
      }
    })
  })
  $(function(){
    $("#id_milit-0-served").change(function() {
      if('true' == $(this).val()) {
        $(this).parent().parent().parent().find('[id^=id_milit-0-]').each(function() {
          $(this).parent().parent().css('display', 'table-row');
        });
      }
      else {
        $(this).parent().parent().parent().find('[id^=id_milit-0-]').each(function() {
          if(this.id != 'id_milit-0-served')
          {
            $(this).parent().parent().css('display', 'none');
            $(this).val('');
          }
        });
      }
    })
  })
  /*
  function prev_edu_organisation_show(){
    if('none' == $('#id_prev_edu_organisation').parent().parent().css('display'))
    {
      $('#id_prev_edu_organisation').parent().parent().css('display', 'table-row');
      $('#id_prev_edu_organisation').val('');
      $('#prev_edu_org').html('Моего учебного заведения нет в списке');
      $('#id_prev_edu_organisation_name').parent().parent().css('display', 'none');
      $('#id_prev_edu_organisation_name').val('');
    }
    else
    {
      $('#id_prev_edu_organisation').parent().parent().css('display', 'none');
      $('#id_prev_edu_organisation').val('');
      $('#prev_edu_org').html('Вернуть выбор учебного заведения из списка');
      $('#id_prev_edu_organisation_name').parent().parent().css('display', 'table-row');
      $('#id_prev_edu_organisation_name').val('');
    }
  }*/
  $(function(){
    $(":input").change(function() {
      $(this).css('border', '1px solid darkgray');
    })
  })
$(function() {
    $( "#id_prev_edu_organisation_name" ).autocomplete({
      source: "/abit-anketa/ajax/autocomplete/"
    });
  });