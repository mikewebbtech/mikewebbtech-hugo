---
title: "QEMU-GlusterFS native integration"
date: 2017-03-27T10:13:52
summary: "I was never a fan of FUSE performance (looking at you QNAP), the performance boost in block device access for Qemu/KVM based hosts using POSIX vs FUSE is impressive. Gluster..."
---

I was never a fan of FUSE performance (looking at you QNAP),  the performance boost in block device access for Qemu/KVM based hosts using POSIX vs FUSE is impressive.  Gluster as a SDS solution for oVirt self hosted engine is worth investigating for a multitude of use cases.

My own testing for HA replication has yielded positive results.

Source: [QEMU-GlusterFS native integration](https://raobharata.wordpress.com/2012/10/29/qemu-glusterfs-native-integration/)