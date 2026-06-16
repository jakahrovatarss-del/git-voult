# Zotero Template

Title:: {{title}}
URL: {{url}}
Zotero Link: {{pdfZoteroLink}}
Author: {{authors}}{{directors}}
Year:  Invalid Date

{% for annotation in annotations -%}
{%- if annotation.annotatedText -%}
{{annotation.annotatedText}}”{% if annotation.color %} {{annotation.colorCategory}} {{annotation.type | capitalize}} {% else %} {{annotation.type | capitalize}} {% endif %}[Page {{annotation.page}}](zotero://open-pdf/library/items/%7B%7Bannotation.attachment.itemKey%7D%7D?page=%7B%7Bannotation.page%7D%7D&annotation=%7B%7Bannotation.id%7D%7D)
{%- endif %}
{%- if annotation.imageRelativePath -%}
!\[\[{{annotation.imageRelativePath}}\]\] {%- endif %}
{% if annotation.comment %}
{{annotation.comment}}
{% endif %}
{% endfor -%}