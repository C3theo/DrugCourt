$(function () {

  let loadForm = function () {
    let btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-client .modal-content").html("");
        $("#modal-client").modal("show");
      },
      success: function (data) {
        $("#modal-client .modal-content").html(data.html_form);

      }
    });
  };
  
  let saveForm = function () {
    let form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#client-table tbody").html(data.html_client_list);
          $("#modal-client").modal("hide");
          
        }
        else {
          $("#modal-client .modal-client").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create client
  $(".js-create-client").click(loadForm);
  $("#modal-client").on("submit", ".js-client-create-form", saveForm);

  // Update client
  $("#client-table").on("click", ".js-update-model", loadForm);
  $("#modal-client").on("submit", ".js-model-update-form", saveForm);

  // Delete client
  $("#client-table").on("click", ".js-delete-model", loadForm);
  $("#modal-client").on("submit", ".js-model-delete-form", saveForm);

  //Eval client
  $("#client-table").on("click", ".js-eval-model", loadForm);
  $("#modal-client").on("submit", ".js-model-eval-form", saveForm);

  // Client Notes
  $("#client-table").on("click", ".js-create-client-note", loadForm);
  $("#modal-client").on("submit", ".js-client-note-form", saveForm);

});
