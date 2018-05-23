
var localizationobj = {};
    localizationobj.pagergotopagestring = "Перейти на:";
    localizationobj.pagershowrowsstring = "Показать строки:";
    localizationobj.pagerrangestring = " из ";
    localizationobj.pagernextbuttonstring = "Следующая";
    localizationobj.pagerpreviousbuttonstring = "Предыдущая";
    localizationobj.pagerfirstbuttonstring = 'Первая',
    localizationobj.pagerlastbuttonstring = 'Последняя',
    localizationobj.sortascendingstring = "По возрастанию";
    localizationobj.sortdescendingstring = "По убыванию";
    localizationobj.sortremovestring = "Удалить сортировку";
    localizationobj.groupsheaderstring = 'Перетащите столбец и бросьте его сюда, чтобы сгруппировать по этому столбцу',
    localizationobj.groupbystring = 'Сгруппировать по этой колонке',
    localizationobj.groupremovestring = 'Удалить из групп',
    localizationobj.firstDay = 1;
    localizationobj.percentsymbol = "%";
    localizationobj.currencysymbol = "Руб.";
    localizationobj.currencysymbolposition = "after";
    localizationobj.decimalseparator = ".";
    localizationobj.thousandsseparator = ",";
    localizationobj.AM = null;
    localizationobj.PM = null;
    localizationobj.filterclearstring = 'Очистить',
    localizationobj.filterstring = 'Применить',
    localizationobj.filtershowrowstring = 'Показать строки где:',
    localizationobj.filterorconditionstring = 'Или',
    localizationobj.filterandconditionstring = 'И',
    localizationobj.filterselectallstring = '(Выбрать все)',
    localizationobj.filterchoosestring = 'Пожалуйста, выберите:',
    localizationobj.filterstringcomparisonoperators = ["равно", "не равно", 'содержит', 'содержит (с учетом регистра)',
        'не содержит', 'не содержит (с учетом регистра)', 'начинается с', 'начинается с (с учетом регистра)',
        'заканчивается на', 'заканчивается на (с учетом регистра)', 'равно', 'равно (с учетом регистра)', 'пусто', 'не пусто'],
    localizationobj.filternumericcomparisonoperators = ["равно", "не равно", "меньше", "меньше или равно", "больше", "больше или равно", "пусто", "не пусто"],
    localizationobj.filterdatecomparisonoperators = ["равно", "не равно", "меньше", "меньше или равно", "больше", "больше или равно", "пусто", "не пусто",],
    localizationobj.filterbooleancomparisonoperators = ["равно", "не равно",],
    localizationobj.validationstring = 'Введенное значение недействительно',
    localizationobj.emptydatastring = 'Нет данных для отображения',
    localizationobj.filterselectstring = 'Выберите Фильтр',
    localizationobj.loadtext = 'Загрузка...',
    localizationobj.clearstring = 'Очистить',
    localizationobj.todaystring = 'Cегодня'
    localizationobj.patterns = {
        d: "dd.MM.yyyy",
        D: "d MMMM yyyy 'г.'",
        t: "H:mm",
        T: "H:mm:ss",
        f: "d MMMM yyyy 'г.' H:mm",
        F: "d MMMM yyyy 'г.' H:mm:ss",
        Y: "MMMM yyyy"
    }
    var days = {
        names: ["воскресенье","понедельник","вторник","среда","четверг","пятница","суббота"],
        namesAbbr: ["Вс","Пн","Вт","Ср","Чт","Пт","Сб"],
        namesShort: ["Вс","Пн","Вт","Ср","Чт","Пт","Сб"]
    };
    localizationobj.days = days;
    var months = {
        names: ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь",""],
        namesAbbr: ["янв","фев","мар","апр","май","июн","июл","авг","сен","окт","ноя","дек",""]
    };
    localizationobj.months = months;
    var monthsGenitive = {
        names: ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря",""],
        namesAbbr: ["янв","фев","мар","апр","май","июн","июл","авг","сен","окт","ноя","дек",""]
    };
    localizationobj.monthsGenitive = monthsGenitive;
