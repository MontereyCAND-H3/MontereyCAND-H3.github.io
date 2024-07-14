---
layout: posts
---

{% assign current_date = site.time %}
{% assign future_hashes = site.trails | where_exp: "item", "item.date >= current_date" %}
{% assign past_hashes = site.trails | where_exp: "item", "item.date < current_date" %}



### Future Trails

<ul>
  {% for item in future_hashes | limit: 6 %}
    <li><a href="{{ item.url }}">({{ item.date | date_to_string }}) Trail #{{ item.relative_path | split: '/' | last | split: '.' | first }}: {{ item.name }}</a></li>
  {% endfor %}
</ul>


### Past Trails

<ul>
  {% for item in past_hashes %}
    <li><a href="{{ item.url }}">Trail #{{ item.relative_path | split: '/' | last | split: '.' | first }}: {{ item.name }}</a></li>
  {% endfor %}
</ul>


### Calendar of nearby trails

<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FLos_Angeles&bgcolor=%23B39DDB&showTitle=0&showPrint=0&showTabs=0&mode=AGENDA&title=Monterey%20CAN'd%20H3&src=Mjk1Y2NmOTMwNjQ4OThhNTgwNzdmMmZmMDhlOTc3ZTc0MGYzMWFhZDVlNzU5NWI2NmRmYjE5M2QwYTIyZTU2MEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=Y2FuZC5oM0BnbWFpbC5jb20&src=c2NoM2NhbGVuZGFyQGdtYWlsLmNvbQ&color=%237986CB&color=%23F4511E&color=%23B39DDB" style="border:solid 1px #777" width="600" height="400" frameborder="0" scrolling="no"></iframe>

