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
          $("#court-table tbody").html(data.html_court_list); ~
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
  $(".js-create-court").click(loadForm);
  $("#modal-court").on("submit", ".js-court-create-form", saveForm);

  // Update court
  $("#court-table").on("click", ".js-update-court", loadForm);
  $("#modal-court").on("submit", ".js-court-update-form", saveForm);

  // Delete court
  $("#court-table").on("click", ".js-delete-court", loadForm);
  $("#modal-court").on("submit", ".js-court-delete-form", saveForm);

  // Client Notes
  $("#court-table").on("click", ".js-create-court-note", loadForm);
  $("#modal-court").on("submit", ".js-court-note-form", saveForm);

});
