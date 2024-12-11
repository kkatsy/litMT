set saveToLocation to "/Users/kk/Desktop/book_scans/"
set bookName to "Дворянское гнездо (Russian Edition)"
set pageCount to 1
set pathFileName to saveToLocation & bookName
tell application "Kindle" to activate
delay 0.5
tell application "System Events" to ¬
	tell window 1 of application process "Kindle" to ¬
		set {position, size} to {{250, 25}, {919, 870}}
repeat with i from 1 to pageCount
	
	set shellCMD to ¬
		"screencapture -R297,81,855,785 -t jpg '" & ¬
		pathFileName & " - Page " & ¬
		i & " of " & pageCount & ".jpg'"
	
	do shell script shellCMD
	delay 1.5
	--  # Press right-arrow key.
	tell application "System Events" to key code 124
	delay 1.5
	
end repeat
