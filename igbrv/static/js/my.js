$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});
//
// function trigger_el(list_el) {
//     $('#' + list_el[0]).prop("disabled", false);
//     var index;
//     for (index = 1; index < list_el.length; ++index) {
//         $('#' + list_el[index]).prop("disabled", true).val(0);
//     }
// }