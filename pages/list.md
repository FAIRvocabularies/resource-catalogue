---
title: Resource list
description: List of all resources
---

# Resources list

{% for resource in site.resources %}

<a href="{{ resource.url | prepend: site.baseurl }}">
  {{ resource.title }}
</a>

<p class="post-excerpt">{{ resource.description | truncate: 160 }}</p>

{% endfor %}  
