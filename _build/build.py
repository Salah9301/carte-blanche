#!/usr/bin/env python3
"""Builds the one-file proposal sites (maquettes) for real Caen restaurants.

Run: python3 _build/build.py   -> writes <slug>/index.html for each site in sites.py
"""
import html, json, os, urllib.parse
from icons import icon
from sites import SITES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def t(fr, en=None):
    """Bilingual inline text: both spans are rendered, CSS shows the active language."""
    fr = fr.replace(" ?", "\u00a0?").replace(" :", "\u00a0:").replace(" !", "\u00a0!").replace("« ", "«\u00a0").replace(" »", "\u00a0»")
    if en is None or en == fr:
        return fr
    return f'<span data-l="fr">{fr}</span><span data-l="en">{en}</span>'

PATTERNS = {
    # 8-point star (zellige)
    "zellige": '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 56 56"><g fill="none" stroke="C" stroke-width="1"><path d="M28 10l5 8.5 9.7-2.2-2.2 9.7L49 31l-8.5 5 2.2 9.7-9.7-2.2L28 52l-5-8.5-9.7 2.2 2.2-9.7L7 31l8.5-5-2.2-9.7 9.7 2.2z" transform="translate(0 -3)"/><path d="M0 0l8 8M56 0l-8 8M0 56l8-8M56 56l-8-8"/></g></svg>',
    # Levantine arches
    "arches": '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="64" viewBox="0 0 48 64"><g fill="none" stroke="C" stroke-width="1"><path d="M6 64V30C6 18 14 10 24 6c10 4 18 12 18 24v34"/><path d="M14 64V32c0-7 4-12 10-15 6 3 10 8 10 15v32"/></g></svg>',
    # diamond lattice
    "lattice": '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"><g fill="none" stroke="C" stroke-width="1"><path d="M20 0l20 20-20 20L0 20z"/><path d="M20 10l10 10-10 10-10-10z"/><circle cx="20" cy="20" r="1.5" fill="C"/></g></svg>',
    # dots grid (modern)
    "dots": '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22"><circle cx="2" cy="2" r="1.3" fill="C"/></svg>',
    # Ottoman quatrefoil
    "quatrefoil": '<svg xmlns="http://www.w3.org/2000/svg" width="52" height="52" viewBox="0 0 52 52"><g fill="none" stroke="C" stroke-width="1"><path d="M26 8c6 0 9 5 9 9 4 0 9 3 9 9s-5 9-9 9c0 4-3 9-9 9s-9-5-9-9c-4 0-9-3-9-9s5-9 9-9c0-4 3-9 9-9z"/><circle cx="26" cy="26" r="3"/><path d="M0 0l6 6M52 0l-6 6M0 52l6-6M52 52l-6-6"/></g></svg>',
}

def pattern_uri(name, color):
    svg = PATTERNS[name].replace('"C"', f'"{color}"')
    return "url(\"data:image/svg+xml," + urllib.parse.quote(svg) + "\")"

def esc(s):
    return html.escape(s, quote=True)

def fmt_time(m):
    m %= 1440
    return f"{m//60:02d}:{m%60:02d}"

def render(s):
    th = s["theme"]
    tel_href = "tel:" + s["tel_intl"]
    maps_q = urllib.parse.quote_plus(s["address"] + ", " + s["city"])
    dir_url = f"https://www.google.com/maps/dir/?api=1&destination={maps_q}"
    map_url = f"https://www.google.com/maps?q={maps_q}&output=embed"

    nav_links = "".join(
        f'<a href="#{a}">{t(fr, en)}</a>'
        for a, fr, en in [("histoire", "Notre maison", "Our story"), ("carte", "La carte", "Menu"), ("visite", "Nous trouver", "Visit us")]
    )

    marquee_items = "".join(f"<span>{esc(w)}</span>" for w in s["marquee"]) * 2

    pillars = "".join(
        f'<div class="pillar"><b>{t(*p[0])}</b><span>{t(*p[1])}</span></div>' for p in s["pillars"]
    )

    sigs = "".join(
        f'''<article class="dish reveal" tabindex="0"><div class="dish-art">{icon(d["icon"], "ico", 1.3)}</div>
          <div class="dish-body"><span class="tag">{t(*d["tag"])}</span><h3>{t(*d["name"])}</h3><p>{t(*d["desc"])}</p>{f'<b class="dish-price">{d["price"]}</b>' if d.get("price") else ""}</div></article>'''
        for d in s["signatures"]
    )

    def item_html(it, rich=False):
        price = it.get("price") or ""
        name = t(*it["name"])
        desc = t(*it["desc"]) if it.get("desc") else ""
        body = f'<div class="item-top"><h4>{name}</h4>' + (f'<i></i><b>{price}</b>' if price else '') + '</div>' + (f"<p>{desc}</p>" if desc else "")
        if rich:
            return f'<div class="c-item"><div class="c-thumb">{icon(it.get("icon", s["hero_icon"]), "ico", 1.5)}</div><div>{body}</div></div>'
        return f'<div class="item">{body}</div>'

    tabs = "".join(
        f'<button class="{"on" if k == 0 else ""}" data-tab="t{k+1}" role="tab">{t(*cat["label"])}</button>'
        for k, cat in enumerate(s["menu"])
    )
    lists = "".join(
        f'<div class="menu-list{" on" if k == 0 else ""}" id="t{k+1}">' + "".join(item_html(it) for it in cat["items"]) + "</div>"
        for k, cat in enumerate(s["menu"])
    )
    carte_tabs = "".join(
        f'<button type="button" data-go="c-t{k+1}" class="{"on" if k == 0 else ""}">{t(*cat["label"])}</button>'
        for k, cat in enumerate(s["menu"])
    )
    carte_cats = "".join(
        f'''<section class="carte-cat" id="c-t{k+1}"><div class="carte-banner">{icon(cat.get("icon", s["hero_icon"]), "ban-ico", 1)}<h3><small>{t(*cat["kicker"])}</small>{t(*cat["label"])}</h3></div>
        <div class="carte-items">''' + "".join(item_html(it, True) for it in cat["items"]) + "</div></section>"
        for k, cat in enumerate(s["menu"])
    )

    chips_pay = "".join(f'<span class="chip">{t(*c)}</span>' for c in s["payments"])
    chips_svc = "".join(f'<span class="chip">{t(*c)}</span>' for c in s["services"])

    contact_extra = ""
    for c in s.get("links", []):
        contact_extra += f'''<a href="{esc(c["href"])}" target="_blank" rel="noopener">{ICON_LINK}<span><small>{esc(c["label"])}</small><strong>{t(*c["text"])}</strong></span></a>'''

    hero_meta = "".join(f'<div><strong>{t(*m[0])}</strong><span>{t(*m[1])}</span></div>' for m in s["hero_meta"])

    orbit = "".join(
        f'<span class="orb o{i+1}">{icon(n, "ico", 1.4)}</span>' for i, n in enumerate(s["orbit"])
    )

    pat = pattern_uri(th["pattern"], th["pattern_color"])

    page = TEMPLATE
    repl = {
        "{{TITLE}}": esc(s["name"]) + " · " + esc(s["city_short"]),
        "{{DESC}}": esc(s["meta_desc"]),
        "{{FONTS}}": th["fonts_href"],
        "{{SERIF}}": th["serif"],
        "{{SANS}}": th["sans"],
        "{{BG}}": th["bg"], "{{BG_RGB}}": th["bg_rgb"], "{{BG2}}": th["bg2"], "{{CARD}}": th["card"],
        "{{LINE}}": th["line"], "{{TEXT}}": th["text"], "{{MUTED}}": th["muted"], "{{SOFT}}": th["soft"],
        "{{ACCENT}}": th["accent"], "{{ACCENT2}}": th["accent2"], "{{ON_ACCENT}}": th["on_accent"],
        "{{GOLD}}": th["gold"], "{{GOLD_SOFT}}": th["gold_soft"], "{{GLOW}}": th["glow"],
        "{{SCHEME}}": th.get("scheme", "dark"), "{{GHOST}}": th["ghost"],
        "{{PATTERN}}": pat,
        "{{LOGO}}": s["logo"], "{{LOGO_SUB}}": s["logo_sub"],
        "{{NAV_LINKS}}": nav_links,
        "{{TEL_HREF}}": tel_href, "{{TEL}}": s["tel"],
        "{{HERO_ICON}}": icon(s["hero_icon"], "hero-ico", 0.9),
        "{{ORBIT}}": orbit,
        "{{HERO_KICKER}}": t(*s["hero_kicker"]),
        "{{H1}}": t(*s["h1"]),
        "{{LEAD}}": t(*s["lead"]),
        "{{DIR_URL}}": dir_url, "{{MAP_URL}}": map_url,
        "{{HERO_META}}": hero_meta,
        "{{MARQUEE}}": marquee_items,
        "{{ABOUT_ICON}}": icon(s["about_icon"], "about-ico", 0.9),
        "{{BADGE}}": f'<strong>{t(*s["badge"][0])}</strong><span>{t(*s["badge"][1])}</span>',
        "{{AB_H}}": t(*s["about_h"]),
        "{{AB_P}}": "".join(f"<p>{t(*p)}</p>" for p in s["about_p"]),
        "{{PILLARS}}": pillars,
        "{{SG_H}}": t(*s["sig_h"]), "{{SG_P}}": t(*s["sig_p"]),
        "{{SIGS}}": sigs,
        "{{MN_H}}": t(*s["menu_h"]),
        "{{TABS}}": tabs, "{{LISTS}}": lists,
        "{{MENU_NOTE}}": t(*s["menu_note"]),
        "{{HOURS_H}}": t(*s["hours_h"]),
        "{{PAY}}": chips_pay, "{{SVC}}": chips_svc,
        "{{ADDRESS}}": esc(s["address"]) + ", " + esc(s["city"]),
        "{{CONTACT_EXTRA}}": contact_extra,
        "{{CTA_H}}": t(*s["cta_h"]), "{{CTA_P}}": t(*s["cta_p"]),
        "{{CARTE_SUB}}": esc(s["name"].upper()) + " · CAEN",
        "{{CARTE_TABS}}": carte_tabs, "{{CARTE_CATS}}": carte_cats,
        "{{NAME}}": esc(s["name"]),
        "{{SCHEDULE}}": json.dumps(s["schedule"]),
        "{{SLUG}}": s["slug"],
        "{{SOURCES}}": esc(s["sources"]),
    }
    for k, v in repl.items():
        page = page.replace(k, v)
    if th.get("scheme", "dark") == "dark":
        page = page.replace("<body>", '<body class="dark-map">', 1)
    assert "{{" not in page, [l for l in page.splitlines() if "{{" in l][:3]
    return page

ICON_LINK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>'

TEMPLATE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "template.html"), encoding="utf-8").read()

if __name__ == "__main__":
    for s in SITES:
        out = os.path.join(ROOT, s["slug"], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(s))
        print("wrote", out, os.path.getsize(out))
