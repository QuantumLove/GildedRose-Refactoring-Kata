
# Review & Recommendations for the Gilded Rose

## Intro

This letter gives insight into the design decisions taken and explores some technical considerations to further enable the Gilded Rose emporium in the future. 

## The problem with the previous design

A chain of if/elses is very hard to read. This because multiple conditions can mix and match and this results in inumerous "branches", hard to fit in our head.

When the requirements are specified, we give then in short and straightforward bulletpoints, and that is what the code should reflect.

Besides saving a few hairs from the maintainers, it makes it way easier to spot edge cases so that tests can be written for those. For example, in the previous code nothing prevents Backstage passes from increasing its quality over 50, even though that is not possible.

## The Descriptor Architecture

The descriptor architecture packages the code into descriptions of what happens to each item as each iteration (day) goes by.

We make the distinction between two types of behavior: The default and the special one.

At the moment an item can only have one time of special behavior, so each descriptor can only apply to one item, making it easy to have a class for each behavior where you can fully understand the Item, that inherits the default behavior so you can focus on the differences.

The applied architecture might look like a bit of an overkill, especially for such a small amount of special items, but it should be easier to maintain and more flexible as we grow than, for example, using a dictionary that maps item names to functions.
And actually, in the end it is similar to a "dicitonary switch" or some kind of [function overloading](https://stackoverflow.com/questions/6434482/python-function-overloading
https://www.artima.com/weblogs/viewpost.jsp?thread=101605) but it feels more organized and ready for complex future new features.

### Adding new items

The `special_item` decorator makes sure the item is registered, and it should be hard to forget it when developing. One could add an additional test to match the GeneralDescriptor subclasses to the descriptors registered, but I think there is enough overengineering in this code already.

### Descriptors could be mix-ins

The way to find/apply descriptors could be further improved.
This current solution is allows for items to be generic or being one and only one type of special item.
We might see in the future adding multiple types to an item, expand on categories such as "conjured", like a "conjured brie" perhaps (the older it is, the better it tastes, and the less calories it has).

Descriptors in that case should become mix-ins and be applied in cascade according to a rules engine that checks their priority and combines multiple conditions to see if they should match.

## Transfering the aging behavior responsability from the GR to the Item

The Goblin has done such a great job with the Item class, I understand that it is a delicate piece of code.

Still, I belive that the quality update, being an intrinsic behavior of the items themselves, should be a property of the Item class, instead of the current solution where we are applying an "aging" operation to the Item.

This would allow for the GildedRose class to be oblivious to the nature of the items and just focus on signaling them that time has passed.

We can then create Item subclasses for each item type or add a method that calculates which descriptor to use at runtime if we expect that items might have a complex behavior in the future.

### Ways around the Goblin "legacy code"

The restriction to not update that code could be subverted:

* We can duplicate the Item class and add more features, and at runtime replace the items in the store with their modern counterparts. This is awful because other services that might want to use these objects might expect the original interface and they will break

* Monkeypatch some properties to the class directly. Again this runs into the problems above but also it would make it way harder to read and maintain.

Besides these being bad architectures, it will upset the Goblin anyway, solutions should come from a consensus of all parties.

## Nitpicks

* Would like to include the quality restriction (between 0 and 50) inside the "update_quality" method but it would transfer that responsability to each child descriptor. Since it is such an unsual feature (only Sulfuras at the moment) it is more practical.
