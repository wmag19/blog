+++
date = '2026-02-21T14:28:05Z'
draft = true
title = 'First Post'
+++
This is a test first post for my Hugo static site.



Test image:

!![Image Description](/images/blowfish.png)
## Theme:

[https://themes.gohugo.io/themes/hugo-papermod/](https://themes.gohugo.io/themes/blowfish/)

## Deployment:
I run a script that syncs markdown files from an obsidian folder into the `content/posts` folder in my blog git repo. A script then copies the referenced images into the `static/images` folder and updates the references in the markdown files.

I used the following [blog post](https://blog.networkchuck.com/posts/my-insane-blog-pipeline/) and associated YouTube [video](https://www.youtube.com/watch?v=dnE7c0ELEH8&pp=ygUSbmV0d29yayBjaHVjayBodWdv) by Network Chuck as a base for these scripts.

TODO: Implement Cloudflare worker for hosting.
