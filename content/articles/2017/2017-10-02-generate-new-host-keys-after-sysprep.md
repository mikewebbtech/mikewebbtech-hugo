---
title: "Generate new host keys after sysprep"
date: 2017-10-02T12:58:14
summary: "[libvirt work flow explained](http://webby.land/2017/09/14/my-libvirt-work-flow-explained/) The host ssh keys will be wiped from the guest image (this is a good thing) meaning that you will no longer be able to ssh..."
---

[libvirt work flow explained](http://webby.land/2017/09/14/my-libvirt-work-flow-explained/)

The host ssh keys will be wiped from the guest image (this is a good thing) meaning that you will no longer be able to ssh into that guest VM (this is a bad thing).

Fortunately this easy fix.

On Ubuntu, to regenerate new ssh host keys with this simple command
`$ sudo dpkg-reconfigure openssh-server`

if successful yoou will get something like

```
Creating SSH2 RSA key; this may take some time ...
2048 SHA256:ToJkgjGdbcFX4wCsiM0IGjGkdSCex3m/ycnsRo0qEA root@UbuntuLTS-clone (RSA)
Creating SSH2 DSA key; this may take some time ...
1024 SHA256:Ug9fJa14YMR9Fud/7bXTokffK/hM/sBVse10nSR/6Y8 root@UbuntuLTS-clone (DSA)
Creating SSH2 ECDSA key; this may take some time ...
256 SHA256:Rh6izWEXkCV6HZLIpzlGQje178vhDgb77ItaZgpDsIQ root@UbuntuLTS-clone (ECDSA)
Creating SSH2 ED25519 key; this may take some time ...
256 SHA256:UD4b7njwxWp1Q3wYf2R//udgPRzfGaeZ/6kE3VgZM+s root@UbuntuLTS-clone ED25519)
```

Restart your ssh server
`$ sudo systemctl restart sshd.service`