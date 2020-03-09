$(function () {

  var loadForm = function () {
    var btn = $(this);
    let dataURL = btn.attr("data-url");
    $.ajax({
      url: dataURL,
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-model .modal-content").html("");
        $("#modal-model").modal("show");
      },
      success: function (data) {
        $("#modal-model .modal-content").html(data.html_form);
        console.log();
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
          // $("#model-table tbody").html(data.html_model_list);
          $("#modal-model").modal("hide");
        }
        else {
          $("#modal-model .modal-model").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create model
  $(".js-create-goal").click(loadForm);
  $("#modal-model").on("submit", ".js-model-create-form", saveForm);

  // Update model
  $("#model-table").on("click", ".js-update-model", loadForm);
  $("#modal-model").on("submit", ".js-model-update-form", saveForm);

  // Delete model
  $("#model-table").on("click", ".js-delete-model", loadForm);
  $("#modal-model").on("submit", ".js-model-delete-form", saveForm);

  //Eval client
  $("#model-table").on("click", ".js-eval-model", loadForm);
  $("#modal-model").on("submit", ".js-model-eval-form", saveForm);


  // model Note
  $("#model-table").on("click", ".js-model-note", loadForm);
  $("#modal-model").on("submit", ".js-model-note-form", saveForm);

});
