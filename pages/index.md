---
title: Resource Catalogue
permalink: /
description: Table with all the resources
---

# Table of Resources

<table class="table table-bordered" id="resource-table" width="100%" cellspacing="0">
    <thead>
    <tr>
    <th>Title</th>
    <th>Identifier</th>    
    <th>Creator</th>
    <th>Description</th>    
    </tr>
    </thead>
    <tbody>{% for resource in site.data %}
    <tr>
    <td>{% if resource[1].landingPage %}<a href="{{ resource[0].landingPage }}" target="_blank">{{ resource[1].title }}</a>{% else %}{{ resource[1].title }}{% endif %}</td>
    <td>{{ resource[1].identifier }}</td>
    <td>{{ resource[1].creator }}</td>
    <td>{{ resource[1].description }}</td>
    </tr>
    {% endfor %}
</tbody>
</table>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<link href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css" rel="stylesheet" type="text/css" />
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.0/js/dataTables.buttons.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.flash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.html5.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.print.min.js"></script>

<script>
$('#resource-table').DataTable({
  "pageLength": 100,
  "dom": 'Bfrtip',
  "buttons": [
        'copy', 'csv', 'excel', 'pdf', 'print'
   ]
});
</script>
