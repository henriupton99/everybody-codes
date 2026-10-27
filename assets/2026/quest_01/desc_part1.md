### Part I

Story section

I told Frodoff, "Come on. We need to leave. Now."
  
  
Questions could wait until we were on the road.
Fortunately, he trusted me enough not to ask why.
That was probably for the best. Explaining that he had accidentally accepted a rather unfortunate destiny by picking up a suspicious-looking stone was not the sort of conversation one had before breakfast.

Before we left Quackshire, there was one last thing we had to check:
the village defences.

Halfbits were delightful folk: brave when necessary, generous by nature, and spectacularly relaxed about routine maintenance.
That was rarely a good combination when the village defences depended on ancient magic.

Many years earlier, we had planted a forest of elven pines around the village.
Their pine cones could be arranged into enchanted formations that repelled hostile magical creatures.
The outposts around the village were arranged in three defensive rings, each using a different type of formation.
In theory, every outpost should have been ready.
In practice, this was Quackshire.

Each outpost had to build exactly one formation using all of its enchanted pine cones.
The first type of protective formation was simple.
The pine cones had to completely fill a square on a grid.
The smallest valid formation was therefore a 1 x 1 square, requiring just

```text
 1
```

pine cone.
Larger squares worked in exactly the same way:

```text
1 x 1     2 x 2      3 x 3  ...

#         ##         ###
          ##         ###
                     ###
```

We inspected every outpost in the first defensive ring.
Unsurprisingly, quite a few pine cones had long since lost their magic and needed replacing.
We wrote down how many enchanted pine cones each outpost still had #YOUR\_NOTES,
then set out to **collect exactly enough fresh ones for every outpost to build a complete square using all of its pine cones**.

For example, if an outpost had

```text
 10
```

enchanted pine cones, that was one too many for a 3 x 3 square,
but six too few for a 4 x 4 square.
The outpost therefore had to collect exactly

```text
 6
```

new pine cones:

```text
 10 + 6 = 16
```

.

**Example based on the following notes:**

```text
3,11,12,16,24,25
```

* The first outpost had

  ```text
   3
  ```

  enchanted pine cones, so it had to collect

  ```text
   1
  ```

  more to build a 2 x 2 square.
* The second outpost had

  ```text
   11
  ```

  pine cones and needed

  ```text
   5
  ```

  more to complete a 4 x 4 square.
* The third outpost had

  ```text
   12
  ```

  pine cones and needed

  ```text
   4
  ```

  more to complete a 4 x 4 square.
* The fourth outpost already had exactly

  ```text
   16
  ```

  pine cones, enough to build a 4 x 4 square.
* The fifth outpost had

  ```text
   24
  ```

  pine cones and needed

  ```text
   1
  ```

  more to complete a 5 x 5 square.
* The final outpost already had exactly

  ```text
   25
  ```

  pine cones, enough to build a 5 x 5 square.

In total, the outposts had to collect
1 + 5 + 4 + 0 + 1 + 0 =

```text
 11
```

new pine cones.

**How many new pine cones must be collected so that every outpost can build a complete square using all of its pine cones?**