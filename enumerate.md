```python
best_buy_items[0]["name"]
```

* `[0]` → means “the first item in the list” (because Python starts counting at 0).
* `["name"]` → means “look inside that dictionary and grab the name.”

So this prints:

```
Samsung 55" 4K UHD TV
```

If you want the **price** of the second item:

```python
best_buy_items[1]["price"]
```

---

### 🔢 What is `enumerate`?

Normally, when you loop over a list, you just get the items.
But sometimes you also want the **number** (the position in the list).

That’s what `enumerate` does: it gives you **both the index number AND the item**.

Example from your code:

```python
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
```

This does two things:

1. `index` → the position in the list (0, 1, 2, 3, …).
2. `item` → the dictionary at that position.

So the output looks like:

```
0 : Samsung 55" 4K UHD TV
1 : LG 65" OLED TV
2 : Sony Noise Cancelling Headphones
...
```

It’s like making a **numbered shopping list** automatically.

---

✅ **Summary for a middle schooler:**

* A dictionary is like a **labeled backpack pocket** (key = label, value = stuff inside).
* A list of dictionaries is like a **shopping catalog**.
* `["name"]` or `["price"]` lets you pull out a specific piece of info.
* `enumerate` is like saying: “Give me the item AND its number in line.”

---

![Dictionary Diagram](output.png)