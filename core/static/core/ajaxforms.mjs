
let loadForm = function () {
  let btn = $(this);
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

let saveForm = function () {
  let form = $(this);

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



export {saveForm, loadForm};