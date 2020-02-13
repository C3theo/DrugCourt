$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-model .modal-content").html("");
        $("#modal-model").modal("show");
      },
      success: function (data) {
        $("#modal-model .modal-content").html(data.html_form);
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
          $("#model-table tbody").html(data.html_model_list);
          $("#modal-model").modal("hide");
        }
        else {
          $("#modal-model .modal-model").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create treatment
  $(".js-create-model").click(loadForm);
  $("#modal-model").on("submit", ".js-model-create-form", saveForm);

  // Update treatment
  $("#model-table").on("click", ".js-update-model", loadForm);
  $("#modal-model").on("submit", ".", saveForm);

  // Delete treatment
  $("#model-table").on("click", ".js-delete-treatment", loadForm);
  $("#modal-model").on("submit", ".js-treatment-delete-form", saveForm);

  // Treatment Note
  $("#model-table").on("click", ".js-model-note", loadForm);
  $("#modal-model").on("submit", ".js-model-note-form", saveForm);



});
