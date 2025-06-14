---
title: "explainshell.com is awesome"
date: 2017-09-25T11:45:56
summary: "Well I came across this site today and putting it out there as a strong recommendation for bookmarking <https://explainshell.com/> OK, awesome is over kill. It does a good job at..."
---

Well I came across this site today and putting it out there as a strong recommendation for bookmarking
<https://explainshell.com/>

OK, awesome is over kill.  It does a good job at things like:

```
find ~/ -name 'core*' -exec rm {} \;
```

But bombs out at things like:

```
for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $iÃ—$j=$((i*j))\\t;done; echo;done
```
