---
title: Resource Catalogue
permalink: /
description: Table with all the resources
---

# Table of Resources

<!-- <div>
  {% for resource in site.data.resources %}
    <p> {{ resource }} </p>
    <p> {{ resource[0] }} </p>
    <p> {{ resource[1] }} </p>
  {% endfor %}
</div>
<div>
  {% for resourceArr in site.data.resources %}
  {% assign resource = resourceArr[1] %}
    <p> title: {{ resource.title }} </p>
    <p> landingPage: {{ resource.landingPage }} </p>
  {% endfor %}
</div> -->
<table class="table table-border" id="resource-table" width="100%" cellspacing="0">
  <thead>
    <tr>
      <th>Title</th>
      <th>Identifier</th>    
      <th>Creator</th>
      <th>Description</th>
      <th>Ext. Link</th>    
    </tr>
  </thead>
  <tbody>
  {% for resourceArray in site.resources %}
  {% assign resource = resourceArray[1] %}
    <tr>
      <td>
        <a href="{{ resourceArray[0] }}">{{ resource.title }}</a>
      </td>
      <td>{{ resource.identifier }}</td>
      <td>{{ resource.creator }}</td>
      <td>{{ resource.description }}</td>
        <td>
          {% if resource.landingPage %}
            <a href="{{ resource.landingPage }}">Visit <i class="fa fa-external-link" aria-hidden="true"></i></a>
          {% endif %}
        </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<script>
$('#resource-table').DataTable({
  "pageLength": 100,
  "dom": 'Bfrtip',
  "buttons": [
        'copy', 'csv', 'excel', 'pdf', 'print'
   ],
   "ordering": true,
   "searching": true
});
</script>
