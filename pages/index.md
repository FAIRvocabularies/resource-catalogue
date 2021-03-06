---
title: Resource Catalogue
permalink: /
description: Table with all the resources
---

# Table of Resources

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
  {% for resource in site.resources %}
    <tr>
      <td>
        <a href="{{ resource.url | prepend: site.baseurl }}">{{ resource.title }}</a>
      </td>
      <td>{{ resource.identifier }}</td>
      <td>{{ resource.creator }}</td>
      <td>{{ resource.description }}</td>
        <td>
          {% if resource.landingPage %}
            <a href="{{ resource.landingPage }}">Visit <i class="fa fa-external-link" aria-hidden="true"></i></a>

            <p>{{ staff_member.content | markdownify }}</p>
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
