$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'GET',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-tx .modal-content").html("");
        $("#modal-tx").modal("show");
      },
      success: function (data) {
        $("#modal-tx .modal-content").html(data.html_form);
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
          $("#tx-table tbody").html(data.html_tx_list);~
          $("#modal-tx").modal("hide");
        }
        else {
          $("#modal-tx .modal-tx").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create tx
  $(".js-create-tx").click(loadForm);
  $("#modal-tx").on("submit", ".js-tx-create-form", saveForm);

  // Update court
  $("#tx-table").on("click", ".js-update-tx", loadForm);
  $("#modal-tx").on("submit", ".js-tx-update-form", saveForm);

  // Delete court
  $("#tx-table").on("click", ".js-delete-tx", loadForm);
  $("#modal-tx").on("submit", ".js-tx-delete-form", saveForm);

  // This is working
  // $(".js-create-court").click(function () {
  //   $.ajax({
  //     url: 'create',
  //     type: 'get',
  //     dataType: 'json',
  //     beforeSend: function () {
  //       $("#modal-court").modal("show");
  //     },
  //     success: function (data) {
  //       $("#modal-court .modal-content").html(data.html_form);
  //     }
  //   });
  // });

});
