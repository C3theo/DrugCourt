$(function () {

    $(".js-create-court").click(function () {
      $.ajax({
        url: '/dates/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-court").modal("show");
        },
        success: function (data) {
          $("#modal-court .modal-content").html(data.html_form);
        }
      });
    });
  
  });