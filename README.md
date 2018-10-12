dollarhex2int Preview
================

![ScreenShot](
        dollarhex2int/example.jpg
      )

## Summary
This plugin for Sublime Text shows the hex value (typically used e.g. in 8bit assembly language) as integer in the status bar.

## Example
$F3 -> 243

$0f -> 15

## Install

To make this work the word separators in Sublime Text need to be adjusted

In your settings, change
`````
"word_separators": "./\\()\"'-:,.;<>~!@#$%^&*|+=[]{}`~?"
`````

to

`````
"word_separators": "./\\()\"'-:,.;<>~!@#%^&*|+=[]{}`~?"
`````


#### Git Clone
Clone this repository in to the Sublime Text "Packages" directory, which is located where ever the
"Preferences" -> "Browse Packages" option in Sublime takes you.

## hex2int
Based on hex2int by unknownuser888
https://github.com/unknownuser88/hex2int



---
