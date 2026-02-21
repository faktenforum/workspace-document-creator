# Typst — Native PDF Generation

**Use when:** User wants PDF, and you write Typst source (`.typ`) directly. For Markdown→PDF, see [document-creation-pandoc-typst.md](document-creation-pandoc-typst.md).

## Compile

```bash
typst compile document.typ document.pdf
# Watch mode (re-compile on change):
typst watch document.typ document.pdf
# List available fonts:
typst fonts
```

**Error handling:** If compilation fails:
1. Read the error message — Typst provides helpful error locations
2. Check https://typst.app/docs/ for correct syntax
3. Try alternative syntax (e.g., content block vs. function call)
4. After 2–3 attempts, hand off to developer router with workspace context

## Page Setup

```typst
#set page(paper: "a4", margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm))
#set page(numbering: "1")
#set page(header: align(right)[My Document])
#set page(footer: align(center)[Page #counter(page).display()])
```

## Text & Font

```typst
#set text(font: "DejaVu Sans", size: 11pt, lang: "de")
#set par(justify: true, leading: 0.65em)
```

Available fonts: DejaVu Sans, DejaVu Serif, DejaVu Sans Mono. Check with `typst fonts`.

## Headings, Lists, Links

```typst
= Heading 1
== Heading 2
- Bullet list
+ Numbered list
/ Term: Definition
#link("https://example.com")[Click here]
See @introduction
= Introduction <introduction>
```

## Tables, Images, Code, Math

```typst
#table(columns: (auto, 1fr, 1fr), align: (left, right, right), ...)
#image("logo.png", width: 50%)
#figure(image("chart.png", width: 80%), caption: [Sales overview])
`inline code`
$ x^2 + y^2 = z^2 $
```

## Spacing, Boxes, Show Rules

```typst
#v(1cm)   // vertical space
#pagebreak()
#line(length: 100%)   // horizontal rule

#block(fill: rgb("#e8f4f8"), inset: 12pt, radius: 4pt)[Highlighted block]

#show heading.where(level: 1): it => { set text(size: 18pt); it.body }
#outline(depth: 2)   // table of contents
```

## Alignment

```typst
#align(center)[Centered text]
#align(right)[Right-aligned]
#align(center + horizon)[Centered both]
```

## Templates

### Letter (DIN 5008 style)

```typst
#set page(paper: "a4", margin: (top: 2.7cm, bottom: 2.5cm, left: 2.5cm, right: 2cm))
#set text(font: "DejaVu Sans", size: 11pt, lang: "de")
#set par(justify: true, leading: 0.65em)

#align(right)[
  Max Mustermann \\
  Musterstraße 1 \\
  12345 Musterstadt \\
  #link("mailto:max@example.com") \\
  +49 123 456789
]

#v(1.5cm)

Firma GmbH \\
z. Hd. Frau Schmidt \\
Beispielweg 42 \\
54321 Beispielstadt

#v(1cm)
#align(right)[Musterstadt, 10. Februar 2026]
#v(1cm)

*Betreff: Anfrage zur Zusammenarbeit*
#v(0.5cm)

Sehr geehrte Frau Schmidt,

Lorem ipsum...

Mit freundlichen Grüßen
#v(1cm)
Max Mustermann
```

### Report

```typst
#set page(paper: "a4", margin: 2.5cm, numbering: "1")
#set text(font: "DejaVu Serif", size: 11pt, lang: "de")
#set par(justify: true, leading: 0.65em)
#set heading(numbering: "1.1")

#align(center + horizon)[
  #text(size: 24pt, weight: "bold")[Projektbericht 2026]
  #v(1cm)
  #text(size: 14pt)[Abteilung Forschung & Entwicklung]
  #v(2cm)
  #text(size: 12pt)[Max Mustermann \\ ACME Corp \\ 10. Februar 2026]
]

#pagebreak()
#outline(depth: 2)
#pagebreak()

= Einleitung
...
```

### Invoice

```typst
#set page(paper: "a4", margin: 2.5cm)
#set text(font: "DejaVu Sans", size: 10pt, lang: "de")

#let invoice_nr = "2026-0042"
#let items = (
  (desc: "Webdesign", qty: 1, price: 2500.00),
  (desc: "Hosting", qty: 12, price: 9.99),
)
#let subtotal = items.map(i => i.qty * i.price).sum()
#let tax = subtotal * 19 / 100
#let total = subtotal + tax

#table(
  columns: (1fr, auto, auto, auto),
  align: (left, center, right, right),
  table.header([*Beschreibung*], [*Menge*], [*Einzelpreis*], [*Gesamt*]),
  ..items.map(i => (i.desc, str(i.qty), [€ #calc.round(i.price, digits: 2)], [€ #calc.round(i.qty * i.price, digits: 2)])).flatten(),
)
#align(right)[Zwischensumme: €#calc.round(subtotal, digits: 2) \\ MwSt.: €#calc.round(tax, digits: 2) \\ *Gesamt: €#calc.round(total, digits: 2)*]
```

## Troubleshooting

- **align syntax:** Use `#align(center)[content]` or `#align(center, [content])`
- **Font not found:** Use DejaVu Sans/Serif/Mono
- **Image not found:** Path relative to `.typ` file; save images in workspace first
