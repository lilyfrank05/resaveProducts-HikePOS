
# Re-save Products in Hike POS

Attention: It's designed for [Hike POS](https://hikeup.com/) only.

## When you may need this

Sometimes, due to unknown reason, the sync of products might not have been triggered properly, and the manual sync 
doesn't work. The only option is to let the system think the product is updated to trigger the sync from Hike POS to 
3rd party. You will need to re-save the product. To help with the efficiency of doing this for many products, you may 
use this script.

## What you will need to prepare

To do this, you will need access to the Hike store and the SKU list of the products you'd like to re-save. To be more 
specific, you will need to the following.

- Store ID
- Username
- Password
- An Excel sheet of the SKU

### What you will need in the SKU sheet

Just make an SKU list of the products. Put them in the first column, and include one worksheet only. If it's a variant 
product, you don't need to include the SKU of the variants, because you will get the same product in the filtered 
product list when using the SKU of the parent product and that of a variant.

## How to use it

Run the python file, and you'll be asked 4 questions.
- Please enter the Hike account ID: (_Please enter the store ID here._) 
- Please enter the Hike username: (_Please enter the username here._) 
- Please enter the password: (_Please enter the password here._) 
- Where's the file? (_Please use the file path here. E.g. /Users/frank/Downloads/SKU.xlsx_)
