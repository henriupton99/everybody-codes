---

### Part II

Once the first defensive ring had been secured, we continued to inspect the second one.
Each outpost in this ring had to **build a square frame instead of a filled square.**

As a result, each formation required fewer enchanted pine cones.
**The frame also had to surround at least one empty cell**; otherwise, the magic would not work.
The smallest possible formation was therefore a 3 x 3 frame, requiring

```text
 8
```

pine cones.
Larger square frames worked in the same way:

```text
3 x 3     4 x 4      5 x 5  ...

###       ####       #####
#.#       #..#       #...#
###       #..#       #...#
          ####       #...#
                     #####
```

Once again, we noted how many enchanted pine cones each outpost still had #YOUR\_NOTES.
We then calculated how many additional pine cones had to be collected for every outpost to build a valid square frame
using all of its pine cones.

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
   5
  ```

  more to build a 3 x 3 frame.
* The second outpost had

  ```text
   11
  ```

  pine cones and needed

  ```text
   1
  ```

  more to complete a 4 x 4 frame.
* The next three outposts already had exactly

  ```text
   12
  ```

  pine cones for a 4 x 4 frame,

  ```text
   16
  ```

  for a 5 x 5 frame,
  and

  ```text
   24
  ```

  for a 7 x 7 frame,
  so they did not need to collect any more.
* The final outpost had

  ```text
   25
  ```

  pine cones.
  The next valid formation was an 8 x 8 frame requiring 28 pine cones,
  so it had to collect

  ```text
   3
  ```

  more.

In total, the outposts had to collect
5 + 1 + 0 + 0 + 0 + 3 =

```text
 9
```

new pine cones.

**How many new pine cones must be collected so that every outpost can build a valid square frame using all of its pine cones?**