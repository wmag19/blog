+++
date = '2026-02-21T14:28:05Z'
draft = false
title = 'First Post'
+++
Welcome to my blog!
## technical details:
The site is deployed using Hugo, a static site generator written in Go. I'm hosting the site on Cloudflare using a Cloudflare Worker. There are instructions on how to do this [here](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/).

I use the [Blowfish](https://themes.gohugo.io/themes/blowfish/) theme for Hugo which is deployed to my git repo via a Git submodule.

Test image:

![Image Description](/images/blowfish.png)

## deployment:
I run a script that syncs markdown files from an obsidian folder into the `content/posts` folder in my blog git repo. A script then copies the referenced images into the `static/images` folder and updates the references in the markdown files.

I used the following [blog post](https://blog.networkchuck.com/posts/my-insane-blog-pipeline/) and associated YouTube [video](https://www.youtube.com/watch?v=dnE7c0ELEH8&pp=ygUSbmV0d29yayBjaHVjayBodWdv) by Network Chuck as a base for these scripts.

## purpose: 
This blog will primarily cover interests within IT and technology which are currently Kubernetes, Coding (Golang), Cloud, AI and Linux.

## about me:
I'm Will and I'm currently working as a Cloud Engineer at a mid-sized UK company. I primarily work with Microsoft Azure, Kubernetes and Infrastructure as Code. I have an infrastructure background and have experience with Windows Servers and Helpdesk roles. I have a degree in Law and am interested in fitness, skiing, sailing and music.


