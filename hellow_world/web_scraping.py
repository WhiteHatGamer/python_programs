from bs4 import BeautifulSoup
import re
import sys,requests

try:
    crickbuzz = requests.get('https://crickbuzz.com')
except Exception as e:
    print(f"Exception occured {e}")
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="HandheldFriendly" content="True" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="apple-itunes-app" content="app-id=490474324, affiliate-data=ct=Buffer%20Resources&amp;pt=936146" />
  <link rel="dns-prefetch" href="https://fonts.gstatic.com" />
  <link rel="preload" href="https://fonts.gstatic.com/" crossorigin />
  <link
    rel="preload"
    href="https://fonts.googleapis.com/css?family=Poppins:600,700|Roboto:300,400,400i,700,700i&display=swap"
    rel="stylesheet"
    as="style"
    onload="this.onload=null;this.rel='stylesheet'"
/>
<noscript>
  <link
    href="https://fonts.googleapis.com/css?family=Poppins:600,700|Roboto:300,400,400i,700,700i&display=swap"
    rel="stylesheet"
    type="text/css"
  />
</noscript>
  <link rel="stylesheet" type="text/css" href="https://buffer.com/resources/assets/built/screen.css?v=5ec3319331" />
  <link rel="dns-prefetch" href="https://cdn.jsdelivr.net" />
  <title>Buffer Blog - Thoughts on Social Media &amp; Online Marketing</title>
<!-- Start cookieyes banner --> <script id="cookieyes" type="text/javascript" src="https://cdn-cookieyes.com/client_data/73a7491b50fa6e35a4e9e152/script.js"></script> <!-- End cookieyes banner -->
  <meta name="description" content="Buffer’s social media marketing blog covers the latest social media tools, analytics, and strategies for Twitter, Facebook, and more..." />
    <link rel="icon" href="https://buffer.com/resources/content/images/size/w256h256/2022/03/android-chrome-512x512-1.png" type="image/png" />
    <link rel="canonical" href="https://buffer.com/resources/" />
    <meta name="referrer" content="no-referrer-when-downgrade" />
    <link rel="next" href="https://buffer.com/resources/page/2/" />
    <meta property="og:site_name" content="Buffer Resources" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Buffer Resources" />
    <meta property="og:description" content="Buffer’s social media marketing blog covers the latest social media tools, analytics, and strategies for Twitter, Facebook, and more..." />
    <meta property="og:url" content="https://buffer.com/resources/" />
    <meta property="og:image" content="https://buffer.com/resources/content/images/2020/07/OG-image_resources-1.png" />
    <meta property="article:publisher" content="https://www.facebook.com/bufferapp" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Buffer Resources" />
    <meta name="twitter:description" content="Buffer’s social media marketing blog covers the latest social media tools, analytics, and strategies for Twitter, Facebook, and more..." />
    <meta name="twitter:url" content="https://buffer.com/resources/" />
    <meta name="twitter:image" content="https://buffer.com/resources/content/images/2020/07/OG-image_resources.png" />
    <meta name="twitter:site" content="@buffer" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="627" />
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "publisher": {
        "@type": "Organization",
        "name": "Buffer Resources",
        "url": "https://buffer.com/resources/",
        "logo": {
            "@type": "ImageObject",
            "url": "https://buffer.com/resources/content/images/2021/02/buffer-logo.svg",
            "width": 143,
            "height": 36
        }
    },
    "url": "https://buffer.com/resources/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://buffer.com/resources/"
    },
    "description": "Buffer’s social media marketing blog covers the latest social media tools, analytics, and strategies for Twitter, Facebook, and more..."
}
    </script>
    <meta name="generator" content="Ghost 5.36" />
    <link rel="alternate" type="application/rss+xml" title="Buffer Resources" href="https://buffer.com/resources/rss/" />
    <script defer src="https://cdn.jsdelivr.net/ghost/portal@~2.25/umd/portal.min.js" data-ghost="https://buffer.com/resources/" data-key="ca2adf4f9fdb1524bdc1ba8a53" data-api="https://buffer.ghost.io/resources/ghost/api/content/" crossorigin="anonymous"></script><style id="gh-members-styles">.gh-post-upgrade-cta-content,
.gh-post-upgrade-cta {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    text-align: center;
    width: 100%;
    color: #ffffff;
    font-size: 16px;
}
.gh-post-upgrade-cta-content {
    border-radius: 8px;
    padding: 40px 4vw;
}
.gh-post-upgrade-cta h2 {
    color: #ffffff;
    font-size: 28px;
    letter-spacing: -0.2px;
    margin: 0;
    padding: 0;
}
.gh-post-upgrade-cta p {
    margin: 20px 0 0;
    padding: 0;
}
.gh-post-upgrade-cta small {
    font-size: 16px;
    letter-spacing: -0.2px;
}
.gh-post-upgrade-cta a {
    color: #ffffff;
    cursor: pointer;
    font-weight: 500;
    box-shadow: none;
    text-decoration: underline;
}
.gh-post-upgrade-cta a:hover {
    color: #ffffff;
    opacity: 0.8;
    box-shadow: none;
    text-decoration: underline;
}
.gh-post-upgrade-cta a.gh-btn {
    display: block;
    background: #ffffff;
    text-decoration: none;
    margin: 28px 0 0;
    padding: 8px 18px;
    border-radius: 4px;
    font-size: 16px;
    font-weight: 600;
}
.gh-post-upgrade-cta a.gh-btn:hover {
    opacity: 0.92;
}</style>
    <script defer src="https://cdn.jsdelivr.net/ghost/sodo-search@~1.1/umd/sodo-search.min.js" data-key="ca2adf4f9fdb1524bdc1ba8a53" data-styles="https://cdn.jsdelivr.net/ghost/sodo-search@~1.1/umd/main.css" data-sodo-search="https://buffer.ghost.io/resources/" crossorigin="anonymous"></script>
    <link href="https://buffer.com/resources/webmentions/receive/" rel="webmention" />
    <script defer src="/resources/public/cards.min.js?v=5ec3319331"></script>
    <link rel="stylesheet" type="text/css" href="/resources/public/cards.min.css?v=5ec3319331">
    <script defer src="/resources/public/member-attribution.min.js?v=5ec3319331"></script>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
<link rel="icon" type="image/svg+xml" href="https://buffer.com/static/icons/favicon.svg">
<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1521042244879171');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1521042244879171&ev=PageView&noscript=1"
/></noscript>
<!-- End Facebook Pixel Code -->
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-18896347-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-18896347-1'); // Universal Analytics property.
  gtag('config', 'G-VQSKXK8EGY'); // Google Analytics 4 property.
  // Updated December 9th 2021, Andy & Matt.
</script>
<script>
  !function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"];analytics.factory=function(e){return function(){var t=Array.prototype.slice.call(arguments);t.unshift(e);analytics.push(t);return analytics}};for(var e=0;e<analytics.methods.length;e++){var key=analytics.methods[e];analytics[key]=analytics.factory(key)}analytics.load=function(key,e){var t=document.createElement("script");t.type="text/javascript";t.async=!0;t.src="https://segment-analytics.buffer.com/analytics.js/v1/" + key + "/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(t,n);analytics._loadOptions=e};analytics._writeKey="SSxPVcWxeEEJDecDDHywm1qf9z3c3i3h";;analytics.SNIPPET_VERSION="4.15.3";
  analytics.load("SSxPVcWxeEEJDecDDHywm1qf9z3c3i3h");
  analytics.page();
  }}();
</script>
<style>:root {--ghost-accent-color: #15171A;}</style>
</head>
<body class="home-template " x-data="{ ...mobileMenu(), ...searchModal() }"
  :class="{ 'gh-head-open': mobileMenuIsOpen() }" x-on:keydown.escape="closeSearchModal">
  <div class="gh-viewport">
   <header class="header-navigation js-header-navigation">
      <section class="header-navigation-container">
        <div class="nav-logo"><a href="/" name="Buffer Homepage"><img src="https://buffer.com/resources/assets/img/header/buffer.svg?v=5ec3319331" width="100" height="25" alt="Buffer"></a></div>
        <nav class="navigation" role="navigation">
            <section class="navigation-desktop-menu">
                <div class="dropdown-item">
                    <a href="#" class="dropdown-link" aria-haspopup="true">Tools <img src="https://buffer.com/resources/assets/img/header/arrow-down.svg?v=5ec3319331" width="18" height="18" alt=""></a>
                    <div class="dropdown-menu" aria-label="submenu">
                        <div class="dropdown-container">
                            <a class="dropdown-menu-item" href="/publish">
                                <img src="https://buffer.com/resources/assets/img/header/tool-icons/publish-icon.svg?v=5ec3319331">
                                <div>
                                    <h3>Publishing</h3>
                                    <p>Plan, collaborate, and publish thumb-stopping content</p>
                                </div>
                            </a>
                            <a class="dropdown-menu-item" href="/analyze">
                                <img src="https://buffer.com/resources/assets/img/header/tool-icons/analyze-icon.svg?v=5ec3319331" alt=""
                                    style="position: relative; left:-7px">
                                <div>
                                    <h3>Analytics</h3>
                                    <p>Analyze social media performance and create reports</p>
                                </div>
                            </a>
                            <a class="dropdown-menu-item" href="/engage">
                                <img src="https://buffer.com/resources/assets/img/header/tool-icons/engage-icon.svg?v=5ec3319331" style="position: relative; left:-2px"
                                    alt="">
                                <div>
                                    <h3>Engagement</h3>
                                    <p>Quickly navigate your comments and engage with your audience</p>
                                </div>
                            </a>
                            <a class="dropdown-menu-item" href="/start-page">
                                <img src="https://buffer.com/resources/assets/img/header/tool-icons/start-page-icon.svg?v=5ec3319331"
                                    style="position: relative; left:-5px; top:-3px" alt="">
                                <div>
                                    <h3>Start Page</h3>
                                    <p>Build a customized landing page in minutes</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="dropdown-item">
                    <a href="#" class="dropdown-link" aria-haspopup="true">Channels <img src="https://buffer.com/resources/assets/img/header/arrow-down.svg?v=5ec3319331" alt="" width="18" height="18"></a>
                    <div class="dropdown-menu" aria-label="submenu">
                        <div class="dropdown-container dropdown-container_channels">
                            <a class="dropdown-menu-item" href="/facebook">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/facebook.svg?v=5ec3319331" alt="">
                                <h3>Facebook</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/google-business-profile">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/google-business-profile.svg?v=5ec3319331"
                                    style="position:relative;top:8px;left:10px;transform:scale(1.8)" alt="">
                                <h3>Google Business Profile</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/instagram">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/instagram.svg?v=5ec3319331" alt="">
                                <h3>Instagram</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/linkedin">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/linkedin.svg?v=5ec3319331" alt="">
                                <h3>LinkedIn</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/mastodon">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/mastodon.svg?v=5ec3319331" alt="">
                                <h3>Mastodon</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/pinterest">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/pinterest.svg?v=5ec3319331" alt="">
                                <h3>Pinterest</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/shopify">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/shopify.svg?v=5ec3319331" alt="">
                                <h3>Shopify</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/tiktok">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/tiktok.svg?v=5ec3319331"  alt="">
                                <h3>TikTok</h3>
                            </a>
                            <a class="dropdown-menu-item" href="/twitter">
                                <img src="https://buffer.com/resources/assets/img/header/channel-icons/twitter.svg?v=5ec3319331"style="transform:scale(1.2)" alt="">
                                <h3>Twitter</h3>
                            </a>
                        </div>
                    </div>
                </div>
                <div><a href="/pricing">Pricing</a></div>
                <div><a href="/resources">Blog</a></div>
            </section>
        </nav>
        <div class="login-signup-mobilemenu">
            <a class="search-icon" @click="openSearchModal" aria-label="Search" href="javascript:;" role="button"><img src="https://buffer.com/resources/assets/img/header/search.svg?v=5ec3319331" alt="" width="17" height="18"></a>
            <a href=" https://login.buffer.com/login" class="login-link">Log in</a>
            <a class="gh-button gh-button-primary desktop-signup"
                href="https://login.buffer.com/signup?product=buffer&plan=free&cycle=year&cta=bufferBlogResources-homepage-nav-signup-1">
                Get started now</a>
            <button class="mobile-menu-button js-toggle-menu" aria-label="Open Mobile Menu">
                <img src="https://buffer.com/resources/assets/img/header/hamburger.svg?v=5ec3319331" height="40px" width="40px" alt="">
            </button>
        </div>
         </section>
      <progress id="reading-progress" class="bf-progress" value="0" aria-valuenow="0" aria-valuemin="0"
        aria-valuemax="100">
        <div class="bf-progress-container">
          <span class="bf-progress-bar"></span>
        </div>
      </progress>
    </header>
    <section class="mobile-menu is-hidden js-mobile-menu">
        <section class="mobile-menu-header">
            <img src="https://buffer.com/resources/assets/img/header/buffer.svg?v=5ec3319331" height="auto" width="100px">
            <button class="mobile-menu-button js-toggle-menu" aria-label="Close Mobile Menu">
                <img src="https://buffer.com/resources/assets/img/header/x.svg?v=5ec3319331" height="40px" width="40px">
            </button>
        </section>
        <section class="mobile-menu-container">
            <details class="mobile-menu-dropdown">
                <summary>
                    <h3>Tools <img src="https://buffer.com/resources/assets/img/header/arrow-down.svg?v=5ec3319331"  width="18" height="18" alt=""></h3>
                </summary>
                <section class="mobile-menu-dropdown-links mobile-tool-links">
                    <a class="" href="/publish"><img src="https://buffer.com/resources/assets/img/header/tool-icons/publish-icon.svg?v=5ec3319331" alt=""> Publish</a>
                    <a class="" href="/analyze"><img src="https://buffer.com/resources/assets/img/header/tool-icons/analyze-icon.svg?v=5ec3319331"
                            style="position: relative; left:-7px" alt="">Analyze</a>
                    <a class="" href="/engage"><img src="https://buffer.com/resources/assets/img/header/tool-icons/engage-icon.svg?v=5ec3319331" style="position: relative; left:-6px"
                            alt="">Engage</a>
                    <a class="" href="/start-page"><img src="https://buffer.com/resources/assets/img/header/tool-icons/start-page-icon.svg?v=5ec3319331"
                            style="position: relative; left:-6px" alt="">Start Page</a>
                </section>
            </details>
            <details class="mobile-menu-dropdown">
                <summary>
                    <h3>Channels <img src="https://buffer.com/resources/assets/img/header/arrow-down.svg?v=5ec3319331" width="18" height="18" alt=""></h3>
                </summary>
                <section class="mobile-menu-dropdown-links mobile-channel-links">
                    <a class="" href="/facebook"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/facebook.svg?v=5ec3319331" alt=""> Facebook</a>
                    <a class="" href="/google-business-profile"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/google-business-profile.svg?v=5ec3319331"
                            style="position:relative;top:8px;left:4px;transform:scale(1.8)" alt=""> Google Business
                        Profile</a>
                    <a class="" href="/instagram"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/instagram.svg?v=5ec3319331" alt="">
                        Instagram</a>
                    <a class="" href="/linkedin"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/linkedin.svg?v=5ec3319331" alt=""> LinkedIn</a>
                    <a class="" href="/mastodon"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/mastodon.svg?v=5ec3319331" alt=""> Mastodon</a>
                    <a class="" href="/pinterest"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/pinterest.svg?v=5ec3319331" alt=""> Pinterest</a>
                    <a class="" href="/shopify"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/shopify.svg?v=5ec3319331" alt=""> Shopify</a>
                    <a class="" href="/tiktok"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/tiktok.svg?v=5ec3319331" alt=""> TikTok</a>
                    <a class="" href="/twitter"> <img src="https://buffer.com/resources/assets/img/header/channel-icons/twitter.svg?v=5ec3319331" style="transform:scale(1.2)" alt="">
                        Twitter</a>
                </section>
            </details>
            <section class="mobile-links-container">
                <a class="mobile-link" href="/pricing">Pricing</a>
                <a class="mobile-link" href="/resources">Blog</a>
            </section>
            <a class="mobile-link mobile-link-login" href="https://login.buffer.com/login">Log in</a>
            <a class="gh-button gh-button-primary gh-button-fit mobile-link-signup"
                href="https://login.buffer.com/signup?product=buffer&plan=free&cycle=year&cta=bufferBlogResources-homepage-mobile-nav-signup-1">Get
                started now</a>
        </section>
    </section>
    <main class="gh-main">
<article class="gh-article bf-featuredpost post tag-flow tag-social-media-marketing featured">
  <div class="gh-header-container gh-container">
    <div class="gh-header-content">
      <div class="gh-post-breadcrumb">
        <!-- Determine correct breadcrumbs -->
    <a class="gh-breadcrumb-link" href="https://buffer.com/resources/publications/">Publications</a>
<!-- You can pass a property with the partial, in which case we only render the first part of the
breadcrumb. This is used on the tag pages like so: '> "breadcrumb" short="true"' -->
        <svg viewBox="0 0 18 27" xmlns="http://www.w3.org/2000/svg"><path d="M2.397 25.426l13.143-11.5-13.143-11.5" stroke-width="3" stroke="currentColor" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <a class="gh-breadcrumb-link" href="https://buffer.com/resources/flow/"><strong>Flow</strong></a>
      </div>
      <div>
        <a href="/resources/creative-process/">
          <h1 class="gh-title">5 Steps to Figuring out Your Creative Process (ft. Advice from Creators)</h1>
        </a>
        <p class="gh-excerpt">In this article, we explore the creative process of four creators: Jayde Powell, Dre Fox, Joy Ofodu, and Katie Xu. Each of these creators has a unique style and approach to their craft, making them stand out in their respective fields.</p>
        <div class="gh-header-meta">
          <time datetime="2023-03-02">Mar 2, 2023</time>
          <span class="bf-readingtime"><svg width="24" height="10" viewBox="0 0 24 10" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="5.7998" cy="5" r="4" stroke="#B8B8B8" stroke-width="1.59999" stroke-linecap="round"/>
<path d="M9.65337 2.24106C9.23422 2.10134 8.78117 2.32787 8.64145 2.74702C8.50173 3.16617 8.72826 3.61922 9.14741 3.75894L9.65337 2.24106ZM14.4534 3.75894C14.8725 3.61922 15.099 3.16617 14.9593 2.74702C14.8196 2.32787 14.3666 2.10134 13.9474 2.24106L14.4534 3.75894ZM11.8004 3.8L11.5474 4.55894C11.7116 4.61368 11.8892 4.61368 12.0534 4.55894L11.8004 3.8ZM9.14741 3.75894L11.5474 4.55894L12.0534 3.04106L9.65337 2.24106L9.14741 3.75894ZM12.0534 4.55894L14.4534 3.75894L13.9474 2.24106L11.5474 3.04106L12.0534 4.55894Z" fill="#B8B8B8"/>
<path d="M22.5996 5.79922L22.5996 4.19922" stroke="#B8B8B8" stroke-width="1.59999" stroke-linecap="round"/>
<path d="M1 5.79922L1 4.19922" stroke="#B8B8B8" stroke-width="1.59999" stroke-linecap="round"/>
<circle cx="17.7998" cy="5" r="4" stroke="#B8B8B8" stroke-width="1.59999" stroke-linecap="round"/>
</svg>
 6 min read</span>
          <a href="/resources/flow/" class="bf-badge bf-badge-flow">Flow</a>
        </div>
      </div>
      <a class="gh-author-card" href="/resources/author/tamilore/">
        <div class="gh-author-card-image-wrap">
          <img class="gh-author-card-image" src="/resources/content/images/size/w100/2022/03/B6060E07-7A0E-4C6C-82EE-C654EA065314_1_102_o.jpeg" alt="Tamilore Oladipo" loading="lazy" />
        </div>
        <div class="gh-author-card-content">
          <strong>Tamilore Oladipo</strong>
          <span class="gh-author-card-bio">Content Writer @ Buffer</span>
        </div>
      </a>
    </div>
    <a class="gh-header-image" href="/resources/creative-process/">
      <img class="gh-feature-image" srcset="/resources/content/images/size/w300/2023/03/patrick-tomasso-1NTFSnV-KLs-unsplash--1-.jpg 300w,
                                    /resources/content/images/size/w600/2023/03/patrick-tomasso-1NTFSnV-KLs-unsplash--1-.jpg 600w,
                                    /resources/content/images/size/w1200/2023/03/patrick-tomasso-1NTFSnV-KLs-unsplash--1-.jpg 1000w"
        sizes="(max-width: 700px) 100px, 400px, 700px" loading="lazy" src="/resources/content/images/size/w1200/2023/03/patrick-tomasso-1NTFSnV-KLs-unsplash--1-.jpg"
        alt="5 Steps to Figuring out Your Creative Process (ft. Advice from Creators)" />
    </a>
  </div>
</article>
<div class="bf-homefeed gh-page">
  <div class="gh-container bf-tab" x-data="tabbedListTop()" x-init="init()">
    <div class="bf-scroll-nav-wrapper">
      <nav class="bf-scroll-nav">
        <a href="javascript:" :class="{ 'active': activeTab === 'latest'}" @click="changeTab('latest')">
          Latest Updates
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'smallbusiness'}" @click="changeTab('smallbusiness')" @mouseover="loadContent('smallbusiness')">
          Small Business
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'socialmediamarketing'}" @click="changeTab('socialmediamarketing')"
          @mouseover="loadContent('socialmediamarketing')">
          Social Media Marketing
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'bufferupdates'}" @click="changeTab('bufferupdates')"
          @mouseover="loadContent('bufferupdates')">
          News
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'podcasts'}" @click="changeTab('podcasts')"
          @mouseover="loadContent('podcasts')">
         Podcasts
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'open'}" @click="changeTab('open')"
          @mouseover="loadContent('open')">
          Open blog
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'casestudies'}" @click="changeTab('casestudies')"
          @mouseover="loadContent('casestudies')">
          Case studies
        </a>
      </nav>
    </div>
    <div x-show="activeTab == 'latest'">
      <div id="latest-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'smallbusiness'">
      <div id="smallbusiness-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'socialmediamarketing'">
      <div id="socialmediamarketing-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'bufferupdates'">
      <div id="bufferupdates-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'podcasts'">
      <div id="podcasts-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'open'">
      <div id="open-banner" class="bf-tab-banner">
        <img class="bf-banner-logo" src="https://buffer.com/resources/assets/img/open.svg?v=5ec3319331" alt="Open" loading="lazy" />
        <p class="bf-banner-desc"></p>
      </div>
      <div id="open-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'casestudies'">
      <div id="casestudies-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
  </div>
</div>
<div class="bf-newsletter-cta">
  <div class="bf-newsletter-cta-container gh-container">
    <div class="bf-newsletter-cta-form">
      <h3>Subscribe to our newsletter</h3>
      <p>We’ll keep you in the loop on our best advice and strategies for social media marketing and growing a small business.</p>
      <!-- Begin Buffer API Signup Form -->
      <form action="https://buffer.com/newsletter" method="post">
        <div class="bf-newsletter-signup">
          <input class="gh-input required email" type="email" value="" name="email" placeholder="Your email address..."
            autocomplete="false" aria-label="Email">
          <button class="gh-button gh-button-lightred" value="Subscribe" type="submit" role="button"
            aria-label="Subscribe" />Subscribe</button>
        </div>
      </form>
      <!-- END Buffer API Signup Form -->
    </div>
  </div>
</div>
<div class="bf-home-bb">
  <div class="gh-container bf-home-sm-content">
    <img class="bf-home-bb-banner" src="https://buffer.com/resources/assets/img/SmallBusinessBanner2.png?v=5ec3319331" alt="Breaking Brand" loading="lazy" />
    <div class="bf-home-sm-text">
      <h4>Small Business, Big Lessons is a podcast from Buffer that goes behind the scenes with inspirational small businesses who are truly driving innovation and redefining how work happens.</h4>
      <a class="gh-button gh-button-lightred"
    href="https://buffer.com/small-business-big-lessons" role="button">Listen now</a>
      <div class="bf-home-bb-cta">
        <a href="https://podcasts.apple.com/us/podcast/small-business-big-lessons/id1587319071" target="_blank" rel="noopener"
          aria-label="Apple Podcasts"><svg xmlns="http://www.w3.org/2000/svg" width="149.105" height="26.755" viewBox="0 0 149.105 26.755"><g fill="#FFF"><path d="M34.654 7.537h-3.777V1.482h.94v5.19h2.837v.865zM35.743 1.616c0-.315.248-.554.583-.554.336 0 .584.24.584.554 0 .31-.248.55-.584.55-.335 0-.583-.24-.583-.55zm.134 1.352h.898v4.569h-.898v-4.57zM39.897 2.88c1.028 0 1.7.478 1.788 1.284h-.864c-.084-.336-.411-.55-.924-.55-.503 0-.885.24-.885.596 0 .272.23.444.726.557l.76.177c.868.201 1.275.574 1.275 1.246 0 .86-.802 1.435-1.893 1.435-1.087 0-1.796-.49-1.875-1.3h.902c.113.352.449.57.995.57.562 0 .96-.252.96-.617 0-.272-.213-.449-.671-.557l-.797-.185c-.87-.206-1.272-.597-1.272-1.276 0-.81.743-1.38 1.775-1.38zM44.171 1.83v1.158h.99v.76h-.99v2.35c0 .478.198.688.646.688.139 0 .219-.008.345-.02v.75a2.906 2.906 0 01-.492.046c-1.003 0-1.401-.352-1.401-1.233V3.748h-.726v-.76h.726V1.831h.902zM50.161 6.303c-.206.819-.935 1.322-1.98 1.322-1.31 0-2.111-.898-2.111-2.358s.818-2.387 2.106-2.387c1.272 0 2.04.868 2.04 2.303v.315H46.99v.05c.029.801.495 1.31 1.216 1.31.546 0 .92-.198 1.087-.554h.87zM46.99 4.832h2.308c-.021-.718-.458-1.184-1.125-1.184s-1.133.47-1.183 1.184zM51.421 2.968h.87v.725h.067c.222-.508.675-.813 1.363-.813 1.02 0 1.582.612 1.582 1.699v2.958h-.902V4.805c0-.734-.319-1.1-.986-1.1s-1.091.446-1.091 1.159v2.673h-.903v-4.57zM58.943 5.25c0-1.473.822-2.37 2.157-2.37 1.33 0 2.152.897 2.152 2.37 0 1.481-.818 2.375-2.152 2.375-1.339 0-2.157-.894-2.157-2.375zm3.383 0c0-.99-.446-1.57-1.226-1.57-.785 0-1.226.58-1.226 1.57 0 .999.44 1.574 1.226 1.574.78 0 1.226-.58 1.226-1.574zM64.458 2.968h.87v.725h.067c.222-.508.675-.813 1.363-.813 1.02 0 1.582.612 1.582 1.699v2.958h-.902V4.805c0-.734-.319-1.1-.986-1.1s-1.091.446-1.091 1.159v2.673h-.903v-4.57z"/></g><g fill="#FFF"><path d="M38.193 20.403h-4.734l-1.136 3.356h-2.005L34.8 11.341h2.083l4.484 12.418h-2.04l-1.135-3.356zm-4.243-1.549h3.752l-1.85-5.447H35.8l-1.85 5.447zM51.05 19.233c0 2.814-1.506 4.621-3.778 4.621-1.29 0-2.315-.577-2.849-1.584h-.043v4.485h-1.858v-12.05h1.799v1.507h.034c.516-.972 1.618-1.6 2.883-1.6 2.298 0 3.812 1.815 3.812 4.621zm-1.91 0c0-1.833-.947-3.038-2.393-3.038-1.42 0-2.375 1.23-2.375 3.038 0 1.824.956 3.046 2.375 3.046 1.446 0 2.393-1.196 2.393-3.046zM61.015 19.233c0 2.814-1.506 4.621-3.778 4.621-1.29 0-2.315-.577-2.849-1.584h-.043v4.485h-1.858v-12.05h1.799v1.507h.034c.516-.972 1.618-1.6 2.883-1.6 2.297 0 3.812 1.815 3.812 4.621zm-1.91 0c0-1.833-.947-3.038-2.393-3.038-1.42 0-2.375 1.23-2.375 3.038 0 1.824.955 3.046 2.375 3.046 1.446 0 2.393-1.196 2.393-3.046zM62.52 11.342h1.86V23.76h-1.86V11.342zM74.055 21.1c-.25 1.644-1.85 2.772-3.898 2.772-2.634 0-4.269-1.765-4.269-4.596 0-2.84 1.644-4.681 4.19-4.681 2.505 0 4.08 1.72 4.08 4.465v.637h-6.394v.112c0 1.55.973 2.565 2.436 2.565 1.032 0 1.841-.49 2.09-1.273h1.765zm-6.282-2.702h4.526c-.043-1.386-.93-2.298-2.22-2.298-1.283 0-2.211.93-2.306 2.298zM84.057 11.342c2.41 0 4.088 1.66 4.088 4.079 0 2.427-1.713 4.095-4.148 4.095h-2.668v4.244H79.4V11.342h4.656zm-2.728 6.557h2.211c1.678 0 2.633-.904 2.633-2.47 0-1.566-.955-2.461-2.624-2.461h-2.22v4.931zM88.824 19.233c0-2.848 1.677-4.639 4.294-4.639 2.625 0 4.295 1.79 4.295 4.64 0 2.856-1.662 4.638-4.295 4.638s-4.294-1.782-4.294-4.639zm6.695 0c0-1.954-.895-3.107-2.401-3.107s-2.402 1.162-2.402 3.107c0 1.962.896 3.107 2.402 3.107s2.401-1.145 2.401-3.107zM98.717 19.233c0-2.797 1.54-4.622 3.786-4.622 1.3 0 2.325.603 2.84 1.6h.035v-4.87h1.868V23.76h-1.808v-1.54h-.034c-.533 1.032-1.567 1.634-2.883 1.634-2.264 0-3.804-1.824-3.804-4.62zm1.902 0c0 1.859.947 3.046 2.392 3.046 1.429 0 2.384-1.205 2.384-3.046 0-1.825-.955-3.038-2.384-3.038-1.445 0-2.392 1.196-2.392 3.038zM115.154 17.821c-.163-.955-.912-1.669-2.134-1.669-1.429 0-2.376 1.196-2.376 3.081 0 1.928.956 3.09 2.392 3.09 1.154 0 1.912-.577 2.118-1.627h1.79c-.206 1.902-1.73 3.176-3.924 3.176-2.582 0-4.269-1.765-4.269-4.639 0-2.814 1.687-4.638 4.251-4.638 2.324 0 3.77 1.462 3.925 3.226h-1.773zM118.082 21.186c0-1.583 1.213-2.539 3.365-2.668l2.478-.137v-.689c0-1.007-.662-1.575-1.789-1.575-1.033 0-1.756.491-1.902 1.274h-1.738c.051-1.635 1.574-2.797 3.69-2.797 2.161 0 3.59 1.18 3.59 2.96v6.206h-1.781v-1.49h-.043c-.526 1.007-1.67 1.645-2.858 1.645-1.772 0-3.012-1.102-3.012-2.729zm5.843-.817v-.697l-2.228.137c-1.11.07-1.739.551-1.739 1.325 0 .792.655 1.31 1.653 1.31 1.3 0 2.314-.896 2.314-2.075zM130.963 14.603c2.006 0 3.443 1.11 3.486 2.71h-1.747c-.077-.8-.757-1.29-1.79-1.29-1.007 0-1.678.464-1.678 1.17 0 .542.447.903 1.386 1.136l1.523.353c1.824.439 2.513 1.11 2.513 2.436 0 1.635-1.55 2.754-3.761 2.754-2.135 0-3.571-1.094-3.709-2.746h1.84c.13.869.827 1.334 1.955 1.334 1.11 0 1.808-.456 1.808-1.179 0-.56-.345-.86-1.291-1.102l-1.619-.395c-1.635-.397-2.462-1.231-2.462-2.487 0-1.6 1.438-2.694 3.546-2.694zM138.694 12.563v2.143h1.722v1.472h-1.722v4.99c0 .776.345 1.137 1.101 1.137.19 0 .492-.026.612-.043v1.463c-.206.052-.62.086-1.033.086-1.832 0-2.547-.688-2.547-2.444v-5.19h-1.317v-1.471h1.317v-2.143h1.867zM145.412 14.603c2.006 0 3.443 1.11 3.486 2.71h-1.747c-.077-.8-.757-1.29-1.79-1.29-1.007 0-1.678.464-1.678 1.17 0 .542.447.903 1.386 1.136l1.523.353c1.824.439 2.513 1.11 2.513 2.436 0 1.635-1.549 2.754-3.76 2.754-2.136 0-3.572-1.094-3.71-2.746h1.841c.13.869.826 1.334 1.954 1.334 1.11 0 1.808-.456 1.808-1.179 0-.56-.345-.86-1.291-1.102l-1.618-.395c-1.636-.397-2.462-1.231-2.462-2.487 0-1.6 1.437-2.694 3.546-2.694z"/></g><path fill="#FFF" d="M24.665 21.81c-.244.621-.809 1.496-1.61 2.112a5.27 5.27 0 0 1-1.77.92c-.809.24-1.804.321-3.042.321H6.92c-1.238 0-2.233-.08-3.041-.32a5.272 5.272 0 0 1-1.772-.92c-.8-.617-1.365-1.492-1.61-2.113C.006 20.558 0 19.138 0 18.243V6.92c0-.895.005-2.315.498-3.567.244-.621.809-1.496 1.61-2.112a5.271 5.271 0 0 1 1.77-.92C4.687.08 5.682 0 6.92 0h11.323c1.239 0 2.234.08 3.041.32.758.225 1.31.565 1.772.92.8.617 1.365 1.492 1.61 2.113.492 1.252.497 2.672.497 3.567v11.323c0 .895-.005 2.315-.498 3.567zm-10.259-7.347c-.377-.398-1.04-.653-1.823-.653-.783 0-1.447.255-1.824.653a1.157 1.157 0 0 0-.334.725c-.064.588-.028 1.094.04 1.903.066.771.191 1.8.354 2.847.115.746.21 1.148.295 1.436.139.467.657.875 1.469.875.81 0 1.33-.408 1.468-.875.086-.288.18-.69.296-1.436.162-1.047.287-2.075.352-2.847.07-.81.105-1.315.041-1.903a1.157 1.157 0 0 0-.334-.725zm-3.88-3.547a2.06 2.06 0 1 0 4.118 0 2.06 2.06 0 0 0-4.119 0zm2.033-8.127c-4.816.014-8.763 3.92-8.822 8.737-.049 3.901 2.442 7.238 5.92 8.462.084.03.17-.04.156-.13a50.475 50.475 0 0 1-.128-.906.304.304 0 0 0-.18-.24c-2.748-1.2-4.667-3.957-4.636-7.15.04-4.19 3.462-7.607 7.652-7.64 4.284-.035 7.78 3.44 7.78 7.716 0 3.16-1.91 5.883-4.638 7.075a.304.304 0 0 0-.178.24c-.04.299-.083.603-.128.906a.118.118 0 0 0 .156.129c3.445-1.212 5.92-4.497 5.92-8.35 0-4.888-3.983-8.863-8.874-8.85zm-.16 4.06a4.8 4.8 0 0 1 4.985 4.791c0 1.377-.583 2.62-1.515 3.495a.367.367 0 0 0-.116.288c.019.33.012.65-.01 1.011a.117.117 0 0 0 .182.104 5.926 5.926 0 0 0 2.592-4.898 5.934 5.934 0 0 0-6.163-5.923c-3.136.122-5.652 2.708-5.693 5.846a5.925 5.925 0 0 0 2.592 4.975.116.116 0 0 0 .181-.104 8.483 8.483 0 0 1-.01-1.01.367.367 0 0 0-.115-.288 4.783 4.783 0 0 1-1.514-3.624 4.809 4.809 0 0 1 4.604-4.664z"/></svg></a>
        <a href="https://open.spotify.com/show/5iyHPA5ZGvnj8moAwlir8I?si=05ec6ff9d18548f8" target="_blank" rel="noopener"
          aria-label="Spotify"><svg xmlns="http://www.w3.org/2000/svg" width="539" height="168" viewBox="0 0 539 168"><title>Spotify_Logo_RGB_White</title><g fill="#FFFFFE" fill-rule="evenodd"><path d="M133.532 74.477c-26.994-16.031-71.52-17.505-97.289-9.684-4.138 1.255-8.514-1.081-9.768-5.219a7.835 7.835 0 015.221-9.771c29.581-8.979 78.755-7.245 109.831 11.202a7.831 7.831 0 012.737 10.733c-2.208 3.722-7.019 4.949-10.732 2.739zm-.884 23.744c-1.893 3.073-5.911 4.036-8.98 2.15-22.505-13.834-56.822-17.841-83.447-9.759-3.453 1.043-7.1-.904-8.148-4.35a6.538 6.538 0 014.353-8.143c30.416-9.229 68.226-4.759 94.074 11.126 3.069 1.89 4.035 5.91 2.148 8.976zm-10.247 22.803a5.215 5.215 0 01-7.176 1.737c-19.666-12.019-44.418-14.734-73.568-8.075a5.217 5.217 0 01-6.249-3.925 5.212 5.212 0 013.925-6.249c31.9-7.293 59.264-4.154 81.337 9.334a5.22 5.22 0 011.731 7.178zM83.996.237C37.746.237.252 37.729.252 83.979c0 46.253 37.494 83.744 83.744 83.744 46.251 0 83.743-37.491 83.743-83.744 0-46.25-37.492-83.742-83.743-83.742zM228.089 77.546c-14.459-3.448-17.034-5.868-17.034-10.952 0-4.805 4.524-8.037 11.25-8.037 6.52 0 12.984 2.455 19.763 7.509a.945.945 0 00.715.174.933.933 0 00.625-.386l7.06-9.952a.949.949 0 00-.18-1.288c-8.067-6.473-17.151-9.62-27.769-9.62-15.612 0-26.517 9.369-26.517 22.774 0 14.375 9.407 19.465 25.663 23.394 13.836 3.187 16.171 5.856 16.171 10.63 0 5.289-4.722 8.577-12.321 8.577-8.439 0-15.324-2.843-23.025-9.512a.997.997 0 00-.695-.226.94.94 0 00-.649.334l-7.916 9.421a.94.94 0 00.093 1.313c8.961 7.999 19.98 12.225 31.872 12.225 16.823 0 27.694-9.193 27.694-23.42 0-12.024-7.184-18.674-24.8-22.958M303.162 93.661c0 10.153-6.254 17.238-15.209 17.238-8.853 0-15.531-7.407-15.531-17.238 0-9.83 6.678-17.238 15.531-17.238 8.811 0 15.209 7.248 15.209 17.238zM290.95 63.286c-7.292 0-13.273 2.872-18.205 8.757v-6.624a.949.949 0 00-.947-.949h-12.946a.948.948 0 00-.946.949v73.602c0 .523.423.949.946.949h12.946a.949.949 0 00.947-.949v-23.232c4.933 5.536 10.915 8.24 18.205 8.24 13.549 0 27.265-10.43 27.265-30.368 0-19.942-13.716-30.375-27.265-30.375zM353.373 111.005c-9.281 0-16.278-7.457-16.278-17.344 0-9.928 6.755-17.134 16.064-17.134 9.341 0 16.385 7.457 16.385 17.351 0 9.927-6.801 17.127-16.171 17.127zm0-47.719c-17.449 0-31.119 13.436-31.119 30.592 0 16.969 13.576 30.264 30.905 30.264 17.511 0 31.223-13.391 31.223-30.481 0-17.033-13.618-30.375-31.009-30.375zM421.644 64.47h-14.247V49.904a.946.946 0 00-.945-.948h-12.945a.95.95 0 00-.95.948V64.47h-6.225a.946.946 0 00-.943.949v11.127c0 .522.421.948.943.948h6.225v28.792c0 11.635 5.791 17.534 17.212 17.534 4.644 0 8.497-.959 12.128-3.018a.945.945 0 00.479-.821v-10.596a.951.951 0 00-1.372-.85c-2.494 1.255-4.905 1.834-7.6 1.834-4.153 0-6.007-1.885-6.007-6.112V77.494h14.247a.946.946 0 00.944-.948V65.419a.946.946 0 00-.944-.949M471.281 64.527v-1.789c0-5.263 2.018-7.61 6.544-7.61 2.699 0 4.867.536 7.295 1.346a.946.946 0 001.245-.902v-10.91a.948.948 0 00-.669-.909c-2.565-.762-5.847-1.546-10.761-1.546-11.959 0-18.279 6.734-18.279 19.467v2.74h-6.22a.952.952 0 00-.95.948v11.184c0 .522.428.948.95.948h6.22v44.41c0 .523.422.948.944.948h12.946a.95.95 0 00.949-.948v-44.41h12.088l18.517 44.398c-2.102 4.665-4.169 5.593-6.991 5.593-2.281 0-4.683-.681-7.139-2.025a.972.972 0 00-.754-.071.959.959 0 00-.56.512l-4.388 9.627a.941.941 0 00.407 1.225c4.581 2.481 8.717 3.54 13.827 3.54 9.56 0 14.844-4.454 19.503-16.434l22.461-58.04a.946.946 0 00-.879-1.292h-13.478a.951.951 0 00-.897.636L509.405 104.6l-15.123-39.463a.943.943 0 00-.884-.61h-22.117M442.505 64.47h-12.947a.95.95 0 00-.948.949v56.485c0 .523.425.948.948.948h12.947a.95.95 0 00.948-.948V65.419a.95.95 0 00-.948-.949M436.097 38.751c-5.128 0-9.291 4.153-9.291 9.282 0 5.131 4.163 9.288 9.291 9.288 5.127 0 9.285-4.157 9.285-9.288 0-5.129-4.158-9.282-9.285-9.282"/></g></svg></a>
        <a href="https://castbox.fm/channel/Small-Business%2C-Big-Lessons-id4610904?country=us" target="_blank" rel="noopener"
          aria-label="CastBoxFm"><svg width="105" height="40" viewBox="0 0 105 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0.00508723 20.0079L8.75882e-05 11.6349C-0.00791241 10.3549 0.532087 9.44088 1.62809 8.79488L15.5911 0.524883C16.7571 -0.171117 17.8471 -0.177117 19.0141 0.519883L33.0311 8.81588C34.1051 9.44888 34.6361 10.3789 34.6371 11.6129L34.6381 28.3589C34.6381 29.5889 34.1251 30.5269 33.0381 31.1629L18.9681 39.4929C17.8481 40.1589 16.7681 40.1749 15.6531 39.5049L1.65309 31.2019C0.533087 30.5419 -0.00391244 29.6019 0.00708756 28.3079L0.0140875 20.0079H0.00508723ZM20.8851 19.9079L20.8811 16.0679C20.8741 15.3459 20.4511 14.8819 19.8061 14.8329C19.0521 14.7759 18.5061 15.2489 18.4861 16.0199L18.4761 18.5399C18.4661 19.0839 18.1111 19.3669 17.6191 19.2599C17.2141 19.1599 17.1071 18.8819 17.1191 18.5069L17.1231 15.1699C17.1251 14.6999 16.9961 14.2999 16.5761 14.0399C15.7211 13.5139 14.7301 14.0529 14.7021 15.0779L14.6921 17.7859C14.6851 18.2819 14.4601 18.5199 14.0381 18.5359C13.5951 18.5509 13.3211 18.2889 13.2921 17.7919L13.2851 16.8479C13.2631 16.3279 12.9991 15.9799 12.5191 15.8109C12.3377 15.7392 12.1413 15.7137 11.9476 15.7365C11.7539 15.7593 11.5688 15.8298 11.409 15.9417C11.2492 16.0535 11.1196 16.2033 11.0319 16.3775C10.9441 16.5517 10.9009 16.7449 10.9061 16.9399L10.8961 19.3329C10.8861 19.7679 10.6291 20.0059 10.2361 20.0179C9.83109 20.0299 9.57609 19.8179 9.51809 19.3849C9.50109 19.2609 9.51809 19.1319 9.50309 19.0079C9.42809 18.3859 8.90809 17.9129 8.31609 17.9199C7.71609 17.9269 7.14809 18.3999 7.13209 19.0199V22.7979C7.14909 23.4159 7.71609 23.8899 8.31209 23.8979C8.91909 23.8959 9.41209 23.4379 9.50009 22.8109C9.51809 22.6659 9.46309 22.4839 9.53209 22.3779C9.67009 22.1779 9.83209 21.9049 10.0541 21.8359C10.2391 21.7759 10.5571 21.8959 10.7111 22.0439C10.8491 22.1769 10.8911 22.4569 10.8941 22.6739L10.9071 26.3889C10.9201 27.2939 11.8521 27.8519 12.6521 27.4489C13.1071 27.2189 13.2981 26.8489 13.2921 26.3189L13.2871 21.4069C13.2881 20.6429 13.5171 20.3009 14.0131 20.3069C14.4881 20.3129 14.6931 20.6319 14.6951 21.3669L14.6981 23.5709C14.7131 24.3359 15.1981 24.8279 15.8981 24.8349C16.6181 24.8429 17.1131 24.3289 17.1281 23.5409L17.1331 21.8409C17.1431 21.3259 17.3991 21.0429 17.8331 21.0409C18.2671 21.0389 18.5031 21.3409 18.5101 21.8439L18.5181 23.7959C18.5421 24.5029 19.0581 24.9839 19.7351 24.9729C20.4331 24.9629 20.9051 24.4689 20.9121 23.6999L20.9151 19.9199L20.8851 19.9079ZM24.6891 21.2429L24.6871 19.1029C24.6771 18.3759 24.2271 17.8979 23.5451 17.8709C22.8331 17.8429 22.3021 18.2569 22.2851 18.9789L22.2931 23.5069C22.3131 24.2089 22.8891 24.6709 23.5481 24.6329C24.2301 24.5929 24.6761 24.1129 24.6881 23.3809L24.6891 21.2409V21.2429ZM26.0891 21.8379L26.0901 22.4029C26.0903 22.6988 26.2066 22.9828 26.4139 23.1939C26.6213 23.405 26.9032 23.5264 27.1991 23.5319C27.8721 23.5689 28.4051 23.1599 28.4691 22.5019C28.5107 22.0642 28.5104 21.6235 28.4681 21.1859C28.4061 20.5359 27.8481 20.0859 27.2061 20.1359C26.5841 20.1739 26.1261 20.6359 26.0901 21.2739C26.0801 21.4619 26.0891 21.6509 26.0891 21.8389V21.8379Z" fill="white"/>
<path d="M82.1371 19.2889C83.5721 19.9749 84.2841 21.0859 84.2671 22.6519C84.2471 24.3119 83.0531 25.8019 81.4171 26.1119C80.7221 26.2419 80.0001 26.2549 79.2891 26.2749L76.5531 26.2809V13.3219C78.0661 13.3719 79.6031 13.0959 81.0661 13.6869C83.0281 14.4789 83.7311 17.2009 82.4431 18.8819L82.1381 19.2899L82.1371 19.2889ZM78.5401 24.3859L80.2881 24.3799C80.5151 24.3729 80.7451 24.3179 80.9641 24.2529C81.7421 24.0229 82.2491 23.3729 82.2641 22.5999C82.2911 21.7239 81.9141 21.0879 81.1501 20.8279C80.3131 20.5419 79.4431 20.4949 78.5301 20.5319V24.3859H78.5401ZM78.5301 18.8499C79.4901 18.8859 80.4501 18.9749 80.9601 18.0099C81.3361 17.2969 81.3601 16.4839 80.8431 15.8069C80.2591 15.0419 79.3851 15.1539 78.5311 15.1429V18.8489L78.5301 18.8499ZM52.1301 23.2199V25.4799C50.4831 26.7339 46.4861 27.2369 43.8281 24.5159C41.4041 22.0359 41.2531 18.2219 43.4811 15.4699C45.7841 12.6249 49.7611 12.4499 52.1381 13.9959V16.2699L51.4961 15.8499C49.9011 14.8149 48.2291 14.5499 46.4911 15.4419C44.1151 16.6479 43.1961 19.9089 44.5471 22.2389C45.9201 24.6069 48.8621 25.3229 51.2121 23.8549L52.1301 23.2189V23.2199ZM62.1631 26.2619H60.2681L60.2181 25.3189C60.1261 25.3659 60.0651 25.3829 60.0241 25.4209C58.2741 27.0289 54.8241 26.5379 53.9941 23.2259C53.6261 21.7629 53.7941 20.3509 54.7341 19.0959C55.9671 17.4309 58.3741 17.0939 59.8991 18.4489C59.9761 18.5169 60.0611 18.5759 60.2071 18.6889L60.2671 17.6609H62.1671L62.1681 26.2609L62.1631 26.2619ZM60.0991 21.9769C60.1001 20.6349 59.0691 19.5169 57.8291 19.5169C56.6351 19.5179 55.5841 20.6409 55.5691 21.9339C55.5531 23.2569 56.6071 24.3879 57.8491 24.3819C59.0721 24.3749 60.0971 23.2799 60.0991 21.9769V21.9769ZM90.1291 26.2819C87.5611 26.2769 85.6991 24.3639 85.7091 21.7439C85.7191 19.3199 87.7261 17.3839 90.2091 17.3969C92.7091 17.4099 94.6791 19.3769 94.6861 21.8669C94.6931 24.3669 92.7161 26.2869 90.1201 26.2809L90.1291 26.2819ZM90.2291 24.2819C91.5891 24.2719 92.6361 23.1999 92.6291 21.8249C92.6211 20.4989 91.4651 19.3229 90.1771 19.4029C88.7141 19.4949 87.7931 20.5079 87.7501 21.8799C87.7101 23.1829 88.8981 24.2919 90.2301 24.2819H90.2291ZM95.7091 17.6579H98.1351L100.027 20.1079L101.957 17.6509H104.463L101.298 21.6049L104.94 26.2449H102.52L100.04 23.1089L97.4871 26.2489H94.9871L98.7891 21.6089L95.7091 17.6589V17.6579ZM68.7931 20.1719H66.9391L66.7361 19.8119C66.5561 19.5549 66.2791 19.4469 66.0281 19.6119C65.8481 19.7319 65.6811 19.9849 65.6581 20.1959C65.6251 20.4799 65.8181 20.6959 66.1381 20.7559L66.8831 20.8559C68.2231 21.1499 69.1251 22.4259 68.9751 23.8029C68.8191 25.2369 67.6931 26.2629 66.2751 26.2699C64.8771 26.2779 63.6951 25.2669 63.5251 23.9119C63.5101 23.7919 63.5231 23.6719 63.5231 23.5269H65.2771L65.4421 23.9149C65.6721 24.3399 66.0681 24.5199 66.4901 24.4149C66.8721 24.3099 67.1821 23.9069 67.1701 23.5289C67.1571 23.0789 66.8281 22.7289 66.3461 22.6329L65.6661 22.5179C64.3501 22.2039 63.6661 21.3179 63.7311 20.0449C63.7951 18.7819 64.7451 17.7499 65.9611 17.6249C67.1961 17.4979 68.3171 18.2319 68.6681 19.4119C68.7351 19.6419 68.7531 19.8879 68.8021 20.1719H68.7931ZM73.4631 15.1289V18.0689L74.5471 18.1389V19.8459L73.4621 19.8959V26.2359H71.5681V19.9089L70.3981 19.8409V18.1349L71.5381 18.0699V15.1299L73.4631 15.1289Z" fill="white"/>
</svg>
</a>
      </div>
    </div>
  </div>
</div>
<div class="bf-homefeed gh-page">
  <div class="gh-container bf-tab" x-data="tabbedListBottom()" x-init="init()">

    <div class="bf-scroll-nav-wrapper">
      <nav class="bf-scroll-nav">
        <a href="javascript:" :class="{ 'active': activeTab === 'flow'}" @click="changeTab('flow')"
          @mouseover="loadContent('flow')">
          Flow
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'breakingbrand'}" @click="changeTab('breakingbrand')"
          @mouseover="loadContent('breakingbrand')">
          Breaking Brand
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'social'}" @click="changeTab('social')"
          @mouseover="loadContent('social')">
          Science of Social Media
        </a>
        <a href="javascript:" :class="{ 'active': activeTab === 'overflow'}" @click="changeTab('overflow')"
          @mouseover="loadContent('overflow')">
          Overflow
        </a>
      </nav>
    </div>
    <div x-show="activeTab == 'flow'">
      <div id="flow-banner" class="bf-tab-banner">
        <img class="bf-banner-logo" src="https://buffer.com/resources/assets/img/flow.svg?v=5ec3319331" alt="Flow" loading="lazy" />
        <p class="bf-banner-desc"></p>
      </div>
      <div id="flow-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'breakingbrand'">
      <div id="breakingbrand-banner" class="bf-tab-banner">
        <img class="bf-banner-logo" src="https://buffer.com/resources/assets/img/breakingbrand.svg?v=5ec3319331" alt="Breaking Brand" loading="lazy" />
        <p class="bf-banner-desc"></p>
      </div>
      <div id="breakingbrand-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'social'">
      <div id="social-banner" class="bf-tab-banner">
        <img class="bf-banner-logo" src="https://buffer.com/resources/assets/img/social.svg?v=5ec3319331" alt="The Science of Social Media" loading="lazy" />
        <p class="bf-banner-desc"></p>
      </div>
      <div id="social-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
    <div x-show="activeTab == 'overflow'">
      <div id="overflow-banner" class="bf-tab-banner">
        <img class="bf-banner-logo" src="https://buffer.com/resources/assets/img/overflow.svg?v=5ec3319331" alt="Overflow" loading="lazy" />
        <p class="bf-banner-desc"></p>
      </div>
      <div id="overflow-content" class="gh-postfeed">
        <div class="bf-loader"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
    y="0px" width="40px" height="40px" viewBox="0 0 40 40" enable-background="new 0 0 40 40" xml:space="preserve">
    <path opacity="0.2" fill="#000" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z" />
    <path fill="#000" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
C22.32,8.481,24.301,9.057,26.013,10.047z">
        <animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 20 20" to="360 20 20"
            dur="0.5s" repeatCount="indefinite" />
    </path>
</svg></div>
      </div>
    </div>
  </div>
</div>
    </main>
    <div class="bf-maincta">
      <div class="bf-maincta-container">
        <div class="bf-maincta-content bf-cta-content">
          <div class="bf-maincta-logos">
            <div id="food52-logo" class="bf-maincta-logo"><svg width="100" height="22" viewBox="0 0 100 22" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M88.36 17.99l3.308-2.91c3.607-3.092 6.011-5.818 6.011-9.066 0-3.65-3.329-5.282-6.627-5.282-4.017 0-5.514 1.988-5.514 3.24 0 .89.648 1.562 1.51 1.562.88 0 1.477-.562 1.635-1.544l.03-.187c.17-1.092.345-2.222 2.314-2.222 2.142 0 3.14 1.392 3.14 4.38 0 2.949-1.095 5.282-4.04 8.609l-5.535 6.312h12.681c.611 0 .741-.21.956-.805l.78-2.086H88.36zM77.991 7.816c-1.407.023-2.903.5-3.944 1.153l.637-5.161 7.826-.123c.542-.01.654-.213.837-.79l.616-1.878-9.678.01-1.19 8.95.271.197.022.017.242.175.162-.154c.725-.687 2.045-1.512 4.213-1.547 3.047-.048 3.554 3.256 3.586 5.23.048 3.054-1.037 6.336-4.228 6.387-2.269.036-2.424-1.068-2.604-2.345l-.042-.29c-.184-.873-.768-1.368-1.605-1.355-.83.014-1.448.639-1.435 1.455.031 1.948 2.534 3.434 5.7 3.384 4.542-.072 7.687-3.06 7.647-7.265-.072-4.547-3.834-6.1-7.033-6.05zM67.512 10.7c0-7.635-4.508-8.88-8.69-8.88h-.7v18.344h.7c5.718 0 8.69-2.878 8.69-9.464zm3.557.026c0 6.39-4.87 10.056-12.247 10.056H53.47v-.21l.193-.054c1.033-.295 1.13-.983 1.13-6.232V7.648c0-5.068-.09-5.87-1.043-6.204l-.014-.002h.007c-.028-.01-.057-.02-.085-.028l-.188-.057v-.181h5.352c7.486 0 12.247 3.39 12.247 9.549zm-27.577 9.882c3.37 0 5.993-2.875 5.993-9.564 0-6.687-2.789-9.485-5.993-9.485s-5.994 2.798-5.994 9.486c0 6.689 2.624 9.563 5.994 9.563zm9.568-9.564c0 6.26-4.967 10.134-9.568 10.134-4.602 0-9.569-3.874-9.569-10.134 0-4.835 3.66-10.056 9.568-10.056 5.91 0 9.57 5.22 9.57 10.057v-.001zm-30.234 9.564c3.37 0 5.993-2.874 5.993-9.563 0-6.688-2.79-9.486-5.993-9.486-3.203 0-5.993 2.798-5.993 9.486 0 6.689 2.624 9.563 5.993 9.563zm9.568-9.563c0 6.259-4.967 10.134-9.568 10.134-4.6 0-9.568-3.875-9.568-10.134 0-4.836 3.658-10.057 9.567-10.057 5.911 0 9.57 5.22 9.57 10.057zM5.012 1.969v7.467l2.684.02c2.51 0 2.504-1.151 2.742-2.585h.226v6.097h-.226c-.238-1.435-.233-2.587-2.74-2.587l-2.685.019v3.969c0 5.27.095 5.958 1.125 6.23l.196.053v.213H.361v-.213l.197-.052c1.03-.273 1.125-.961 1.125-6.231V7.73c0-5.271-.096-5.958-1.125-6.231l-.197-.053V1.26H12.83c.491 0 .656.179.771.83l.426 2.803h-.292l-.023-.055c-.7-2.124-1.97-2.87-5.23-2.87H5.01h.001z" fill="currentcolor"/>
</svg>
</div>
            <div id="burrow-logo" class="bf-maincta-logo"><svg width="105" height="16" viewBox="0 0 105 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M95.06 7.482c-.177.402-.322.723-.46 1.046-.936 2.19-1.875 4.376-2.796 6.572-.128.307-.275.436-.623.428-1.013-.026-2.027-.017-3.042-.004-.25.003-.376-.075-.46-.319-1.352-3.904-1.957-7.909-1.652-12.037.07-.95.178-1.899.27-2.87h3.063c-.726 4.075-.57 8.103.634 12.105.085-.189.173-.377.254-.567 1.197-2.79 2.396-5.579 3.58-8.374.119-.28.26-.384.565-.372.597.025 1.196.008 1.799.008 1.336 3.127 2.663 6.23 3.988 9.334 1.2-3.999 1.381-8.029.64-12.134h2.974c.105 1.287.256 2.574.306 3.864.146 3.762-.445 7.416-1.682 10.971-.102.29-.226.4-.538.393-.985-.02-1.971-.023-2.956.001-.34.01-.5-.102-.63-.416-.981-2.355-1.984-4.702-2.98-7.05-.07-.166-.144-.329-.253-.579zM2.897 6.52c2.202 0 4.255.035 6.306-.015 1.016-.024 1.603-.758 1.605-1.796.001-1.034-.596-1.773-1.6-1.801-1.838-.052-3.679-.028-5.518-.023-.093 0-.256.107-.268.184-.184 1.132-.348 2.267-.525 3.45zm.078 2.571c.025 1.283.152 2.493.453 3.68.021.086.234.173.359.174 1.755.01 3.509.01 5.264.003.211-.001.426-.04.634-.082 1.004-.21 1.486-.852 1.466-1.941-.018-.923-.614-1.611-1.549-1.763-.28-.046-.567-.067-.851-.068-1.74-.006-3.48-.003-5.221-.003h-.555zM.984.269h1.091c2.314 0 4.628-.025 6.941.015.746.014 1.515.116 2.229.327 1.428.423 2.363 1.403 2.595 2.892.247 1.582-.091 3.012-1.433 4.06-.078.061-.158.12-.26.199.079.063.136.123.205.162 1.418.804 2.015 2.056 1.922 3.642-.1 1.686-.941 2.907-2.534 3.476-.778.279-1.635.438-2.461.456-2.641.056-5.284.016-7.926.028-.3 0-.419-.094-.488-.381C.186 12.31-.102 9.439.032 6.528c.096-2.1.394-4.172.952-6.26zm52.66 7.247c.098.011.166.026.235.027 1.64.001 3.28.018 4.92-.01.434-.008.877-.12 1.293-.254.529-.169.886-.549 1.066-1.087.523-1.57-.223-2.855-1.84-3.147-.25-.045-.51-.06-.764-.062-1.114-.007-2.227-.003-3.339-.003h-1.113c-.385 1.513-.534 3.001-.458 4.536zm8 2.034l3.218 5.966c-1.104 0-2.128.013-3.151-.015-.127-.004-.291-.198-.368-.34-.825-1.534-1.644-3.068-2.44-4.615-.172-.336-.367-.463-.752-.454-1.286.027-2.57.01-3.856.01H53.7l.933 5.39c-.066.006-.184.025-.304.025-.614.003-1.229.002-1.843.002-.877 0-.879 0-1.056-.837-.58-2.748-.842-5.526-.748-8.332.066-1.96.386-3.885.883-5.78.056-.215.127-.307.364-.306 2.428.015 4.855-.002 7.282.038.633.011 1.28.132 1.892.304 2.482.702 3.456 2.68 3.282 4.994-.13 1.728-.981 2.971-2.483 3.794-.075.041-.145.087-.258.156zM37.61 3.062c-.018.06-.069.165-.08.275-.143 1.287-.277 2.574-.417 3.862-.033.301.124.352.384.35 1.185-.009 2.37.005 3.555-.008.64-.007 1.285-.017 1.92-.088.628-.069 1.187-.323 1.535-.895.86-1.417.063-3.327-1.574-3.464-1.74-.144-3.503-.032-5.323-.032zM35.055.35c2.895 0 5.636-.067 8.372.022 2.107.07 3.802 1.363 4.27 3.128.587 2.225.138 4.613-2.293 5.901-.075.04-.142.091-.24.155l3.194 5.917c-.163.02-.268.043-.373.044-.87.003-1.742-.006-2.613.006-.245.004-.375-.079-.49-.3-.83-1.594-1.683-3.175-2.51-4.768-.139-.265-.296-.363-.595-.36-1.34.016-2.683.007-4.025.008-.139 0-.277.013-.529.026l.933 5.39h-2.179c-.84 0-.839 0-1.018-.825-.705-3.242-.964-6.52-.649-9.822.147-1.539.498-3.058.745-4.522zm45.369 8.031c-.01-2.475-.734-4.054-2.542-5.01-.981-.518-2.046-.69-3.148-.646-2.402.096-4.836 1.458-5.122 4.578-.155 1.687.179 3.247 1.48 4.46.929.863 2.078 1.217 3.313 1.316 3.174.255 6.087-1.45 6.019-4.698zm-5.398 7.447c-2.026-.054-3.905-.528-5.55-1.746-1.58-1.17-2.491-2.75-2.808-4.68-.237-1.446-.163-2.875.316-4.262.744-2.158 2.234-3.626 4.345-4.43 2.513-.959 5.062-.95 7.556.051 2.852 1.145 4.309 3.36 4.553 6.378.13 1.614-.066 3.195-.838 4.654-1.154 2.184-3.064 3.313-5.414 3.78-.71.14-1.44.173-2.16.255zM20.224.29c-.143.883-.297 1.693-.398 2.51-.271 2.172-.436 4.35.04 6.515.22 1.005.648 1.911 1.377 2.663 1.607 1.66 5.213 1.726 6.622-1.326.582-1.26.733-2.602.754-3.962.032-2.063-.224-4.099-.628-6.118-.014-.068-.024-.136-.046-.253.159-.01.293-.029.427-.029.7-.003 1.401.024 2.1-.01.394-.02.541.115.615.492.43 2.181.602 4.382.502 6.6-.063 1.398-.245 2.78-.727 4.111-.854 2.36-2.507 3.762-4.98 4.162-1.364.221-2.735.211-4.085-.099-2.378-.546-3.835-2.075-4.572-4.35-.614-1.903-.738-3.87-.63-5.84.087-1.562.356-3.113.535-4.67.034-.295.15-.412.463-.405.855.021 1.71.008 2.63.008z" fill="currentcolor"/>
</svg>
</div>
            <div id="dressup-logo" class="bf-maincta-logo"><svg width="102" height="27" viewBox="0 0 102 27" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 20.73V.012C.072.008.131.003.192.003c2.287 0 4.575-.008 6.863.003 1.282.006 2.517.256 3.684.803 1.228.577 2.234 1.43 3.082 2.478 1.151 1.425 1.86 3.046 2.164 4.85.219 1.3.239 2.605.076 3.912-.31 2.483-1.298 4.641-3.118 6.385-1.223 1.172-2.682 1.885-4.353 2.165-.579.098-1.163.138-1.748.14-2.206.002-4.411 0-6.616 0-.073 0-.147-.007-.226-.01zm1.163-1.189c.068.004.11.008.15.008 1.908 0 3.816.005 5.725-.003.74-.004 1.467-.119 2.174-.345 1.559-.498 2.808-1.44 3.826-2.7 1.12-1.388 1.676-3.004 1.865-4.76.12-1.114.1-2.227-.078-3.336-.25-1.55-.823-2.965-1.782-4.216-.644-.84-1.402-1.553-2.327-2.078-1.147-.652-2.391-.937-3.7-.946-1.888-.01-3.775-.003-5.663-.003-.061 0-.12.007-.192.011.002 6.125.002 12.24.002 18.368zm88.711-.968v7.79c-.201.021-.391.008-.581.01-.193.003-.385.001-.564.001l-.028-.026c-.004-.005-.011-.01-.012-.015-.004-.027-.01-.054-.01-.082l.002-17.424c0-.019.01-.038.018-.07h1.166v2.188c.11-.03.143-.11.19-.168.53-.638 1.149-1.168 1.889-1.55 1.005-.519 2.08-.699 3.2-.649.899.04 1.766.23 2.557.664 1.729.951 2.839 2.377 3.191 4.335.238 1.325.134 2.635-.468 3.854-.947 1.918-2.48 3.104-4.61 3.433-1.411.218-2.774.022-4.035-.694-.66-.374-1.223-.866-1.717-1.44l-.15-.169-.038.012zM94.8 9.728c-2.866-.03-5.031 2.401-5.027 5.037.003 2.703 2.35 5.03 5.043 5.025 2.758-.005 5.03-2.313 5.027-5.046-.003-2.669-2.288-5.057-5.043-5.016zM70.883.007h1.143c.006.056.016.11.017.161.002.227 0 .454 0 .682 0 4.872.002 9.743-.001 14.615 0 .493.043.977.192 1.448.309.98.956 1.674 1.833 2.174.626.356 1.306.547 2.018.623.85.09 1.693.05 2.517-.198.928-.277 1.719-.769 2.327-1.532.454-.57.696-1.23.757-1.956.02-.246.027-.495.027-.743.002-4.996 0-9.99 0-14.988V.014H82.9V15.5c0 .73-.087 1.445-.366 2.124-.561 1.37-1.57 2.291-2.925 2.841-.994.403-2.04.502-3.103.465-.947-.033-1.86-.22-2.715-.634-1.103-.533-1.955-1.324-2.464-2.456-.263-.585-.395-1.2-.433-1.84-.012-.199-.01-.399-.01-.599V.29l-.001-.282zM42.489 14.496H31.275c0 .115-.002.21 0 .303.021.728.136 1.44.409 2.12.559 1.39 1.56 2.295 3.009 2.684 1.094.293 2.194.278 3.288-.012.752-.199 1.393-.593 1.911-1.17.271-.302.504-.636.754-.956.041-.054.077-.112.124-.18l1.061.488c-.042.083-.073.15-.111.213-.963 1.65-2.408 2.594-4.277 2.896-1.11.18-2.212.11-3.285-.248-1.963-.655-3.518-2.417-3.911-4.449-.256-1.326-.215-2.644.304-3.9.798-1.93 2.241-3.145 4.283-3.589 1.381-.3 2.764-.232 4.078.326 1.773.753 2.956 2.048 3.426 3.947.112.457.155.923.163 1.392.003.034-.004.067-.012.135zm-11.022-1.15h9.688c0-.036.003-.057-.001-.076-.129-.646-.386-1.235-.805-1.746-.586-.715-1.33-1.212-2.199-1.518-1.006-.357-2.037-.38-3.077-.184-.794.15-1.505.482-2.109 1.025-.738.664-1.191 1.506-1.493 2.437-.005.018-.003.04-.004.061zM53.68 9.97l-.855.74c-.03-.024-.059-.04-.082-.062-.756-.709-1.669-.963-2.678-.905-.267.015-.536.062-.79.142-.61.193-.951.632-1.04 1.262-.029.203-.04.414-.02.617.05.536.326.941.768 1.236.405.27.852.45 1.306.61.747.262 1.49.538 2.194.904.355.186.69.398.972.69.53.547.81 1.205.86 1.962.026.414.006.826-.102 1.23-.172.647-.526 1.176-1.038 1.604-.681.572-1.47.885-2.352.953-.794.062-1.57-.027-2.31-.338-1.023-.43-1.736-1.189-2.282-2.163.32-.216.657-.399.998-.61.038.054.072.102.104.152.181.302.39.583.636.837.512.531 1.133.845 1.868.916.58.056 1.156.05 1.723-.103.08-.02.158-.046.236-.074.797-.286 1.215-.867 1.316-1.693.033-.274.047-.552-.016-.822-.16-.675-.54-1.202-1.166-1.495-.642-.3-1.313-.533-1.968-.8-.395-.16-.79-.322-1.179-.5-.21-.097-.413-.22-.608-.348-.706-.46-1.066-1.129-1.145-1.959-.037-.374-.04-.748.07-1.107.37-1.189 1.175-1.953 2.386-2.185 1.55-.297 2.931.12 4.097 1.203.029.025.053.057.096.106zm5.197 7.87c.047.073.08.133.12.188.165.228.32.468.504.68.503.575 1.127.938 1.9 1.026.613.071 1.223.066 1.823-.096.663-.179 1.17-.55 1.401-1.222.072-.206.113-.427.14-.644.093-.804-.2-1.46-.812-1.973-.146-.122-.316-.225-.49-.297-.617-.257-1.242-.49-1.859-.745-.446-.182-.888-.372-1.324-.576-.198-.092-.385-.216-.565-.343-.583-.412-.906-.987-1.017-1.685-.063-.398-.082-.799.02-1.19.301-1.178 1.071-1.907 2.212-2.269 1.657-.34 3.11.046 4.344 1.215.014.013.022.033.044.067l-.847.735c-.036-.028-.069-.05-.097-.076-.748-.693-1.648-.94-2.645-.895-.218.011-.44.043-.652.097-.75.192-1.16.704-1.225 1.474-.067.807.25 1.402.951 1.8.391.222.805.388 1.23.534.74.258 1.475.533 2.165.912.235.128.466.271.671.441.697.577 1.043 1.335 1.097 2.232.022.373-.007.743-.096 1.107-.15.621-.469 1.143-.944 1.57-.712.64-1.553.983-2.504 1.05-.65.045-1.294-.013-1.919-.214-.896-.288-1.609-.83-2.168-1.58-.165-.22-.308-.455-.476-.708.342-.218.677-.41 1.018-.616zm-35.973 2.885h-1.175V8.756h1.165c.024.507 0 1.013.015 1.56.05-.06.08-.089.103-.124.24-.38.532-.72.863-1.024.419-.385.904-.575 1.482-.573.99.001 1.863.315 2.652.941-.204.32-.412.64-.625.971-.08-.05-.148-.095-.215-.139-.546-.359-1.134-.588-1.796-.609-.388-.012-.732.102-1.044.327-.506.365-.86.848-1.108 1.414-.213.485-.32.991-.319 1.525.005 2.474.002 4.948.002 7.422v.278z" fill="currentcolor"/>
</svg>
</div>
            <div id="huckberry-logo" class="bf-maincta-logo"><svg width="114" height="19" viewBox="0 0 114 19" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M20.83 1.064c.348 1.025.522 2.089.522 3.172V6.42h-5.473V.735h-4.41l.117.329c.348 1.025.522 2.108.522 3.19V15.26h3.77V9.554h5.474v5.705h3.77V.735h-4.408l.116.329zM43.205 5.9c1.16 0 1.72.637 1.895 2.107l3.346-.193c-.174-1.335-.464-2.012-1.257-2.882-1.006-1.083-2.36-1.644-4.12-1.644-3.597 0-6.014 2.476-6.014 6.17 0 3.616 2.32 6.014 5.82 6.014 1.974 0 3.5-.657 4.526-1.992.619-.754.87-1.373 1.025-2.63l-3.345-.193c-.213 1.373-.871 2.011-1.992 2.011-1.431 0-2.012-.967-2.012-3.326 0-2.34.658-3.443 2.128-3.443zm-10.463 4.234c0 .619.058 1.412-.33 1.934-.367.484-.985.793-1.585.793-.91 0-1.316-.483-1.316-1.508V3.54h-3.364v7.813c0 1.644.155 2.224.658 2.939.599.851 1.681 1.122 2.648 1.18 1.277.097 2.883-.155 3.655-1.315.117.464.272 1.025.292 1.102h2.764V3.54l-3.462.019.04 6.575zM60.88 3.54h-3.5s-4.41 5.105-4.641 5.376V.735h-4.022l.116.349c.348 1.025.522 2.088.522 3.17V15.28h3.365v-3.017l2.089-2.321 2.533 5.318h3.965l-3.965-7.735L60.88 3.54zm29.088 2.204V3.54H86.68v11.72h3.48v-4.777c0-2.437 1.007-3.733 3.54-3.733V3.288c-1.47 0-3.23.793-3.732 2.456zm8.103 0V3.54h-3.288v11.72h3.482v-4.777c0-2.437 1.005-3.733 3.539-3.733V3.288c-1.47 0-3.21.793-3.733 2.456zm12.667-2.204l-2.244 6.652-2.224-6.652h-3.655l4.216 11.719-1.083 3.346h2.804c.329-.947 4.564-13.499 5.106-15.085h-2.92v.02zm-41.831-.213c-1.276 0-2.224.483-2.998 1.702V.735h-4.216l.116.349c.35 1.025.523 2.088.523 3.152v11.023h2.843c0-.02.174-.638.31-1.141.831 1.045 1.643 1.374 3.035 1.374 3.075 0 4.893-2.283 4.893-6.15.02-3.694-1.72-6.015-4.506-6.015zm.87 6.749c-.038.56-.135 1.238-.367 1.818-.29.697-.793 1.219-1.663 1.219-1.14 0-1.857-.93-1.857-2.476V8.703c0-1.682.716-2.746 1.895-2.746 2.05-.02 2.09 2.669 1.992 4.119zM85.829 10c-.02-2.07-.271-3.037-.986-4.198-.91-1.527-2.727-2.475-4.758-2.475-3.481 0-5.86 2.533-5.86 6.19 0 3.576 2.399 5.975 5.996 5.975 1.779 0 3.075-.503 4.138-1.586.6-.619.929-1.14 1.277-2.128l-3.23-.212c-.31.967-1.006 1.49-2.07 1.49-1.411 0-2.34-1.007-2.34-2.515 0-.097 0-.349.02-.542h7.813zm-5.57-4.43c1.296 0 1.896.716 2.05 2.398h-4.293c.174-1.624.89-2.398 2.243-2.398zm-73.49.31l-.309-.387.406.271c.909.58 1.818 1.102 2.707 1.547.174-.619.31-1.257.348-1.915C7.117 2.94 5.667.658 5.28 0 4.893.658 3.462 2.94.638 5.396c.058.638.174 1.277.348 1.915.89-.445 1.799-.967 2.708-1.547l.406-.271-.309.387C2.688 7.233 1.412 8.51 0 9.67c.019.677.116 1.354.29 2.012 1.663-.619 3.133-1.335 4.97-2.321l-1.585 1.895v.136c0 1.315-.213 2.63-.639 3.867h4.468c-.426-1.257-.638-2.552-.638-3.867v-1.18c.947.483 1.934.928 3.365 1.489.154-.658.251-1.334.29-2.011-1.393-1.18-2.65-2.457-3.752-3.81z" fill="currentcolor"/>
</svg>
</div>
            <div id="happysocks-logo" class="bf-maincta-logo"><svg width="88" height="36" viewBox="0 0 88 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M36.391 17.615c-.54-.377-1.235-.456-1.846-.21-.683.351-1.224.93-1.529 1.634l.264-2.426c.002-.017.002-.035 0-.052.006-.053.006-.106 0-.158 0-.083-.039-.162-.106-.21-.13-.077-.291-.077-.421 0-.556.242-.94.766-1.002 1.37-.511 3.633-.758 7.3-.739 10.968-.001 1.654.07 3.308.211 4.956.03.827.582 1.548 1.371 1.793.141.05.298.031.422-.052.092-.099.132-.237.106-.37-.261-2.804-.384-5.62-.369-8.437l.21.16c.625.413 1.416.492 2.11.21 1.16-.528 2.109-1.793 2.531-3.692.633-2.636.158-4.745-1.16-5.589l-.053.105zm-.316 4.746c-.264 1.582-.897 2.795-1.688 3.164-.203.132-.452.17-.685.105-.528-.158-.791-1.054-.686-2.214.158-2.268 1.055-3.902 1.951-4.588.176-.149.403-.224.633-.21.264.105.844 1.581.422 3.69l.053.053zm20.143-3.164l-.686-.422c-3.533-2.214-7.962-5.062-8.067-8.753.006-1.832.725-3.59 2.003-4.904 1.21-1.277 2.882-2.018 4.641-2.056 1.3-.052 2.564.446 3.48 1.371 1.123 1.153 1.732 2.714 1.687 4.324-.05 1.417-.508 2.79-1.318 3.954-.211.264-.211.528-.105.528.165.165.409.226.632.158 1.688-.21 3.059-2.53 3.059-5.168 0-3.058-1.951-6.644-7.224-6.644-2.442-.02-4.795.928-6.539 2.637-1.533 1.5-2.407 3.55-2.426 5.695 0 4.745 4.43 7.54 8.015 9.808l1.582 1.054c2.795 1.846 4.061 3.164 3.164 5.01-.685 1.582-3.269 1.898-5.273 1.687-2.004-.21-4.588-.896-5.062-3.269-.106-.528-.369-.528-.527-.528-.37 0-.528.528-.633 1.055-.057.987.285 1.957.949 2.69 1.055 1.16 2.637 1.792 4.904 1.898 2.478.158 5.8-.528 7.066-3.059 1.055-1.898 1.371-4.218-3.269-7.17l-.053.104zM15.72 18.143c.624.013 1.208-.31 1.53-.844.061-.075.098-.167.105-.264-.005-.056-.023-.11-.053-.158-.079-.16-.243-.262-.422-.264-.401-.066-.806-.1-1.212-.105-.052-5.335.195-10.67.738-15.978.068-.164.026-.354-.106-.474-.13-.075-.291-.075-.421 0-.695.31-1.162.981-1.213 1.74-.701 4.855-1.053 9.754-1.055 14.66-2.659-.065-5.32.058-7.962.368v-1.582c-.044-4.21.185-8.42.685-12.602.01-.168-.071-.329-.211-.422-.13-.075-.291-.075-.422 0-.642.25-1.117.804-1.265 1.476-.704 4.447-1.039 8.945-1.002 13.447-.624.097-1.241.238-1.846.422-.896.263-1.371 1.16-1.582 1.951-.008.07-.008.141 0 .211-.004.14.054.275.159.37.169.12.391.14.58.051.855-.323 1.737-.57 2.636-.738-.019 2.343.105 4.685.369 7.013.211 1.582 1.055 2.11 1.899 2.11.166.036.339-.003.474-.106.077-.086.115-.2.106-.316.002-.035.002-.07 0-.106-.369-2.992-.58-6.002-.633-9.017 2.62-.4 5.261-.647 7.91-.738-.035 3.03.106 6.057.421 9.07.211 1.582 1.055 2.11 1.741 2.215.198.062.416.023.58-.106.077-.086.115-.2.105-.316.002-.035.002-.07 0-.106-.43-3.587-.641-7.197-.633-10.81v-.052zm68.815 4.007c-1.055-2.267-1.213-3.902-.528-4.482.115-.092.19-.224.211-.369.005-.14-.053-.276-.158-.369-.213-.249-.517-.4-.844-.422-.296-.01-.583.104-.791.316-.896.844-1.582 2.426-2.109 4.852h-.053c-.143-.025-.288.037-.369.158-.217.267-.329.605-.316.95.011.231.046.46.105.685l.158.527-.052.211c-.053.158-.106.263-.106.422-.259.537-.66.993-1.16 1.318-.202.132-.452.17-.685.105-.422-.158-1.055-1.054-1.213-2.53 1.25-.653 2.142-1.836 2.426-3.217.059-.26.095-.525.105-.79.012-.852-.289-1.677-.844-2.322-.346-.438-.865-.707-1.423-.738-.525.013-1.022.242-1.371.633-.534.601-.946 1.3-1.213 2.057.062-3.388.326-6.769.791-10.125.05-.123.03-.265-.053-.369-.094-.1-.236-.142-.369-.105h-.053c-.549.251-.929.771-1.002 1.371-.781 4.42-1.081 8.91-.896 13.393-.389 1.05-1.136 1.927-2.109 2.48-.333.16-.722.16-1.055 0-.527-.318-.949-1.583-.897-3.165.106-2.109.897-3.85 1.424-4.219.054-.06.13-.098.211-.105.053 0 .053.053.106.105.263.422.369 1.582-.106 2.901-.022.091-.003.188.053.263.105.106.211.106.369.106.685-.053 1.371-.844 1.371-2.11-.034-.913-.531-1.749-1.318-2.214-.463-.29-1.048-.31-1.529-.053-.475.241-.876.605-1.161 1.055l-1.792 2.267c-.163-.969-.669-1.849-1.424-2.478-.243-.183-.541-.276-.844-.264-.265-.296-.696-.382-1.054-.21-.95.526-1.899 2.32-2.11 4.112-.422 3.797 1.424 4.851 2.268 5.115.676.254 1.438.134 2.003-.316.897-.686 1.424-2.11 1.424-3.902v-.844c.153-.22.294-.45.422-.686l-.105.74c-.37 3.848 1.423 4.903 2.531 5.272.776.241 1.618.145 2.32-.264.451-.277.83-.656 1.107-1.107v.052c0 .832.532 1.576 1.319 1.846.149.027.303-.01.421-.105.093-.099.132-.237.106-.37-.791-5.009 1.054-8.7 2.109-9.228.133-.093.316-.07.422.053.248.47.305 1.02.158 1.53-.293 1.335-1.163 2.474-2.373 3.111-.261.147-.408.44-.369.738.264 2.11 1.371 3.586 2.9 3.85.755.173 1.55 0 2.162-.475.357-.285.645-.645.844-1.055.403.7 1.067 1.211 1.846 1.424.763.147 1.553-.089 2.109-.633.949-.79.949-2.268.053-4.324v-.053zm-20.724-3.322c.317.053.686.791.844 1.951-.371-.232-.651-.587-.791-1.002-.074-.22-.109-.452-.106-.685-.008-.09.011-.183.053-.264zm.949 3.48c0 1.741-.527 2.953-.949 3.322-.105.121-.264.18-.422.16-.211-.054-1.054-.898-1.054-2.743 0-.21 0-.422.052-.686.047-.589.153-1.172.317-1.74.275.928 1.092 1.598 2.056 1.687zm18.825 3.322c-.131.111-.308.15-.474.106-.633-.106-1.582-.79-2.215-2.109.002-.018.002-.036 0-.053v-.053l.106-.316c.232-1.147.549-2.275.949-3.375.134.97.419 1.913.843 2.795l.106.211c.422 1.054 1.055 2.32.685 2.742v.052zM29.43 17.615c-.526-.359-1.197-.437-1.792-.21-.684.351-1.224.93-1.53 1.634l.264-2.478c.007-.053.007-.106 0-.158 0-.083-.039-.162-.105-.21-.131-.077-.292-.077-.422 0-.556.242-.939.766-1.002 1.37-.313 2.15-.507 4.315-.58 6.486-.369 1.054-.844 1.476-1.055 1.476-.044-.024-.081-.06-.105-.105-.422-.739-.633-3.903.105-6.855.041-.125.021-.262-.053-.37-.093-.1-.236-.142-.369-.105-.241.061-.461.19-.632.37-.168-.342-.423-.633-.739-.845-.479-.287-1.068-.326-1.582-.105-1.16.527-2.109 1.951-2.636 4.06-.844 3.164.211 4.746 1.476 5.273.55.265 1.191.265 1.74 0 .542-.359.936-.902 1.108-1.529.215.66.721 1.184 1.371 1.424.409.166.871.147 1.265-.053v1.846c-.002 1.672.068 3.343.211 5.01.022.812.55 1.53 1.319 1.792.14.05.297.03.421-.053.093-.099.132-.236.106-.369-.211-2.215-.369-5.062-.369-8.437.067.057.137.11.211.158.624.415 1.415.494 2.109.211 1.16-.527 2.109-1.793 2.531-3.69.633-2.637.158-4.747-1.213-5.59l-.053.052zm-8.12 3.164c-.106 2.637-.949 4.43-1.582 5.01-.097.1-.23.156-.369.158-.369-.106-.897-.79-.897-2.109.014-.478.067-.955.159-1.424.263-1.793 1.16-3.375 1.792-3.797.159-.105.211-.105.211-.105.317.105.633.843.528 2.11l.158.157zm7.804 1.582c-.316 1.582-.896 2.795-1.687 3.164-.189.117-.417.155-.633.105-.527-.158-.791-1.054-.686-2.214.159-2.268 1.055-3.902 1.951-4.588.176-.149.403-.224.633-.21.264.105.844 1.581.528 3.69l-.106.053zm14.765-4.429c.01-.116-.029-.23-.106-.317-.124-.083-.281-.102-.422-.052-.527.105-.896.527-1.054 1.318-.181.941-.305 1.892-.369 2.847l-.106 1.055c-.263 2.795-.896 3.058-1.054 3.058-.159 0-.422-.263-.633-.738-.633-1.582-.369-5.378.053-7.382.04-.125.021-.26-.053-.369-.121-.093-.282-.113-.422-.053-.53.158-.922.612-1.002 1.16-.738 2.953-.738 6.75.317 8.226.285.415.757.663 1.26.663.324 0 .64-.103.902-.294.316-.226.585-.513.79-.843l.211 3.322c.071.597.106 1.125.106 1.582 0 1.265-.211 1.898-.633 2.214-.238.148-.535.168-.791.053-.791-.316-1.582-1.476-1.898-3.164-.053-.316-.264-.369-.369-.369-.183-.013-.354.094-.422.264-.276.67-.313 1.415-.106 2.11.264 1.317 1.055 2.32 1.899 2.635.769.248 1.614.067 2.214-.474.897-.686 1.951-2.109 1.582-4.85-.399-3.805-.399-7.64 0-11.444l.106-.158zm41.816-1.055c-.723 0-1.318-.595-1.318-1.318 0-.723.596-1.318 1.319-1.318.703 0 1.289.562 1.317 1.265l.001.053c0 .723-.595 1.318-1.318 1.318h-.001zm0-2.426h-.053c-.608 0-1.107.5-1.107 1.107s.499 1.107 1.107 1.107c.607 0 1.107-.499 1.107-1.106l.002-.053c0-.578-.476-1.055-1.055-1.055h-.001zm.316 1.793l-.211-.527h-.264v.527h-.263v-1.476h.527c.242-.002.448.182.475.422.013.182-.094.353-.264.422l.264.527-.264.105zm-.211-1.16h-.264v.422h.264c.158 0 .211-.053.211-.21 0-.117-.095-.212-.211-.212z" fill="currentcolor"/>
</svg>
</div>
            <div id="shopify-logo" class="bf-maincta-logo"><svg width="108" height="31" viewBox="0 0 108 31" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M37.032 16.968c-.913-.504-1.393-.913-1.393-1.49 0-.745.648-1.201 1.682-1.201 1.2 0 2.259.505 2.259.505l.84-2.572s-.77-.6-3.052-.6c-3.172 0-5.382 1.826-5.382 4.373 0 1.44 1.033 2.547 2.403 3.34 1.105.625 1.49 1.082 1.49 1.73 0 .697-.553 1.25-1.586 1.25-1.538 0-2.98-.793-2.98-.793l-.89 2.57s1.346.89 3.58.89c3.27 0 5.6-1.61 5.6-4.493.048-1.586-1.153-2.692-2.571-3.51zm13.024-5.408c-1.61 0-2.86.77-3.845 1.923l-.048-.024 1.394-7.305h-3.653L40.371 24.73h3.63l1.2-6.344c.481-2.403 1.707-3.87 2.861-3.87.816 0 1.13.554 1.13 1.346 0 .505-.05 1.106-.17 1.61l-1.369 7.282h3.628l1.418-7.498c.17-.792.264-1.73.264-2.38.05-2.09-1.009-3.315-2.907-3.315zm9.396 10.623c-1.25 0-1.754-1.058-1.754-2.38 0-2.09 1.081-5.479 3.052-5.479 1.297 0 1.706 1.106 1.706 2.187 0 2.259-1.08 5.672-3.004 5.672zM61.23 11.56c-4.373 0-7.28 3.941-7.28 8.34 0 2.81 1.73 5.094 4.997 5.094 4.302 0 7.185-3.845 7.185-8.34.024-2.617-1.49-5.094-4.902-5.094zm10.766 10.695c-.937 0-1.49-.53-1.49-.53l.6-3.388c.434-2.259 1.611-3.772 2.861-3.772 1.105 0 1.441 1.033 1.441 1.995 0 2.33-1.394 5.695-3.412 5.695zm3.461-10.694c-2.452 0-3.846 2.162-3.846 2.162h-.048l.217-1.947h-3.221c-.168 1.322-.456 3.318-.745 4.832l-2.523 13.264h3.629l1.009-5.383h.073s.744.48 2.138.48c4.277 0 7.065-4.373 7.065-8.795 0-2.426-1.081-4.614-3.748-4.614zm8.939-5.215c-1.154 0-2.091.913-2.091 2.115 0 1.08.673 1.826 1.706 1.826h.048c1.129 0 2.115-.77 2.139-2.114.024-1.082-.697-1.827-1.802-1.827zM79.3 24.73h3.654l2.475-12.881h-3.677L79.3 24.729zm15.357-12.905h-2.523l.12-.6c.216-1.25.937-2.355 2.163-2.355.648 0 1.153.192 1.153.192l.72-2.836s-.624-.312-1.97-.312c-1.297 0-2.571.36-3.556 1.2-1.25 1.059-1.826 2.573-2.114 4.11l-.097.6H86.87l-.53 2.74h1.684L86.102 24.73h3.628l1.923-10.165h2.499l.505-2.74zm8.747.024s-2.283 5.72-3.292 8.844h-.048c-.072-1.01-.889-8.844-.889-8.844h-3.82l2.186 11.824c.048.264.024.432-.073.6-.432.818-1.129 1.61-1.97 2.188-.673.504-1.442.816-2.043 1.033l1.01 3.075c.744-.168 2.258-.77 3.556-1.97 1.658-1.562 3.197-3.941 4.758-7.21l4.446-9.54h-3.821zM14.658 4.496c0-.721-.096-1.754-.432-2.62 1.106.217 1.634 1.442 1.875 2.187-.434.12-.914.265-1.443.433zm-5.719 9.708c.096 1.538 4.157 1.875 4.398 5.504.168 2.859-1.514 4.805-3.941 4.95-2.932.192-4.542-1.538-4.542-1.538l.625-2.644s1.61 1.226 2.908 1.13c.841-.048 1.153-.745 1.129-1.225-.12-2.02-3.436-1.9-3.653-5.215-.192-2.788 1.634-5.6 5.672-5.864 1.561-.096 2.354.289 2.354.289l-.913 3.46s-1.033-.481-2.259-.384c-1.778.12-1.802 1.249-1.778 1.537zM11.726.988c.337 0 .625.07.866.216-.385.192-.769.505-1.13.865-.913.985-1.61 2.523-1.898 3.989-.865.264-1.73.529-2.524.769.529-2.307 2.476-5.792 4.686-5.84zm1.971 3.797c-.961.288-2.018.625-3.051.936.288-1.13.865-2.26 1.537-3.003.265-.265.625-.577 1.034-.77.408.866.504 2.044.48 2.837zm4.206-1.298s-.337.096-.889.264c-.097-.312-.241-.673-.433-1.058-.625-1.201-1.562-1.85-2.668-1.85-.071 0-.144 0-.24.025-.024-.05-.072-.073-.096-.121-.481-.528-1.105-.77-1.851-.745-1.441.048-2.883 1.082-4.037 2.932-.816 1.298-1.441 2.932-1.609 4.205-1.658.505-2.812.865-2.836.889-.841.265-.865.289-.961 1.082C2.21 9.71 0 26.628 0 26.628l18.167 3.149V3.462c-.144 0-.217.025-.264.025zm.816 26.24l7.546-1.873S23.02 5.913 22.997 5.768c-.024-.145-.144-.24-.264-.24-.12 0-2.235-.049-2.235-.049s-1.298-1.249-1.78-1.73v25.977z" fill="currentcolor"/>
</svg>
</div>
            <div id="stripe-logo" class="bf-maincta-logo"><svg width="68" height="30" viewBox="0 0 68 30" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M67.561 15.424c0-4.804-2.327-8.595-6.775-8.595-4.467 0-7.169 3.791-7.169 8.557 0 5.65 3.19 8.502 7.77 8.502 2.233 0 3.922-.507 5.198-1.22v-3.753c-1.276.638-2.74 1.032-4.598 1.032-1.82 0-3.435-.638-3.64-2.853h9.176c0-.244.038-1.22.038-1.67zm-9.27-1.783c0-2.12 1.294-3.003 2.476-3.003 1.145 0 2.365.882 2.365 3.003H58.29zM46.373 6.83c-1.839 0-3.02.862-3.678 1.462l-.244-1.163h-4.129v21.882l4.692-.994.02-5.31c.675.487 1.67 1.181 3.321 1.181 3.36 0 6.418-2.702 6.418-8.652-.019-5.442-3.115-8.407-6.4-8.407zm-1.126 12.93c-1.107 0-1.764-.395-2.214-.883l-.019-6.962c.488-.545 1.164-.92 2.233-.92 1.708 0 2.891 1.914 2.891 4.373 0 2.515-1.164 4.391-2.89 4.391zM31.865 5.721l4.711-1.013V.898l-4.71.995v3.828zm0 1.427h4.711v16.421h-4.71V7.148zm-5.046 1.388l-.3-1.388h-4.054v16.421h4.692V12.44c1.107-1.445 2.984-1.182 3.566-.976V7.148c-.601-.226-2.797-.638-3.904 1.388zm-9.385-5.461l-4.58.976-.018 15.033c0 2.777 2.084 4.823 4.86 4.823 1.54 0 2.666-.282 3.285-.62v-3.81c-.6.245-3.565 1.108-3.565-1.67v-6.662h3.565V7.148h-3.565l.018-4.073zm-12.686 8.84c0-.732.6-1.014 1.595-1.014 1.426 0 3.228.432 4.654 1.201v-4.41C9.44 7.073 7.901 6.83 6.343 6.83 2.533 6.83 0 8.82 0 12.14c0 5.18 7.131 4.354 7.131 6.587 0 .863-.75 1.145-1.801 1.145-1.558 0-3.547-.638-5.124-1.502v4.467c1.745.751 3.51 1.07 5.124 1.07 3.903 0 6.587-1.933 6.587-5.293-.019-5.592-7.169-4.598-7.169-6.699z" fill="currentcolor"/>
</svg>
</div>
          </div>
          <h2>Join 140,000+ small businesses like yours that use Buffer to build their brand on social media every month</h2>
          <a class="gh-button gh-button-lightred"
            href="https://login.buffer.com/signup?product=buffer&plan=free&cycle=year&cta=bufferBlogResources-ctaBanner-signup-1"
            onclick="fathom.trackGoal('6QQZXZYI', 0);" role="button">Sign up for free</a>
          <ul class="bf-cta-features">
            <li><svg viewBox="0 0 29 28" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" stroke-linecap="round" stroke-miterlimit="10">
  <path d="M10.95 14.264l3.388 3.313 4.603-7.291" fill="none" stroke="#b8b8b8" stroke-width="2"/>
  <path fill="none" d="M8.945 7.931h12v12h-12z"/>
</svg>
 No credit card required</li>
            <li><svg viewBox="0 0 29 28" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" stroke-linecap="round" stroke-miterlimit="10">
  <path d="M10.95 14.264l3.388 3.313 4.603-7.291" fill="none" stroke="#b8b8b8" stroke-width="2"/>
  <path fill="none" d="M8.945 7.931h12v12h-12z"/>
</svg>
 Cancel anytime</li>
          </ul>
        </div>
      </div>
    </div>

    <footer class="bf-foot">
      <div class="bf-foot-wrapper">
        <div class="bf-foot-container gh-container">
          <div class="bf-foot-mast">
            <div class="bf-foot-mast-top">
              <a class="bf-foot-logo" href="https://buffer.com/resources/">
                <img src="/resources/content/images/2021/02/buffer-logo.svg" alt="Buffer Resources" />
              </a>
            </div>
          </div>
          <div class="bf-foot-nav">
            <div>
              <strong>Categories</strong>
              <ul class="bf-foot-nav-list">
                <li><a href="https://buffer.com/resources/social-media-marketing/">Social Media Marketing</a></li>
                <li><a href="https://buffer.com/resources/instagram/">Instagram Marketing</a></li>
                <li><a href="https://buffer.com/resources/analytics/">Social Analytics</a></li>
                <li><a href="https://buffer.com/resources/news-trends/">News and Trends</a></li>
                <li><a href="https://buffer.com/resources/tools/">Best apps and tools</a></li>
                <li><a href="https://buffer.com/resources/open/">Inside Buffer</a></li>
                <li><a href="https://buffer.com/resources/remote-work/">Remote Work</a></li>
                <li><a href="https://buffer.com/resources/open/">Transparency</a></li>
              </ul>
            </div>
            <div>
              <strong>Blog & podcasts</strong>
              <ul class="bf-foot-nav-list">
                <li><a href="https://buffer.com/resources/science-of-social-media/">Science of Social Media</a></li>
                <li><a href="https://buffer.com/resources/breaking-brand/">Breaking Brand</a></li>
                <li><a href="https://buffer.com/resources/flow/">Social Media Blog</a></li>
                <li><a href="https://buffer.com/resources/open/">Open Blog</a></li>
              </ul>
            </div>
            <div>
              <strong>About Buffer</strong>
              <ul class="bf-foot-nav-list">
                <li><a
                    href="https://buffer.com/brand-building?utm_source=resources&utm_medium=blog&utm_campaign=footer-table-of-contents"
                    onclick="fathom.trackGoal('6QQZXZYI', 0);">Social
                    media solutions</a></li>
                <li><a href="https://buffer.com/about">Our culture</a></li>
                <li><a href="https://buffer.com/resources/buffer-values/">Our values</a></li>
              </ul>
            </div>
          </div>
          <div class="bf-foot-mast-bottom">
            <div class="bf-foot-mast-bottom-left">
              <div class="bf-foot-social">
                <a class="bf-foot-social-ig" href="https://instagram.com/buffer" target="_blank" rel="noopener"
                  aria-label="Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <path d="M16 2.881c4.275 0 4.781.019 6.462.094 1.563.069 2.406.331 2.969.55a4.952 4.952 0 0 1 1.837 1.194 5.015 5.015 0 0 1 1.2 1.838c.219.563.481 1.412.55 2.969.075 1.688.094 2.194.094 6.463s-.019 4.781-.094 6.463c-.069 1.563-.331 2.406-.55 2.969a4.94 4.94 0 0 1-1.194 1.837 5.02 5.02 0 0 1-1.837 1.2c-.563.219-1.413.481-2.969.55-1.688.075-2.194.094-6.463.094s-4.781-.019-6.463-.094c-1.563-.069-2.406-.331-2.969-.55a4.952 4.952 0 0 1-1.838-1.194 5.02 5.02 0 0 1-1.2-1.837c-.219-.563-.481-1.413-.55-2.969-.075-1.688-.094-2.194-.094-6.463s.019-4.781.094-6.463c.069-1.563.331-2.406.55-2.969a4.964 4.964 0 0 1 1.194-1.838 5.015 5.015 0 0 1 1.838-1.2c.563-.219 1.412-.481 2.969-.55 1.681-.075 2.188-.094 6.463-.094zM16 0c-4.344 0-4.887.019-6.594.094-1.7.075-2.869.35-3.881.744-1.056.412-1.95.956-2.837 1.85a7.833 7.833 0 0 0-1.85 2.831C.444 6.538.169 7.7.094 9.4.019 11.113 0 11.656 0 16s.019 4.887.094 6.594c.075 1.7.35 2.869.744 3.881.413 1.056.956 1.95 1.85 2.837a7.82 7.82 0 0 0 2.831 1.844c1.019.394 2.181.669 3.881.744 1.706.075 2.25.094 6.594.094s4.888-.019 6.594-.094c1.7-.075 2.869-.35 3.881-.744 1.05-.406 1.944-.956 2.831-1.844s1.438-1.781 1.844-2.831c.394-1.019.669-2.181.744-3.881.075-1.706.094-2.25.094-6.594s-.019-4.887-.094-6.594c-.075-1.7-.35-2.869-.744-3.881a7.506 7.506 0 0 0-1.831-2.844A7.82 7.82 0 0 0 26.482.843C25.463.449 24.301.174 22.601.099c-1.712-.081-2.256-.1-6.6-.1z"/>
  <path d="M16 7.781c-4.537 0-8.219 3.681-8.219 8.219s3.681 8.219 8.219 8.219 8.219-3.681 8.219-8.219A8.221 8.221 0 0 0 16 7.781zm0 13.55a5.331 5.331 0 1 1 0-10.663 5.331 5.331 0 0 1 0 10.663zM26.462 7.456a1.919 1.919 0 1 1-3.838 0 1.919 1.919 0 0 1 3.838 0z"/>
</svg>
</a>
                <a class="bf-foot-social-fb" href="https://www.facebook.com/bufferapp" target="_blank" rel="noopener"
                  aria-label="Facebook"><svg width="16" height="31" viewBox="0 0 16 31" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10.3 30.7v-14H15l.7-5.5h-5.4V7.8c0-1.6.4-2.7 2.7-2.7h3V.2C14.6.1 13.2 0 11.8 0c-4.2 0-7 2.5-7 7.2v4H0v5.5h4.7v14h5.6z" /></svg></a>
                <a class="bf-foot-social-tw" href="https://twitter.com/buffer" target="_blank" rel="noopener"
                  aria-label="Twitter"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M30.063 7.313c-.813 1.125-1.75 2.125-2.875 2.938v.75c0 1.563-.188 3.125-.688 4.625a15.088 15.088 0 0 1-2.063 4.438c-.875 1.438-2 2.688-3.25 3.813a15.015 15.015 0 0 1-4.625 2.563c-1.813.688-3.75 1-5.75 1-3.25 0-6.188-.875-8.875-2.625.438.063.875.125 1.375.125 2.688 0 5.063-.875 7.188-2.5-1.25 0-2.375-.375-3.375-1.125s-1.688-1.688-2.063-2.875c.438.063.813.125 1.125.125.5 0 1-.063 1.5-.25-1.313-.25-2.438-.938-3.313-1.938a5.673 5.673 0 0 1-1.313-3.688v-.063c.813.438 1.688.688 2.625.688a5.228 5.228 0 0 1-1.875-2c-.5-.875-.688-1.813-.688-2.75 0-1.063.25-2.063.75-2.938 1.438 1.75 3.188 3.188 5.25 4.25s4.313 1.688 6.688 1.813a5.579 5.579 0 0 1 1.5-5.438c1.125-1.125 2.5-1.688 4.125-1.688s3.063.625 4.188 1.813a11.48 11.48 0 0 0 3.688-1.375c-.438 1.375-1.313 2.438-2.563 3.188 1.125-.125 2.188-.438 3.313-.875z"/></svg></a>
                <a class="bf-foot-social-li" href="https://www.linkedin.com/company/bufferapp" target="_blank"
                  rel="noopener" aria-label="LinkedIn"><svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M23.6 23.9h-4v-6.3c0-1.5 0-3.4-2.1-3.4s-2.4 1.6-2.4 3.3v6.4h-4V11H15v1.8h.1c.5-1 1.9-2.1 3.8-2.1 4.1 0 4.8 2.7 4.8 6.2v7h-.1zM6.5 9.2c-1.3 0-2.3-1-2.3-2.3 0-1.3 1-2.3 2.3-2.3 1.3 0 2.3 1 2.3 2.3.1 1.2-1 2.3-2.3 2.3zm2.1 14.7h-4V11h4v12.9zM25.7.8H2.5c-1.1 0-2 .9-2 2V26c0 1.1.9 2 2 2h23.2c1.1 0 2-.9 2-2V2.7c0-1-.9-1.9-2-1.9z" /></svg></a>
                <a class="bf-foot-social-pi" href="https://www.pinterest.com/bufferapp/" target="_blank" rel="noopener"
                  aria-label="Pinterest"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16.0131 0C7.16967 0 0 7.1579 0 15.9868C0 22.7632 4.21745 28.5526 10.1746 30.8816C10.0296 29.6184 9.91102 27.6711 10.2273 26.2895C10.5173 25.0395 12.0988 18.3421 12.0988 18.3421C12.0988 18.3421 11.6244 17.3816 11.6244 15.9737C11.6244 13.75 12.916 12.0921 14.5239 12.0921C15.8945 12.0921 16.5535 13.1184 16.5535 14.3421C16.5535 15.7105 15.6837 17.7632 15.2224 19.6711C14.8402 21.2632 16.0263 22.5658 17.5947 22.5658C20.4415 22.5658 22.6293 19.5658 22.6293 15.25C22.6293 11.4211 19.8748 8.75 15.9341 8.75C11.3739 8.75 8.6985 12.1579 8.6985 15.6842C8.6985 17.0526 9.22568 18.5263 9.88466 19.3289C10.0165 19.4868 10.0296 19.6316 9.99009 19.7895C9.87148 20.2895 9.59471 21.3816 9.54199 21.6053C9.47609 21.8947 9.30476 21.9605 9.00163 21.8158C6.99834 20.8816 5.74628 17.9737 5.74628 15.6184C5.74628 10.5789 9.41019 5.94737 16.3295 5.94737C21.878 5.94737 26.2009 9.89474 26.2009 15.1842C26.2009 20.6974 22.7215 25.1316 17.8978 25.1316C16.2767 25.1316 14.7479 24.2895 14.2339 23.2895C14.2339 23.2895 13.43 26.3421 13.2323 27.0921C12.8764 28.4868 11.9011 30.2237 11.2422 31.2895C12.7446 31.75 14.3262 32 15.9868 32C24.8303 32 31.9999 24.8421 31.9999 16.0132C32.0263 7.15789 24.8566 0 16.0131 0Z" />
</svg>
</a>
              </div>
              <div class="bf-foot-legal">
                Copyright &copy; 2023 Buffer <span>|</span> <a
                  href="https://buffer.com/legal#privacy-policy">Privacy</a> <span>|</span> <a
                  href="https://buffer.com/legal#terms">Terms</a> <span>|</span> <a
                  href="https://buffer.com/legal#security">Security</a>
              </div>
            </div>
            <div class="bf-foot-mast-bottom-right">
              <p>Get started with Buffer for free </p>
              <a class="gh-button gh-button-primary"
                href="https://login.buffer.com/signup?product=buffer&plan=free&cycle=year&cta=bufferBlogResources-footer-signup-1"
                onclick="fathom.trackGoal('6QQZXZYI', 0);" role="button">Sign up now</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
  <div id="search-modal" class="bf-modal-backdrop" :class="{ 'bf-modal--open': searchIsOpen() }"
    :aria-expanded="searchIsOpen() ? 'true' : 'false'">
    <div class="bf-search-modal">
      <div class="bf-modal-content gh-container">
        <div class="bf-modal-head">
          <form class="bf-search-input">
            <span><svg width="27" height="28" viewBox="0 0 27 28" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10" stroke="currentcolor" stroke-width="3" stroke-linecap="round"/>
  <path d="M19 19.5l6.5 6.5" stroke="currentcolor" stroke-width="3" stroke-linecap="round"/>
</svg></span>
            <label class="hidden" for="search">Search</label>
            <input id="search-field" type=text placeholder="Search" autocomplete="off" autofocus="true"
              onfocus="this.value = ''" name="search" aria-label="Search" x-on:input.once="search.start()" />
          </form>
          <div id="search-close" class="bf-search-close" role="button" @click="closeSearchModal"
            aria-label="Close Search"><svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M25.542 25.542c.61-.61.61-1.587 0-2.197L2.655.458c-.61-.61-1.587-.61-2.197 0-.61.61-.61 1.587 0 2.197l22.887 22.887c.61.61 1.587.61 2.197 0z" fill="currentcolor"/>
  <path fill-rule="evenodd" clip-rule="evenodd" d="M25.542.458c-.61-.61-1.587-.61-2.197 0L.458 23.345c-.61.61-.61 1.587 0 2.197.61.61 1.587.61 2.197 0L25.542 2.655c.55-.61.55-1.587 0-2.197z" fill="currentcolor"/>
</svg></div>
        </div>
        <div id="suggestions" class="bf-modal-body">
          <h3 class="bf-search-title">May we suggest</h3>
          <div class="bf-search-suggestions">
            <a class="bf-suggestion" href="https://buffer.com/resources/open/">Inside Buffer</a>
            <a class="bf-suggestion" href="https://buffer.com/resources/online-marketing/">Online Marketing</a>
            <a class="bf-suggestion" href="https://buffer.com/resources/social-media-marketing/">Social Media Marketing</a>
            <a class="bf-suggestion" href="https://buffer.com/resources/tips-how-to/">Tips / How To</a>
          </div>
        </div>
        <div id="results" class="">
        </div>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/@tryghost/content-api@1.4.1/umd/content-api.min.js"
    integrity="sha256-g/5nu4pCu3GBwkr71MyB8boZhkd9ZibNoV0JAs6ZIOU=" crossorigin="anonymous"></script>
  <script src="https://buffer.com/resources/assets/built/buffer.js?v=5ec3319331"></script>
    <script src="https://buffer.com/resources/assets/built/mobile-menu.js?v=5ec3319331"></script>
  <script>
    var siteUrl = "https://buffer.com/resources";
  </script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/vaafb692b2aea4879b33c060e79fe94621666317369993" integrity="sha512-0ahDYl866UMhKuYcW078ScMalXqtFJggm7TmlUtp0UlD4eQk0Ixfnm5ykXKvGJNFjLMoortdseTfsRT8oCfgGA==" data-cf-beacon='{"rayId":"7a1a304d18bd862c","token":"d6f4af4cc5954a5fa6947c67b09f4363","version":"2023.2.0","si":100}' crossorigin="anonymous"></script>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')

print("1. soup.head : ",soup.head)
print("2. soup.title : ",soup.title)
print("2. soup.title.contents : ",soup.title.contents)
print("3. soup.body.b : ",soup.body.b)
#print("3. soup.body.b.string : ",soup.body.b.string)
print("4. soup.a : ",soup.a)
print("5. soup.find_all('a') : ",soup.find_all('a'))