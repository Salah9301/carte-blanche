# Line illustrations (64x64, stroke = currentColor) shared by the proposal sites.
ICONS = {
"tagine": '<ellipse cx="32" cy="52" rx="25" ry="5"/><path d="M11 50c2-3 9-5 21-5s19 2 21 5"/><path d="M17 46 29.5 15h5L47 46"/><path d="M29.5 15c.2-3 4.8-3 5 0"/><circle cx="32" cy="9.5" r="2.6"/><path d="M21.5 36h21M25 27h14"/><path d="M27 41.5h10"/>',
"couscous": '<path d="M7 36h50c0 11-11 19-25 19S7 47 7 36z"/><path d="M12 36c2-11 10-17 20-17s18 6 20 17"/><path d="M24 21l-5-9M33 19.5V9M41 22l5-8"/><circle cx="22" cy="30" r="1.2"/><circle cx="30" cy="27" r="1.2"/><circle cx="39" cy="30" r="1.2"/><circle cx="34" cy="32" r="1.2"/><circle cx="26" cy="33" r="1.2"/><path d="M24 55l-3 3h22l-3-3"/>',
"skewer": '<path d="M9 55 55 9"/><rect x="16" y="37" width="11" height="11" rx="2.5" transform="rotate(45 21.5 42.5)"/><circle cx="32" cy="32" r="5.5"/><rect x="37" y="16" width="11" height="11" rx="2.5" transform="rotate(45 42.5 21.5)"/><path d="M52 12l3-3"/><path d="M6 58l3-3"/>',
"wrap": '<path d="M21 58 12 21c8-7 32-7 40 0l-9 37z"/><path d="M12 21c3 4 7-1 10 2s7-3 10 0 7-3 10 0 6-2 10-2"/><path d="M15 33h33M17.5 43h29"/><path d="M22 14c2-3 6-4 10-4s8 1 10 4"/>',
"doner": '<path d="M32 4v56"/><path d="M21 13h22l-3.5 37h-15z"/><path d="M22 21h20M23 30h18M24 39h16"/><path d="M14 56h36"/><path d="M48 18c4 3 4 9 0 12M52 15c6 5 6 13 0 18"/>',
"teapot": '<path d="M17 30h30c0 14-7 22-15 22s-15-8-15-22z"/><path d="M21 30c0-6 5-10 11-10s11 4 11 10"/><path d="M32 20v-5"/><circle cx="32" cy="12" r="2.4"/><path d="M17 36 7 27l2-2.5 9.5 6"/><path d="M47 32c8.5 0 8.5 13 0 14"/><path d="M22 56h20"/>',
"tea": '<path d="M21 18h22l-3.5 37h-15z"/><path d="M22.2 28h19.6"/><path d="M28 12c3-3 0-5 3-8M35 12c3-3 0-5 3-8"/><path d="M38 34c4-2 8 0 9 4-4 2-8 0-9-4z"/><path d="M19 58h26"/>',
"bowl": '<path d="M7 30h50c0 14-11 23-25 23S7 44 7 30z"/><path d="M20 30c-1-6 5-11 12-11 8 0 13 6 9 11"/><path d="M27 30c0-4 4-6 7-4"/><circle cx="32" cy="23" r="1.2"/><path d="M24 58h16"/>',
"hummus": '<ellipse cx="32" cy="34" rx="25" ry="12"/><path d="M14 34c0-5 8-8 18-8s18 3 18 8"/><path d="M22 34c2-4 8-5 12-3s4 6-1 7"/><circle cx="26" cy="30" r="1"/><circle cx="38" cy="33" r="1"/><path d="M7 34v4c0 7 11 12 25 12s25-5 25-12v-4"/>',
"falafel": '<ellipse cx="32" cy="46" rx="26" ry="8"/><circle cx="21" cy="36" r="7"/><circle cx="35" cy="34" r="7"/><circle cx="28" cy="24" r="7"/><circle cx="44" cy="40" r="5"/><path d="M19 35h0M34 33h0M27 23h0" stroke-width="2.6"/>',
"baklava": '<path d="M32 10l13 13-13 13-13-13z"/><path d="M19 23 7 35l13 13 12-12"/><path d="M45 23l12 12-13 13-12-12"/><path d="M32 16v14M25 23h14"/><circle cx="32" cy="23" r="1.3"/><circle cx="20" cy="35" r="1.3"/><circle cx="44" cy="35" r="1.3"/>',
"salad": '<path d="M8 32h48c0 13-11 22-24 22S8 45 8 32z"/><path d="M14 32c-1-7 4-12 10-12-1-5 5-9 9-6 3-4 10-2 10 3 6 0 9 6 7 15"/><circle cx="28" cy="26" r="2.2"/><circle cx="38" cy="25" r="2.2"/><path d="M22 58h20"/>',
"fries": '<path d="M18 30h28l-4 26H22z"/><path d="M22 30 20 10M27 30l-1-22M32 30V7M37 30l1-21M42 30l2-18"/><path d="M27 42c2 3 8 3 10 0"/>',
"drink": '<path d="M22 14h20l-2.5 44h-15z"/><path d="M23 24h18"/><path d="M36 14 40 4h6"/><circle cx="29" cy="36" r="1.4"/><circle cx="34" cy="44" r="1.4"/><circle cx="30" cy="50" r="1.4"/>',
"pita": '<circle cx="32" cy="32" r="23"/><circle cx="32" cy="32" r="17"/><circle cx="25" cy="27" r="1.3"/><circle cx="37" cy="25" r="1.3"/><circle cx="40" cy="36" r="1.3"/><circle cx="28" cy="39" r="1.3"/><circle cx="33" cy="32" r="1.3"/>',
"sandwich": '<path d="M8 30c0-9 11-15 24-15s24 6 24 15z"/><path d="M8 34c4 3 8-2 12 1s8-2 12 1 8-2 12 1 8-2 12-1"/><path d="M9 40h46"/><path d="M8 44h48c0 5-4 7-8 7H16c-4 0-8-2-8-7z"/><path d="M20 22l3 2M30 20l2 2M40 22l2 2"/>',
"chicken": '<path d="M34 14c-12 0-22 9-22 20 0 6 4 12 11 12h15c11 0 18-8 18-17 0-8-9-15-22-15z"/><path d="M38 46l6 9M46 46l6 7"/><circle cx="54" cy="54" r="2"/><circle cx="46" cy="56.5" r="2"/><path d="M20 28c3-4 7-6 12-6"/>',
"cheese": '<path d="M8 40 40 16l16 10v18H8z"/><path d="M8 40h48"/><circle cx="22" cy="48" r="2.4"/><circle cx="38" cy="50" r="2"/><circle cx="46" cy="32" r="2.6"/><circle cx="32" cy="30" r="1.6"/>',
"leaf": '<path d="M32 6c11 8 16 17 16 26a16 16 0 0 1-32 0c0-9 5-18 16-26z"/><path d="M32 16v42"/><path d="M32 30l-7-6M32 38l8-7M32 46l-8-6"/>',
"pastry": '<path d="M10 40c0-12 10-20 22-20s22 8 22 20z"/><path d="M10 40h44l-4 10H14z"/><path d="M20 30c4-4 8-4 12 0s8 4 12 0"/><circle cx="32" cy="16" r="3"/>',
"lantern": '<path d="M32 4v6"/><path d="M26 10h12l2 6H24z"/><path d="M24 16c-6 6-8 14-8 20 0 8 7 12 16 12s16-4 16-12c0-6-2-14-8-20"/><path d="M32 16v32M22 26h20M18 38h28"/><path d="M28 48l-2 8h12l-2-8"/>',
"fig": '<path d="M32 10c3 0 4 3 4 5 9 3 16 13 16 23a20 20 0 0 1-40 0c0-10 7-20 16-23 0-2 1-5 4-5z"/><path d="M32 10c0-3 2-5 5-6"/><path d="M26 34c2 6 10 6 12 0"/><circle cx="32" cy="32" r="1.4"/>',
"crocus": '<path d="M32 58V30"/><path d="M32 30c-8-2-12-10-10-20 6 2 10 8 10 20z"/><path d="M32 30c8-2 12-10 10-20-6 2-10 8-10 20z"/><path d="M32 30c-3-8-1-16 0-22 1 6 3 14 0 22z"/><path d="M26 44c-6-2-10 0-12 4M38 44c6-2 10 0 12 4"/>',
"star": '<path d="M32 4l7 13 14-4-4 14 13 7-13 7 4 14-14-4-7 13-7-13-14 4 4-14-13-7 13-7-4-14 14 4z"/><circle cx="32" cy="34" r="8"/>',
"menu": '<rect x="14" y="8" width="36" height="48" rx="3"/><path d="M22 20h20M22 28h20M22 36h14M22 44h18"/>',
}

def icon(name, cls="ico", sw=1.6):
    return f'<svg class="{cls}" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
