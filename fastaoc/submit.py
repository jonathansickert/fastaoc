import os

import requests
from dotenv import load_dotenv

load_dotenv()


def submit(year: int, day: int, part: int, answer: int):
    data: dict[str, str] = {"level": str(part), "answer": str(answer)}
    cookie: str | None = os.environ.get("SESSION_COOKIE")
    assert cookie is not None
    respose: requests.Response = requests.post(
        url=f"https://adventofcode.com/{year}/day/{day}/answer",
        data=data,
        cookies={"session": cookie},
    )
    print(respose.text)


text = """
<!DOCTYPE html>
<html lang="en-us">
<head>
<meta charset="utf-8"/>
<title>Day 1 - Advent of Code 2024</title>
<link rel="stylesheet" type="text/css" href="/static/style.css?31"/>
<link rel="stylesheet alternate" type="text/css" href="/static/highcontrast.css?1" title="High Contrast"/>
<link rel="shortcut icon" href="/favicon.png"/>
<script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
</head><!--




Oh, hello!  Funny seeing you here.

I appreciate your enthusiasm, but you aren't going to find much down here.
There certainly aren't clues to any of the puzzles.  The best surprises don't
even appear in the source until you unlock them for real.

Please be careful with automated requests; I'm not a massive company, and I can
only take so much traffic.  Please be considerate so that everyone gets to play.

If you're curious about how Advent of Code works, it's running on some custom
Perl code. Other than a few integrations (auth, analytics, social media), I
built the whole thing myself, including the design, animations, prose, and all
of the puzzles.

The puzzles are most of the work; preparing a new calendar and a new set of
puzzles each year takes all of my free time for 4-5 months. A lot of effort
went into building this thing - I hope you're enjoying playing it as much as I
enjoyed making it for you!

If you'd like to hang out, I'm @was.tl on Bluesky, @ericwastl@hachyderm.io on
Mastodon, and @ericwastl on Twitter.

- Eric Wastl


















































-->
<body>
<header><div><h1 class="title-global"><a href="/">Advent of Code</a></h1><nav><ul><li><a href="/2024/about">[About]</a></li><li><a href="/2024/events">[Events]</a></li><li><a href="https://cottonbureau.com/people/advent-of-code" target="_blank">[Shop]</a></li><li><a href="/2024/settings">[Settings]</a></li><li><a href="/2024/auth/logout">[Log Out]</a></li></ul></nav><div class="user">(anonymous user #4691338) <span class="star-count">4*</span></div></div><div><h1 class="title-event">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="title-event-wrap">Î»y.</span><a href="/2024">2024</a><span class="title-event-wrap"></span></h1><nav><ul><li><a href="/2024">[Calendar]</a></li><li><a href="/2024/support">[AoC++]</a></li><li><a href="/2024/sponsors">[Sponsors]</a></li><li><a href="/2024/leaderboard">[Leaderboard]</a></li><li><a href="/2024/stats">[Stats]</a></li></ul></nav></div></header>

<div id="sidebar">
<div id="sponsor"><div class="quiet">Our <a href="/2024/sponsors">sponsors</a> help make Advent of Code possible:</div><div class="sponsor"><a href="/2024/sponsors/redirect?url=https%3A%2F%2Fwww%2Ebjss%2Ecom%2F" target="_blank" onclick="if(ga)ga('send','event','sponsor','sidebar',this.href);" rel="noopener">BJSS</a> - Delivered by teams of passionate experts, we provide brilliant software engineering that delivers transformative outcomes for our clients.</div></div>
</div><!--/sidebar-->

<main>
<article><p>That's the right answer!  You are <span class="day-success">one gold star</span> closer to finding the Chief Historian.</p><p>You have completed Day 1! You can <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I+just+completed+%22Historian+Hysteria%22+%2D+Day+1+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F1" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I+just+completed+%22Historian+Hysteria%22+%2D+Day+1+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F1&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I+just+completed+%22Historian+Hysteria%22+%2D+Day+1+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F1';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this victory or <a href="/2024">[Return to Your Advent Calendar]</a>.</p></article>
</main>

<!-- ga -->
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');
</script>
<!-- /ga -->
</body>
</html>
"""

if __name__ == "__main__":
    # a = 18934359
    # submit(year=2024, day=1, part=2, answer=a)

    print("That's the right answer!" in text)
