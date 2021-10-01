# process_my_sony_jpgs

Sony cameras are dumb, they produce around 30MB per shot or even larger, some bursts are not in a group photos, filename sometimes duplicate, I wanna create a tool for myself to batch rename these files and able to do some AI operations.

## current operations
* rename: rename file from `XXX` to `YYYY-MM-DD_XXX`
* resize: create a `6666` resolution file.
 
## how to run (Only MAC or Linux)
you need to have swiss-army-knife image tool imageMagick, `brew install imagemagick` or `apt install iamgemagick`

`git clone` this repo and run with:
`python3 process_sony_jpgs.py`
