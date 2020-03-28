import { saveForm, loadForm } from './ajaxforms.js';
import { generateTable } from './ajaxtable.js';

$(function () {

    // Create model
    $(".js-create-goal").click(loadForm);
    $("#modal-model").on("submit", ".js-model-create-form", saveForm);

    // Update model
    $("#model-table").on("click", ".js-update-model", loadForm);
    $("#modal-model").on("submit", ".js-model-update-form", saveForm);

    // Delete model
    $("#model-table").on("click", ".js-delete-model", loadForm);
    $("#modal-model").on("submit", ".js-model-delete-form", saveForm);

    // model Note
    $("#model-table").on("click", ".js-model-note", loadForm);
    $("#modal-model").on("submit", ".js-model-note-form", saveForm);

    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        $.fn.dataTable.tables({ visible: true, api: true }).columns.adjust();
    });

    $('#courtDate').DataTable({
        columns: [
            {
                // "data": "office", // can be null or undefined
                "defaultContent": ""
            },
            {
                // "data": "office", // can be null or undefined
                "defaultContent": ""
            },
            {
                // "data": "office", // can be null or undefined
                "defaultContent": ""
            }]
    });

    $('#treatment').DataTable({
        columns: [
            // {
            //   "defaultContent": ""
            // },
            {
                "defaultContent": ""
            },
            {
                "defaultContent": ""
            },
            {
                "defaultContent": ""
            },
            {
                "defaultContent": ""
            },
            {
                "defaultContent": ""
            },
            {
                "defaultContent": ""
            },
        ]
    });

    // This table has a child row for additional info

    let tbl = $('#objectives');
    let table = tbl.DataTable({
        ajax: {
            url: tbl.attr('data-url'), // Use table's "data-url" attr
            dataSrc: 'results'
        },
        columns: [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {
                data: 'obj_num',
                "defaultContent": ""
            },
            {
                data: 'description',
                "defaultContent": ""
            },
            {
                data: 'obj_target',
                "defaultContent": ""
            },
        ],
        order: [[1, 'asc']]
    });

    //console.log(`ajax: ${table.context[0]['ajax']['url']}`);
    //This is where the child table is generated
    $('#objectives tbody').on('click', 'td.details-control',
        function () {

            let $tr = $(this).closest('tr');
            var row = table.row($tr);

            if (row.child.isShown()) {
                row.child.hide();
                $tr.removeClass('shown');
            }

            else {
                let data = row.data()
                let $child_table = $('<table/>').attr({ class: 'compact table table-striped table-bordered' });
                // Objectives Primary Key
                url = `/treatment/objectives/${data.pk}/goal/create`
                let goals = data.goals;
                generateTable($child_table, goals, url);
                row.child($child_table).show();
                $tr.addClass('shown');
            }
        });


});
