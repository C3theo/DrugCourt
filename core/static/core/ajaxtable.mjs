
function getColumns(data, dropColumns) {

  let columns = Array(length(data[0]));
  for (let key in data[0]) {
    if (dropColumns.indexOf(key) == -1) {
      columns.append(key);
    }
  }
  return columns
}


function generateHeader(data, btn_url, columns) {

  let $thead = $('<thead>').attr({ class: 'thead-dark' });
  let $tr = $('<tr>');
  $thead.append($tr);
  let $th = $('<th>');
  $tr.append($th);

  let $add_button = $('<button>').attr({ class: 'btn btn-primary js-update-model', 'data-url': btn_url, 'type': 'button' });
  $span = $('<span>').attr({ class: 'fas fa-plus' }).text(' Problem Goal');
  $add_button.append($span);
  $th.append($add_button);
  let dropColumns = ['client', 'objective', 'id'];
  //columns = getColumns(data, dropColumns);

  for (let key in data[0]) {
    if (dropColumns.indexOf(key) == -1) {
      let $th = $('<th>').text(key);
      $tr.append($th);

    }
  }

  return $thead

}

function generateBody(data) {

  $tbody = $('<tbody>');
  for (element of data) {

    let $tr = $('<tr>');
    let $td = $('<td>');

    let goalUrl = `/treatment/objectives/goal/${element['id']}/update`;
    $button = $('<button>').attr({ class: 'btn btn-warning btn-sm js-update-model', 'data-url': goalUrl });

    $span = $('<span>').attr({ class: 'fas fa-edit' }).text(' Edit');
    $button.append($span);
    $td.append($button)
    $tr.append($td);
    let dropColumns = ['client', 'objective', 'id'];


    for (let key in element) {
      if (dropColumns.indexOf(key) == -1) {
        let $td = $('<td>').text(element[key]);
        $tr.append($td);
        $tr.appendTo($tbody);
      }
    }
  }
  return $tbody
}


function generateTable(table, data, url) {

  let $thead = generateHeader(data, url);
  table.append($thead);
  let $tbody = generateBody(data);
  table.append($tbody);


}

// Not working
function bindChildTable(table) {
  let $tr = $(this).closest('tr');
  var row = table.row($tr);

  if (row.child.isShown()) {
    row.child.hide();
    $tr.removeClass('shown');
  }

  else {
    let data = row.data()
    let $child_table = $('<table/>').attr({ class: 'compact table table-striped table-bordered' });
    url = `/treatment/objectives/${data.pk}/goal/create`
    let goals = data.goals;
    generateTable($child_table, goals, url);
    row.child($child_table).show();
    $tr.addClass('shown');
  }
}

export {generateTable, generateHeader, generateBody};
// Main program starts here

// $(document).ready(function () {

  // $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  //   $.fn.dataTable.tables({ visible: true, api: true }).columns.adjust();
  // });

  // $('#courtDate').DataTable({
  //   columns: [
  //     {
  //       // "data": "office", // can be null or undefined
  //       "defaultContent": ""
  //     },
  //     {
  //       // "data": "office", // can be null or undefined
  //       "defaultContent": ""
  //     },
  //     {
  //       // "data": "office", // can be null or undefined
  //       "defaultContent": ""
  //     }]
  // });

  // $('#treatment').DataTable({
  //   columns: [
  //     // {
  //     //   "defaultContent": ""
  //     // },
  //     {
  //       "defaultContent": ""
  //     },
  //     {
  //       "defaultContent": ""
  //     },
  //     {
  //       "defaultContent": ""
  //     },
  //     {
  //       "defaultContent": ""
  //     },
  //     {
  //       "defaultContent": ""
  //     },
  //     {
  //       "defaultContent": ""
  //     },
  //   ]
  // });

  // // This table has a child row for additional info

  // let tbl = $('#objectives');
  // let table = tbl.DataTable({
  //   ajax: {
  //     url: tbl.attr('data-url'), // Use table's "data-url" attr
  //     dataSrc: 'results'
  //   },
  //   columns: [
  //     {
  //       "className": 'details-control',
  //       "orderable": false,
  //       "data": null,
  //       "defaultContent": ''
  //     },
  //     {
  //       data: 'obj_num',
  //       "defaultContent": ""
  //     },
  //     {
  //       data: 'description',
  //       "defaultContent": ""
  //     },
  //     {
  //       data: 'obj_target',
  //       "defaultContent": ""
  //     },
  //   ],
  //   order: [[1, 'asc']]
  // });

  // //console.log(`ajax: ${table.context[0]['ajax']['url']}`);
  // //This is where the child table is generated
  // $('#objectives tbody').on('click', 'td.details-control',
  //   function () {

  //     let $tr = $(this).closest('tr');
  //     var row = table.row($tr);

  //     if (row.child.isShown()) {
  //       row.child.hide();
  //       $tr.removeClass('shown');
  //     }

  //     else {
  //       let data = row.data()
  //       let $child_table = $('<table/>').attr({ class: 'compact table table-striped table-bordered' });
  //       // Objectives Primary Key
  //       url = `/treatment/objectives/${data.pk}/goal/create`
  //       let goals = data.goals;
  //       generateTable($child_table, goals, url);
  //       row.child($child_table).show();
  //       $tr.addClass('shown');
  //     }
  //   });

// });