$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-court .modal-content").html("");
        $("#modal-court").modal("show");
      },
      success: function (data) {
        $("#modal-court .modal-content").html(data.html_form);
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
          $("#model-table tbody").html(data.html_court_date_list); ~
            $("#modal-court").modal("hide");
        }
        else {
          $("#modal-court .modal-court").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create court
  $(".js-create-model").click(loadForm);
  $("#modal-court").on("submit", ".js-model-create-form", saveForm);

  // Update court
  $("#model-table").on("click", ".js-update-model", loadForm);
  $("#modal-model").on("submit", ".js-model-update-form", saveForm);

  // Delete court
  $("#model-table").on("click", ".js-delete-court", loadForm);
  $("#modal-court").on("submit", ".js-court-delete-form", saveForm);

  // Client Notes
  $("#model-table").on("click", ".js-create-model-note", loadForm);
  $("#modal-court").on("submit", ".js-court-note-form", saveForm);

});
