+++
date = '2025-07-01T06:06:51+08:00'
draft = false 
title = 'Codeblock'
summary = 'Testing Hugo codeblocks withou using custom layout/\_default/\_markup/render-codeblock.html. Restyling using CSS and overiding for overflow-x'
tags = ''
categories = ''
series = ''
+++

```text
some code
```

```shell
# some code
echo "Hello world"
```

```go
<figure {{ if isset .Params "class" }}class="{{ index .Params "class" }}"{{ end }}>
    {{ if isset .Params "link"}}<a href="{{ index .Params "link"}}">{{ end }}
        <img src="{{ index .Params "src" }}" {{ if or (isset .Params "alt") (isset .Params "caption") }}alt="{{ if isset .Params "alt"}}{{ index .Params "alt"}}{{else}}{{ index .Params "caption" }}{{ end }}"{{ end }} />
    {{ if isset .Params "link"}}</a>{{ end }}
    {{ if or (or (isset .Params "title") (isset .Params "caption")) (isset .Params "attr")}}
    <figcaption>{{ if isset .Params "title" }}
        <h4>{{ index .Params "title" }}</h4>{{ end }}
        {{ if or (isset .Params "caption") (isset .Params "attr")}}<p>
        {{ index .Params "caption" }}
        {{ if isset .Params "attrlink"}}<a href="{{ index .Params "attrlink"}}"> {{ end }}
            {{ index .Params "attr" }}
        {{ if isset .Params "attrlink"}}</a> {{ end }}
        </p> {{ end }}
    </figcaption>
    {{ end }}
```
