# Drinks Quiz

Two pages, linked by the tabs at the top:

- **Bottles** (`index.html`): brand-and-category flashcards
- **Drinks** (`drinks.html`): random 1–3 drink order tickets for practicing the 50 packet recipes, with shot rounds, self-grading, missed-drink drilling, an optional timer, and optional recipe check (glass, pour, garnish, straw)

## Bottles

Flashcards for the Minnesota School of Bartending brand-and-category test: 185 beers, wines, and call liquors. Each card shows the brand (with a pronunciation guide where needed); flip it to see the category and a photo of the bottle.

- Filter by Beer / Wine / Liquor
- Tap to flip, then mark **Got it** or **Missed it**
- Drill only the cards you missed at the end
- Keyboard: Space flips, → / 1 = got it, ← / 2 = missed

The whole app is a single self-contained `index.html` (photos are embedded), so it runs on GitHub Pages with no build step.

`src/` holds the card data (`cards.json`) and the template used to generate `index.html`.

Photo credits: some bottle photos come from Wikimedia Commons and Open Food Facts (CC BY-SA); the rest are product photos.
