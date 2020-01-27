$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-treatment .modal-content").html("");
        $("#modal-treatment").modal("show");
      },
      success: function (data) {
        $("#modal-treatment .modal-content").html(data.html_form);
        console.log('test');
      }
    });
  };
  
  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#treatment-table tbody").html(data.html_treatment_list);
          $("#modal-treatment").modal("hide");
        }
        else {
          $("#modal-treatment .modal-treatment").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create treatment
  $(".js-create-treatment").click(loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-create-form", saveForm);

  // Update treatment
  $("#treatment-table").on("click", ".js-update-treatment", loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-update-form", saveForm);

  // Delete treatment
  $("#treatment-table").on("click", ".js-delete-treatment", loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-delete-form", saveForm);

  // Treatment Note
  $("#treatment-table").on("click", ".js-treatment-note", loadForm);
  $("#modal-treatment").on("submit", ".js-treatment-note-form", saveForm);



});
