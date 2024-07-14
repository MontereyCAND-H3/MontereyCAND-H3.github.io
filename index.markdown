---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# https://github.com/mmistakes/minimal-mistakes/blob/master/docs/_pages/home.md

layout: splash
---

Welcome to the homepage of the Monterey CAN'd [Hash House Harriers](https://www.hashhouseharriers.com/what-is-hashing/)!

We're a running group with a drinking problem!
Or a drinking group with a running problem, I can never keep it straight!
Either way, we strongly believe that running is best when there's a nice alcoholic beverage waiting for you at the other end (and with a few beer stops along the way)!

Join us on the 2nd or 3rd Saturday of the Month for a wonderfully debaucherous time!


<div class="container">
  <div class="box box1">
    
    {% assign current_date = site.time %}
    {% assign future_hashes = site.trails | where_exp: "item", "item.date >= current_date" %}
    Join us for our next hash!
    {% for item in future_hashes | limit: 1 %}
      <a href="{{ item.url }}">({{ item.date | date_to_string }}) Trail #{{ item.relative_path | split: '/' | last | split: '.' | first }}: {{ item.name }}</a>
    {% endfor %}
  </div>
  <div class="box box2">
    Check <a href="/trails">Upcumming Trails</a> for our next outing, or join our <a href="https://chat.whatsapp.com/CHaIbQ75q5cGocMnhURlQk">whatsapp group</a> for up-to-the-minute details!
  </div>
</div>