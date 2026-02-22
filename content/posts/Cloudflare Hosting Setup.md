+++
date = '2026-02-22T12:28:05Z'
draft = false
title = "Cloudflare Hosting Setup"
+++

I thought I should go into more detail on how the blog is hosted in Cloudflare.

First I have a worker setup with a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) bound to the root of my [domain](https://wcfm.me). This serves traffic to this domain only, as well as a custom Cloudflare worker domain.

However, I would like to also serve traffic querying the www. subdomain. In order to achieve this, I have used a Cloudflare [template](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/) which serves this purpose well. 

One complication is that Cloudflare Rules require an active DNS record. In order to have a DNS record for the Rule to 'bind' to -  I have used the Cloudflare special IP address `192.0.2.1` with a wildcard DNS A record. Please see below:

![Image Description](/images/Pasted%20image%2020260222132445.png)

I've created a Mermaid diagram to outline the rough flow of traffic:

{{< mermaid >}}
flowchart LR
  %% top row
  S[User visits site ] --> R[Redirect rule]

  %% middle row (requests)
  B[Browser makes request to www.]
  A[Browser request to domain root]

  %% bottom row (worker)
  W[Cloudflare Worker ]

  %% layout links
  B -.-> R
  R -.-> A
  A --> W
  W --> A

  %% invisible links to force vertical placement
  S -.-> B
  S -.-> A
{{< /mermaid >}}


It's worth mentioning that Cloudflare has a DNS record of type 'Worker' bound to the root of the domain to serve traffic to the Worker.

![Image Description](/images/Pasted%20image%2020260222132540.png)

I followed the [Hugo documentation](https://gohugo.io/host-and-deploy/host-on-cloudflare/) in order to setup my Worker to automatically sync from my GitHub repo, avoiding any CI/CD pipelines. I decided to use a Worker as they're more flexible and there's a preference towards Workers within the Cloudflare portal and documentation - suggesting a possible deprecation path for Cloudflare Pages.

Additionally, I setup some extra rules to enforce TLS 1.2, redirect https, enable Browser Integrity checking, prevent AI scraping and replace insecure JavaScript libraries

Overall, I found the process of setting this up very easy and most importantly, free. I don't have any certificates, DNS records or infrastructure to manage and this is all hosted within Cloudflare's free plan. However, since Hugo renders out static content, I could migrate this to another hosting partner relatively simply.
