"use strict";
// Class definition

var KTDefaultDatatableDemo = function () {
	// Private functions

	// basic demo
	var demo = function () {

		var datatable = $('#kt_datatable').KTDatatable({
			data: {
				type: 'local',
				source: {
					read: {
						url: HOST_URL + '/api/datatables/demos/default.php'
					}
				},
				pageSize: 20,
				serverPaging: true,
				serverFiltering: true,
				serverSorting: true
			},

			layout: {
				scroll: true,
				height: 550,
				footer: false
			},

			sortable: true,

			filterable: false,

			pagination: true,

			search: {
				input: $('#kt_datatable_search_query')
			},

			columns: [
				{
					field: 'OrderID',
					title: 'Nº de Identificação',
				}, {
					field: 'documento',
					title: 'Nome do arquivo',
					width: 200,
					template: function(row) {
						return row.Documento;
					},
				}, {
					field: 'ShipDate',
					title: 'Data',
					type: 'date',
					format: 'DD/MM/YYYY',
				}, {
					field: 'Type',
					title: 'Categoria',
					autoHide: false,
					// callback function support for column rendering
					template: function(row) {
						var status = {
							1: {'title': 'Imposto', 'state': 'danger'},
							2: {'title': 'Documento', 'state': 'primary'},
							3: {'title': 'Declaração', 'state': 'success'},
							4: {'title': 'Guias', 'state': 'dark'},
						};
						return '<span class="label label-' + status[row.Type].state + ' label-dot mr-2"></span><span class="font-weight-bold text-' + status[row.Type].state + '">' +
								status[row.Type].title + '</span>';
					},
				}, {
					field: 'Ações',
					title: 'Ações',
					sortable: false,
					width: 110,
					overflow: 'visible',
					autoHide: false,
					template: function() {
						return '\
							<div class="dropdown dropdown-inline">\
								<a href="javascript:;" class="btn btn-sm btn-clean btn-icon" data-toggle="dropdown">\
	                                <i class="la la-cog"></i>\
	                            </a>\
							  	<div class="dropdown-menu dropdown-menu-sm dropdown-menu-right">\
									<ul class="nav nav-hoverable flex-column">\
							    		<li class="nav-item"><a class="nav-link" href="#"><i class="nav-icon la la-edit"></i><span class="nav-text">Editar</span></a></li>\
							    		<li class="nav-item"><a class="nav-link" href="#"><i class="nav-icon la la-print"></i><span class="nav-text">Imprimir</span></a></li>\
									</ul>\
							  	</div>\
							</div>\
							<a href="javascript:;" class="btn btn-sm btn-clean btn-icon" title="Excluir">\
								<i class="la la-trash"></i>\
							</a>\
						';
					},
				}],

		});

		$('#kt_datatable_search_status').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Status');
        });

        $('#kt_datatable_search_type').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Type');
        });

        $('#kt_datatable_search_status, #kt_datatable_search_type').selectpicker();

   };

	return {
		// public functions
		init: function () {
			demo();
		}
	};
}();

jQuery(document).ready(function () {
	KTDefaultDatatableDemo.init();
});
