---
layout: home
---

{% assign current_time = site.time | date: "%s" %}
{% assign future_trails = site.upcumming-trails | where_exp: "item", "item.time >= current_time" | limit: 10 %}
{% assign past_trails = site.upcumming-trails | where_exp: "item", "item.time <= current_time" %}


### Future Trails

<ul>
  {% for item in future_trails | limit: 10 %}
    <li><a href="{{ item.url }}">Trail #{{ item.relative_path | split: '/' | last | split: '.' | first }}:{{ item.name }}</a></li>
  {% endfor %}
</ul>

### Calendar of trails

<iframe src="https://calendar.google.com/calendar/embed?src=295ccf93064898a58077f2ff08e977e740f31aad5e7595b66dfb193d0a22e560%40group.calendar.google.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>


### Past Trails

<ul>
  {% for item in past_trails %}
    <li><a href="{{ item.url }}">Trail #{{ item.relative_path | split: '/' | last | split: '.' | first }}:{{ item.name }}</a></li>
  {% endfor %}
</ul>
