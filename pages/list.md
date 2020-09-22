---
title: Resource list
description: List of all resources
permalink: list
---

# Resources list

{% for resource in site.resources %}

<div class="col-sm-4">
  <div class="card" style="width: 20rem;">    
    <div class="card-block">
      <h4 class="card-title">
        <a href="{{ resource.url | prepend: site.baseurl }}">
            {{ resource.title }}
        </a>
      </h4>
      <p class="card-text">{{ resource.description }}</p>
    </div>
  </div>
</div>
{% endfor %}

<p class="post-excerpt">{{ resource.description | truncate: 160 }}</p>

